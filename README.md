# Tax Break! A dungeon crawler about tax season over SSH

This is a Python game that can run over SSH. It is about Due Taxes gone wrong! The beginning is a little tough, but find the right path to get to the fun stuff!

![Tax Break screenshot](PhotoForRead.me.jpg)

Rated PG-13 (fictional violence, uses its one swear.)

## Play online (IPv6 only)

The game is now online. Have fun! Open a terminal and run:

```
ssh -p 2222 2a01:4f9:3a:276e::374
```

Type `yes` if it asks about the host key. No password or username is needed.

> [!NOTE]
> This needs IPv6. Check yours at test-ipv6.com. On Windows, "Unknown error" usually means you don't have IPv6. If you don't, try a phone hotspot (or the Termius app: new host, that address, port 2222, any username), or use Self Host below. The server holds 20 players at once, and it can go down sometimes.

## Self Host

1. **Make sure Python is installed.** This is a Python game, so you need Python.
2. **Make sure pip is installed.** If pip gives you problems, see Troubleshooting.
3. **Download the repo.** Use `git clone https://github.com/GeckoOfDeath/Tax-Break-A-dungeon-crawler-about-tax-season-over-SSH` or the green Code button, then Download ZIP.
4. **Install the requirements.** In the game folder, run `pip install -r requirements.txt`. If you get a pip error, use `python -m pip install -r requirements.txt`.
5. **Start the server.** Run `py ssh_server.py` and leave that window open. If `py` doesn't work, use `python3` or `python`. Make sure you're in the folder with all the files.
6. **Connect.** Open a second terminal and run `ssh -p 2222 localhost`.
7. **Play the game!**

I worked very hard on this game, I really hope you enjoy it. There are 2 endings and a mini boss to discover.

$\color{red}{\textsf{THERE IS NO SECRET ENDING. THERE IS NO SECRET ENDING.}}$

## Troubleshooting

1. Make sure you're in the right folder.
2. Make sure Python is installed.
3. Use `python3` or `python` if `py` doesn't work.
4. If pip is installed and still giving an error, use `python -m pip install -r requirements.txt`.
5. If `requirements.txt` doesn't show up in the folder, re-download the repo.
