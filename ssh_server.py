"""
Tiny SSH server that runs the tax game for anyone who connects.

Setup:   pip install asyncssh
Run:     python ssh_server.py
Play:    ssh -p 2222 localhost          (from a second terminal)

By default it only listens on 127.0.0.1, so only YOUR computer can connect.
No login or password is needed, and it never touches your system's real SSH.
"""

import asyncio
import os
import sys

import asyncssh

HOST = "127.0.0.1"   # change to "0.0.0.0" ONLY if you want others to connect
PORT = 2222

HERE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.join(HERE, "tax_game_v2.py")
HOST_KEY = os.path.join(HERE, "ssh_host_key")


class GameServer(asyncssh.SSHServer):
    def begin_auth(self, username):
        return False  # no password needed


async def handle_client(process):
    # If the client has a real terminal, it won't echo typing, so we do it.
    echo = process.get_terminal_type() is not None

    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    game = await asyncio.create_subprocess_exec(
        sys.executable, "-u", GAME,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
        env=env,
    )

    async def pump_output():
        while True:
            data = await game.stdout.read(1024)
            if not data:
                break
            text = data.decode("utf-8", errors="replace")
            text = text.replace("\r\n", "\n").replace("\n", "\r\n")
            process.stdout.write(text)

    async def pump_input():
        line = ""
        in_escape = False  # swallow arrow keys etc.
        while True:
            data = await process.stdin.read(1024)
            if not data:
                return
            for ch in data:
                if in_escape:
                    if ch.isalpha() or ch == "~":
                        in_escape = False
                    continue
                if ch == "\x1b":
                    in_escape = True
                elif ch in "\r\n":
                    if echo:
                        process.stdout.write("\r\n")
                    game.stdin.write((line + "\n").encode("utf-8"))
                    await game.stdin.drain()
                    line = ""
                elif ch in "\x7f\x08":
                    if line:
                        line = line[:-1]
                        if echo:
                            process.stdout.write("\b \b")
                elif ch in "\x03\x04":  # Ctrl+C / Ctrl+D
                    return
                elif ch >= " ":
                    line += ch
                    if echo:
                        process.stdout.write(ch)

    out_task = asyncio.create_task(pump_output())
    in_task = asyncio.create_task(pump_input())
    await asyncio.wait({out_task, in_task}, return_when=asyncio.FIRST_COMPLETED)

    if game.returncode is None:
        game.kill()
    for task in (out_task, in_task):
        task.cancel()
    process.exit(0)


async def main():
    if not os.path.exists(HOST_KEY):
        asyncssh.generate_private_key("ssh-ed25519").write_private_key(HOST_KEY)

    await asyncssh.create_server(
        GameServer, HOST, PORT,
        server_host_keys=[HOST_KEY],
        process_factory=handle_client,
        encoding="utf-8",
    )
    print(f"Game server running. In another terminal, play with:\n\n    ssh -p {PORT} localhost\n")
    print("Press Ctrl+C here to stop the server.")
    await asyncio.Future()  # run forever


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, OSError) as e:
        if isinstance(e, OSError):
            print(f"Could not start server: {e}\n(Is something already using port {PORT}?)")
        else:
            print("\nServer stopped.")
