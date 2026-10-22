import sys
import random

player_hp = 100
monster1_hp = 50
monster2_hp = 100
monster3_hp = 100
monster4_hp = 100
monster5_hp = 150
monster6_hp = 150
monster7_hp = 150
miniboss_hp = 300
boss_hp = 600


player_attack_damage = 25
cat_heal_amount = 20
monster1_attack = 20
monster2_attack = 20
monster3_attack = 33
monster4_attack = 33
monster5_attack = 34
monster6_attack = 34
monster7_attack = 34
miniboss_attack = 34
boss_attack = 49.5
boss_attack_desperate = 33
max_player_hp = 100
parry = False
door_one_enter = False
door_two_enter = False
door_three_enter = False


def reset_game():

    global player_hp, monster1_hp, monster2_hp, monster3_hp, monster4_hp
    global monster5_hp, monster6_hp, monster7_hp, miniboss_hp, boss_hp
    global player_attack_damage, cat_heal_amount
    global parry, door_one_enter, door_two_enter, door_three_enter

    player_hp = 100
    monster1_hp = 50
    monster2_hp = 100
    monster3_hp = 100
    monster4_hp = 100
    monster5_hp = 150
    monster6_hp = 150
    monster7_hp = 150
    miniboss_hp = 300
    boss_hp = 600

    player_attack_damage = 25
    cat_heal_amount = 20
    parry = False
    door_one_enter = False
    door_two_enter = False
    door_three_enter = False


def main():
    reset_game()
    while True:
        print("\n" + "=" * 40)
        print("You forgot to pay your taxes.")
        print("\n" + "=" * 40)
        print("\nYou're sitting on your couch when you get a notification from the IRS. It says: \"alr brody you forgot to pay your taxes your cooked fr\". Do you?")
        print("1. Respond to the notification")
        print("2. Go play some video games and grab some pizza and ignore it")
        print("Q. Quit game")

        choice = input("\nWhat do you want to do? ").strip().lower()

        if choice == 'q':
            print("\nThanks for playing!")
            sys.exit(0)
        elif choice == '1':
            notification()
            break
        elif choice == '2':
            pizza()
            break


def notification():
    print("\nYou check the notification and it says you have to pay your taxes or else the IRS will come after you.")
    print("1. Go to their office to sort it out.")
    print("2. Go grab that pizza and ignore it.")

    choice = input("\nWhat do you want to do? ").strip()
    if choice == '1':
        print("\nYou grab your car keys, and as you reach the door you hear a knock...")
        dooranswer()

    elif choice == '2':
        print("\nPizza sounds pretty good!")
        pizza()


def pizza():
    print("\nYou grab your pizza and sit down to eat it. You hear a knock on your door. You try to ignore it, but he keeps knocking. Do you?")
    print("1. Go answer the door")
    print("2. Go back to eating your pizza and ignore it.")

    choice = input("\nWhat do you want to do? ").strip()
    if choice == '1':
        print("\nYou go to answer the door...")
        dooranswer()

    elif choice == '2':
        Death1doorknock()


def dooranswer():
    print("\nThe man's voice sounds funny. He is mumbling about being a tax collector. Something doesn't feel right. It's too quick. Do you?")
    print("1. Be normal and open the door")
    print("2. Be a total psycho and blast him through the door with your 12 gauge shotgun")

    choice = input("\nWhat do you want to do? ").strip()
    if choice == '1':
        print("\nYou open the door...")
        death2dooranswer()

    elif choice == '2':
        print("\nWow, look at you, a total psycho. You blast the innocent man through the door with your 12 gauge shotgun...")
        Blastdoorknockerwithshotgunlol()


def Death1doorknock():
    print("\nYou don't answer the door and go back to eating your pizza. You hear a crash, and the last thing you see is your door flying at you.")
    print("Really man, A door? like I know a falling goat killed a guy once, but thats like top 10 most pathetic deaths.")
    print("\nYou died. Game over.")

    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        main()
    else:
        print("\nThanks for playing!")
        sys.exit(0)


def death2dooranswer():
    print("\nYou open the door and see a man in a suit. As he says he's from the IRS, you stare at his head. It's a deformed shark head with thousands of teeth.")
    print("\n uh oh")
    print("\nYou try to run, but a spike-like tongue shoots through you and it all fades to black. Game over.")

    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        main()
    else:
        print("\nThanks for playing!")
        sys.exit(0)


def Blastdoorknockerwithshotgunlol():
    print("\nYou shot the man through the door with your 12 gauge shotgun. Now you've done it. Murder is a crime, you know. He was an innocent civil serva- You look out the shotgun-blasted hole to see a monster's body crumpled on the ground.")
    print("\nYou crazy bastard! Killing the innocent man was the right decision! I gotta say, I was doubting you for a minute there.")
    print("\nWell, now what are you going to do?")
    print("1. Continue to the tax office.")
    print("2. Go grab your cat. I mean, if you're crazy, might as well.")

    choice = input("\nWhat do you want to do? ").strip()
    if choice == '1':
        print("\nYou continue to the tax office.")
        TaxDriveDeath()

    elif choice == '2':
        print("\nYou go grab your cat and head out the door.")
        catdrive()


def TaxDriveDeath():
    print("\nYou're on your way to the tax office when someone runs a red light and hits you.")
    print("If only you had been 1 second later.")
    print("Wait, that didn't look like a ca-")
    print("\nGame over. You died.")

    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        main()
    else:
        print("\nThanks for playing!")
        sys.exit(0)


def catdrive():
    print("\nYou grab your cat and head out the door. You're on your way to the tax office when something runs a red light in front of you and almost hits you.")
    print("The thing smashes into the car in front of you, and you see that it's a strange bat-like creature.")
    print("\nWAIT, IF YOU HAD BEEN 1 SECOND LATER, YOU WOULD HAVE BEEN HIT BY THE BAT-LIKE CREATURE. IT WAS MEANT TO HIT YOU!!!")
    print("\nYou should be dead, but your cat saved you. Weirdo. What do you do next?")
    print("1. Pedal to the metal, baby!")
    print("2. Use that stupid 12 gauge shotgun to blast the bat-like creature.")

    choice = input("\nWhat do you want to do? ").strip()
    if choice == '1':
        print("\nYou speed past the creature, toward the tax office.")
        taxoffice()
    elif choice == '2':
        print("\nYou raise your shotgun to blast the bat.")
        Fight1()


def Fight1():
    global player_hp
    global monster1_hp

    print("\nThe bat-thingy turns toward you, eyes staring down your shotgun barrel.")

    while player_hp > 0 and monster1_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"Monster's Health: {monster1_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            monster1_hp -= player_attack_damage
            print("\nYou blast the creature in the face! It scrambles.")

        elif choice == "2":
            print("\nYou brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nYour cat heals {healed} health. Crazy.")

        else:
            print("\nThat's not an option, idiot.")
            continue

        if monster1_hp <= 0:
            Monster1win()
            break

        if random.random() < 0.4:
            if choice == "2":
                print("The creature attacks you, but you blocked it!")
            else:
                player_hp -= monster1_attack
                print(f"The creature attacks you for {monster1_attack} damage!")

        else:
            print("The creature's attack misses.")

    if player_hp <= 0:
        print("\nThe monster rips your lungs out. You died while trying to file your taxes. Kinda pathetic.")
        died()


def Monster1win():
    print("\n" + "-" * 30)
    print("\nYou blast the monster one final time and it splatters against the car behind it.")
    taxoffice()


def died():
    print("\nGame over. You died.")
    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        main()
    else:
        print("\nThanks for playing!")
        sys.exit(0)


def taxoffice():
    print("\nYou race down the road toward the tax office. This is crazy! I mean, you knew the IRS was bad, but not this bad!!")
    print("\n" + "+" * 30)
    print("\nChapter 2: THE TAX OFFICE")
    print("\n" + "+" * 30)
    print("\nYou arrive at the tax office. The parking lot is almost empty.")
    print("You should park and walk in. There's no other option.")
    print("1. Park and walk in")
    print("2. *sigh* Smash your car through the front door.")

    choice = input("\nWell, you're going to walk in, right? ")
    if choice == "1":
        print("\nThank god. I knew you were crazy, but you're not THAT crazy.")
        walk_in()

    elif choice == "2":
        print("\nYou press down on your peda- WAIT NO NO WHAT ARE YOU DOING?")
        print("Your car smashes into the front of the government agency.")
        smash_in()


def smash_in():
    ITALIC = "\033[3m"
    RESET = "\033[0m"
    print(f"\nYou smashed your {ITALIC}car{RESET} into a {ITALIC}government agency{RESET}.")
    print("Your car smashes through the glass front doors, rips through some red something, and plows into the front desk.")
    print("\nYou step out of the car. Thankfully, the front desk was empty. Whatever your car hit appeared to have 10 eyes, so it was not human.")
    print("*cough* or it could have been 5 people *cough*")
    print("\nDo you?")
    print("1. Inspect the room.")
    print("2. Charge into the first door you see.")

    choice = input("\nI mean, you should check it out, right? ")
    if choice == "1":
        print("\nYou check out the room.")
        frontroom()

    elif choice == "2":
        print("\nYou charge blindly into a room. Smart.")
        Door1_2()


def walk_in():
    global player_hp
    global monster2_hp

    print("\nYou walk into the office. Almost instantly you see it: a huge red blob with a ton of eyes. It charges at you!")

    while player_hp > 0 and monster2_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"Monster's Health: {monster2_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            monster2_hp -= player_attack_damage
            print("\nYou blast the creature in the face! It scrambles.")

        elif choice == "2":
            print("\nYou brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nYour cat heals {healed} health. Crazy.")

        else:
            print("\nThat's not an option, idiot.")
            continue

        if monster2_hp <= 0:
            Monster2win()
            break

        if random.random() < 0.4:
            if choice == "2":
                print("The creature attacks you, but you blocked it!")
            else:
                player_hp -= monster2_attack
                print(f"The creature attacks you for {monster2_attack} damage!")

        else:
            print("The creature's attack misses.")

        if player_hp <= 0:
            print("\nThe monster rips your heart out. You died while trying to file your taxes. Kinda pathetic.")
            died()


def Monster2win():
    print("\nThe red covers you. Not blood, but strange matter. It doesn't matter; you need to get your taxes done.")
    print("\nDo you want to:")
    print("1. Check out the room")
    print("2. Charge into the first door you see.")

    choice = input("\nI mean, you should check it out, right? ")
    if choice == "1":
        print("\nYou check out the room.")
        frontroom()

    elif choice == "2":
        print("\nYou charge blindly into a room. Smart.")
        Door1_1()


def frontroom():
    print("\nYou look around the room. It seems to have been left only recently. There are 3 doors on the back wall.")
    print("Which door do you choose?")
    print("1. The first door, labeled \"Meeting Rooms\".")
    print("2. The second door, labeled \"Employees Only\".")
    print("3. The third door, labeled \"Bathroom\".")

    choice = input("\nWhat door do you enter? ")
    if choice == "1":
        print("\nYou enter the first room.")
        Door1_1()
    elif choice == "2":
        print("\nYou enter the second door.")
        Door1_2()
    elif choice == "3":
        print("\nYou enter the third door.")
        Door1_3()


def Door1_1():
    global player_hp
    global monster3_hp
    print("\nYou enter the meeting room. Desks line the room. It almost seems as though there had been a fight here.")
    print("\nWait... One of those desks has a mouth!")

    while player_hp > 0 and monster3_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"Mimic Health: {monster3_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            monster3_hp -= player_attack_damage
            print("\nYou blast the creature in the face! It scrambles.")

        elif choice == "2":
            print("\nYou brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nYour cat heals {healed} health. Crazy.")

        else:
            print("\nThat's not an option, idiot.")
            continue

        if monster3_hp <= 0:
            Monster3win()
            break

        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("You parry the attack! The monster takes 50 damage.")
                    monster3_hp -= 50
                    if monster3_hp <= 0:
                        Monster3win()
                        break
                else:
                    print("The creature attacks you, but you blocked it!")

            else:
                player_hp -= monster3_attack
                print(f"The creature attacks you for {monster3_attack} damage!")

        else:
            print("The creature's attack misses.")

        if player_hp <= 0:
            print("\nThe monster rips your head off. You died while trying to file your taxes. Kinda pathetic.")
            died()


def Door1_2():
    global player_hp
    global monster4_hp
    print("\nThe employee room is overrun with bloody vines. In the center of the room there is... a... a... A NEW SHOTGUN!!!!")
    print("\nWait... Standing in front of the shotgun is a pair of pants, filled with vines. Isn't this supposed to be a tax game?")

    while player_hp > 0 and monster4_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"Pants Health: {monster4_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            monster4_hp -= player_attack_damage
            print("\nYou blast the creature in the face! It scrambles.")

        elif choice == "2":
            print("\nYou brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nYour cat heals {healed} health. Crazy.")

        else:
            print("\nThat's not an option, idiot.")
            continue

        if monster4_hp <= 0:
            Monster4win()
            break

        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("You parry the attack! The monster takes 50 damage.")
                    monster4_hp -= 50
                    if monster4_hp <= 0:
                        Monster4win()
                        break
                else:
                    print("The creature attacks you, but you blocked it!")

            else:
                player_hp -= monster4_attack
                print(f"The creature attacks you for {monster4_attack} damage!")

        else:
            print("The creature's attack misses.")

        if player_hp <= 0:
            print("\nThe monster rips your head off. You died while trying to file your taxes. Kinda pathetic.")
            died()


def Door1_3():
    print("\nYou need to use the bathroom or something.")
    print("\nYou see a box of... catnip? On a toilet?")
    print("Grab it?")
    print("1. Get the boost.")
    print("No other options.")

    choice = input("\nContinue? ")
    if choice == "1":
        print("\nYes, continue. Nothing else there.")
        catnip1()

    elif choice == "2":
        print("\nNO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO")
        print("NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO")
        print("NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO")
        print("NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO")
        print("NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO")
        print("\nYou see a large rectangular cutout, hinges, and a door made of tiles.")
        secret_ending_1()


def secret_ending_1():
    print("\nGod. Please. Don't. Push. It. Open.")
    print("1. Turn back. Grab the catnip. Leave.")
    print("2. Open. The. Door.")

    choice = input("\nPlease don't open the door. Taxes. Taxis. tackds. ")
    if choice == "1":
        print("\nOh thank god.")
        catnip1()
    elif choice == "2":
        print("\nHate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        print("Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate")
        secret_ending_lockpick()


def secret_ending_lockpick(code=None, attempts=8, length=5, show_shift_hints=True):
    if code is None:
        code = "".join(random.choice("0123456789") for _ in range(length))
    length = len(code)
    ordinals = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    print("\nYou push open the door. Another door looms before you, a 5-digit lock in the center. I can't stop you now.")
    print(f"Enter a 5-digit number to test the lock. ({attempts} attempts)\n")

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"[{attempt}/{attempts}] Try: ").strip()
            if guess.isdigit() and len(guess) == length:
                break
            print("Enter 5 digits.")

        result = ["none"] * length
        leftover = []
        for i in range(length):
            if guess[i] == code[i]:
                result[i] = "click"
            else:
                leftover.append(code[i])
        for i in range(length):
            if result[i] == "none" and guess[i] in leftover:
                result[i] = "shift"
                leftover.remove(guess[i])

        for i in range(length):
            slot = ordinals[i] if i < len(ordinals) else f"#{i + 1}"
            if result[i] == "click":
                print(f"  {guess[i]} in the {slot} slot... *click*")
            elif result[i] == "shift" and show_shift_hints:
                print(f"  {guess[i]} in the {slot} slot... something shifts, but not here.")

            else:
                print(f"  {guess[i]} in the {slot} slot... nothing.")
        if guess == code:
            print("\nThe door swings open.")
            secret_ending_end()
            return

    print("\nThe door makes a terrible noise, and you're pushed out of the room. The secret door is gone.")
    catnip1()


def secret_ending_end():
    print("\nYou weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")
    print("You weren't ever supposed to finish your taxes.")

    print("\n" + "+" * 30)
    print("\nSecret Ending: Bertha, the Tax Lady.")
    print("\n" + "+" * 30)
    print("\nYou walk into a room. The floor and walls are covered in stacks of paper. A small southern lady sits at a desk in the center of the room.")
    print("She's typing on her typewriter when she sees you.")
    print("\n\"Hello there, darling!\" She squints her eyes. \"Oh! I know you! I just sent you a message. Wow, you got here quick as a bullet, didn't you?\"")
    print("\nShe laughs to herself. \"I haven't seen anyone show up since they moved me to this room. I've been doing everyone's taxes, but no one but you has come to pick them up!\"")
    print("\nShe stands up slowly, walks over to you, and pets the cat on your shoulder. \"Aren't you a sweetie pie?\"")
    print("\nShe continues past you and reaches into a pile of papers, pulling out a few and handing them to you.")
    print("\n\"There you go. Just scan those into the interweb doohickey and you'll be good to go. See you next year!\"")
    print("\n" + "*" * 30)
    print("\nThe END!!! You actually did your taxes!")
    print("You weren't supposed to be able to do that...")
    print("\n" + "*" * 30)

    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        main()
    else:
        print("\nThanks for playing!")
        sys.exit(0)


# !!!!!!!!!!!!!!!!!! end of secret ending !!!!!!!!!!!!!!!!!!


def catnip1():
    global cat_heal_amount
    global door_three_enter
    door_three_enter = True
    cat_heal_amount = 33
    print("\nYour cat purrs, and she seems to become more powerful. Or maybe you're going crazy. Probably crazy!")
    print("Continue?")

    choice = input("y/n: ")
    if choice == "y":
        print("\nYou continue.")
        stairs()
    elif choice == "n":
        print("\nYou wait. And wait. And wait. And wait... and more waiting. Over time your body decays. Wow. You died standing in a restroom. Terrible.")
        died()


def Monster3win():
    global door_one_enter
    global parry
    door_one_enter = True
    parry = True
    print("\nThe desk crumples, revealing a new shield.")
    print("You can now parry. Every block has a small chance of returning a hefty blow.")
    print("\nContinue through the door ahead?")

    choice = input("y/n: ")
    if choice == "y":
        print("\nYou continue.")
        stairs()
    elif choice == "n":
        print("\nYou wait. And wait. And wait. And wait... and more waiting. Over time your body decays. Wow. You died standing in a random room. Terrible.")
        died()


def Monster4win():
    global player_attack_damage
    global door_two_enter
    door_two_enter = True
    player_attack_damage = 33
    print("\nThe pants burst apart in a spray of denim and bloody gunk. Wow. You beat a pair of pants.")
    print("Sadly, the only thing you're focused on is the bright and shiny shotgun. After grabbing it, you notice it looks stronger than your last.")
    print("\nContinue through the door ahead?")

    choice = input("y/n: ")
    if choice == "y":
        print("\nYou continue.")
        stairs()
    elif choice == "n":
        print("\nYou wait. And wait. And wait. And wait... and more waiting. Over time your body decays. Wow. You died standing in a random room. Terrible.")
        died()


def stairs():
    print("\nYou stand in a stairwell. Meaty vines lead up the walls toward the next floor.")
    print("You also see the other rooms, but there's no point going back to a room you've already been in.\n")
    if door_one_enter == False:
        print("1. Enter door 1 (Meeting Room)")
    if door_two_enter == False:
        print("2. Enter door 2 (Employee Room)")
    if door_three_enter == False:
        print("3. Enter door 3 (Bathroom)")
    print("c. Continue.")

    choice = input("\nWhat do you do? ")
    if choice == "1":
        if door_one_enter == False:
            print("\nYou head back into door 1.")
            Door1_1()
        else:
            print("\nYou have already been here. You cannnt goo babbaackkkk")
            print("EEEEEEEEEERRRRRRRRRROOOOOOOOOOOOORRRRRRRRRRRR")
            died()
    if choice == "2":
        if door_two_enter == False:
            print("\nYou head back into door 2.")
            Door1_2()
        else:
            print("\nYou have already been here. You cannnt goo babbaackkkk")
            print("EEEEEEEEEERRRRRRRRRROOOOOOOOOOOOORRRRRRRRRRRR")
            died()
    if choice == "3":
        if door_three_enter == False:
            print("\nYou head back into door 3.")
            Door1_3()
        else:
            print("\nYou have already been here. You cannnt goo babbaackkkk")
            print("EEEEEEEEEERRRRRRRRRROOOOOOOOOOOOORRRRRRRRRRRR")
            died()
    if choice == "c":
        print("\nYou continue up the stairwell.")
        chapter3()


def chapter3():
    print("\nYou take a final step, looking around at the office space around you. It looks like an office, but much less normal than the first floor.")
    print("\n" + "+" * 30)
    print("\nChapter 3: The Second Floor")
    print("\n" + "+" * 30)
    print("\nYou look around more. This room seems to be a puzzle. Not a literal puzzle! There are NO PUZZLES in this game. NONE. NONE. NONE.")
    print("\nThere are odd objects all around: chairs stuck to the ceiling, meaty vines running everywhere. You can't see the end of the hall; it's too dark.")
    print("There is a door ahead of you. Shall you enter? You don't have much of a choice.")

    choice = input("\nContinue? (y/n): ")
    if choice == "y":
        print("\nYou continue on, through the dark room.")
        downthehall()
    elif choice == "n":
        print("\nWhat are you doing?")
        print("You stand there for a while. I think you're thinking? After a while, you decide to move forward.")
        downthehall()


def downthehall():
    global player_hp
    global monster5_hp
    print("\nYou continue down the room. The room narrows in front of you.")
    print("You push on, and the room is now a winding tunnel. The ceiling is so low that your cat hops off your shoulder and you have to lean over to fit.")
    print("\nA monster that looks like a man with a TV head, crab walking down the tunnel, approaches you.")
    print("You hear more down the tunnel.")

    while player_hp > 0 and monster5_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"TV Head Health: {monster5_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            monster5_hp -= player_attack_damage
            print("\nYou blast the creature in the face! It scrambles.")

        elif choice == "2":
            print("\nYou brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nYour cat heals {healed} health. Crazy.")

        else:
            print("\nThat's not an option, idiot.")
            continue

        if monster5_hp <= 0:
            Monster6()
            break

        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("You parry the attack! The monster takes 50 damage.")
                    monster5_hp -= 50
                    if monster5_hp <= 0:
                        Monster6()
                        break
                else:
                    print("The creature attacks you, but you blocked it!")

            else:
                player_hp -= monster5_attack
                print(f"The creature attacks you for {monster5_attack} damage!")

        else:
            print("The creature's attack misses.")

        if player_hp <= 0:
            print("\nThe monster rips your head off. You died while trying to file your taxes. Kinda pathetic.")
            died()


def Monster6():
    global player_hp
    global monster6_hp
    print("\nYour shotgun blasts ring through the small space. Your ears bleed.")
    print("And apparently so do the rest of the TV heads' \"ears\", because there are now two more approaching.")
    print("Luckily, the tunnel is too narrow for them to fight you at once, so you fight one at a time.")

    while player_hp > 0 and monster6_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"TV Head Health: {monster6_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            monster6_hp -= player_attack_damage
            print("\nYou blast the creature in the face! It scrambles.")

        elif choice == "2":
            print("\nYou brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nYour cat heals {healed} health. Crazy.")

        else:
            print("\nThat's not an option, idiot.")
            continue

        if monster6_hp <= 0:
            Monster7()
            break

        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("You parry the attack! The monster takes 50 damage.")
                    monster6_hp -= 50
                    if monster6_hp <= 0:
                        Monster7()
                        break
                else:
                    print("The creature attacks you, but you blocked it!")

            else:
                player_hp -= monster6_attack
                print(f"The creature attacks you for {monster6_attack} damage!")

        else:
            print("The creature's attack misses.")

        if player_hp <= 0:
            print("\nThe monster rips your head off. You died while trying to file your taxes. Kinda pathetic.")
            died()


def Monster7():
    global player_hp
    global monster7_hp
    print("\nYour shotgun blasts ring through the small space. Your ears bleed.")
    print("This is getting tiring.")
    print("Last one.")

    while player_hp > 0 and monster7_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"TV Head Health: {monster7_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            monster7_hp -= player_attack_damage
            print("\nYou blast the creature in the face! It scrambles.")

        elif choice == "2":
            print("\nYou brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nYour cat heals {healed} health. weird cat.")

        else:
            print("\nThat's not an option, idiot.")
            continue

        if monster7_hp <= 0:
            tunnelend()
            break

        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("You parry the attack! The monster takes 50 damage.")
                    monster7_hp -= 50
                    if monster7_hp <= 0:
                        tunnelend()
                        break
                else:
                    print("The creature attacks you, but you blocked it!")

            else:
                player_hp -= monster7_attack
                print(f"The creature attacks you for {monster7_attack} damage!")

        else:
            print("The creature's attack misses.")

        if player_hp <= 0:
            print("\nThe monster rips your head off. You died while trying to file your taxes. Kinda pathetic.")
            died()


def tunnelend():
    print("\nFinally, you're almost through the tunnel, but there's a split.")
    print("The side tunnel is maybe half the size. There's a portion of an old office wall with a sign saying HR.")
    print("It feels like there's something strong down there...")
    print("1. Go down the side path.")
    print("2. Continue down the tunnel.")

    choice = input("\nWhat do you choose? ")
    if choice == "1":
        print("\nYou squeeze down the side tunnel.")
        miniboss()
    elif choice == "2":
        print("\nYou continue down the main path.")
        floor2stairs()


def miniboss():
    global player_hp
    global miniboss_hp
    print("\nYou exit the small tunnel to see an office room. It's almost normal, but something feels off.")
    print("Someone... no, something rises up from below a table. Its body is that of a normal office worker, but its head is a briefcase filled with tentacles.")
    print("\nYou brace yourself for a big fight...")

    while player_hp > 0 and miniboss_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"Boss Health: {miniboss_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            miniboss_hp -= player_attack_damage
            print("\nYou blast the boss in the face! It scrambles.")

        elif choice == "2":
            print("\nYou brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nYour cat heals {healed} health. I think your healing too much, you should get better luck.")
        else:
            print("\nThat's not an option, idiot.")
            continue

        if miniboss_hp <= 0:
            minibossWin()
            break

        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("You parry the attack! The monster takes 50 damage.")
                    miniboss_hp -= 50
                    if miniboss_hp <= 0:
                        minibossWin()
                        break
                else:
                    print("The creature attacks you, but you blocked it! How do you block that? Do you hit the gym?")

            else:
                player_hp -= miniboss_attack
                print(f"The creature attacks you for {miniboss_attack} damage!")

        else:
            print("The creature's attack misses.")

        if player_hp <= 0:
            print("\nThe boss's tentacle rips your head off. You died while trying to file your taxes. Kinda pathetic.")
            died()


def minibossWin():
    global player_attack_damage
    print("\nThe briefcase creature screams out, spitting something out of its briefcase as it crumples.")
    print("As the creature dies, you pick up the box, heartless man. The box says:")
    print("\n\"Shotgun bullets, twice as strong as any other!\" There's a lot of shotgun stuff here for an office, but you're too excited to think about that.")
    print("\nVines fall, revealing a new tunnel out.")
    print("Continue?")
    player_attack_damage = player_attack_damage * 2
    choice = input("\nContinue? ")
    if choice == "y":
        print("\nYou continue down the smaller path.")
        floor2stairs()
    else:
        print("\nCome on man, just go.")
        floor2stairs()


def floor2stairs():
    print("\nYou've done it. The final set of stairs stands in front of you. You can finally finish your...")
    print("Taxes Taxes Taxes Taxes Taxes Taxes Taxes Taxes Taxes Taxes Taxes Taxes Taxes Taxes Taxes TaxesTaxesTaxesTaxesTaxesTaxesTaxesTaxesTaxesTaxesTaxesTaxesTaxesTaxes.")
    print("\n1. Go up the stairs. GO UP THE STAIRS, THERE'S NO OTHER WAY NOW.")

    choice = input("\nGO GO GO GO GO GO GO GO GOG GG GOG OG GOG GOG ")
    if choice == "1":
        print("\nYou walk up the stairs.")
        bossfight_enter()
    else:
        print("\nYou walk up the stairs. There's no other choice.")
        bossfight_enter()


def bossfight_enter():
    print("\nThis is it. I can't guide you anymore. The doors that stand before you are the only way forward.")
    print("I truly hope you finish your taxes.")
    bossfight_phase1()


def bossfight_phase1():
    global player_hp
    global boss_hp
    print("\nI look around the new room. It looks like where the boss used to work. The walls are lined with portraits of old bosses, and there's a desk with a boss plaque.")
    print("Sitting in the chair is a man. His body is limp, but he looks normal otherwise. Better than normal, even. He looks unharmed.")
    print("\nVines start to race toward him, dashing by my feet. They wrap around him, creating a huge fleshy body.")
    print("His boss plaque is held to his chest by the vines, a grotesque face emerging.")
    print("\nMy ears bleed as he screams out into the room. This is it. The final battle.")
    print("\n" + "+" * 30)
    print("\nFinal Boss: Phase 1")
    print("\n" + "+" * 30)

    while player_hp > 0 and boss_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"Boss Health: {boss_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            boss_hp -= player_attack_damage
            print("\nI blast the boss! It screams.")

        elif choice == "2":
            print("\nI brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nI pet my cat, and it heals {healed} health.")

        else:
            print("\nThat's not an option.")
            continue

        if boss_hp <= 400:
            bossfight_phase2()
            break

        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("I parry the attack! The boss takes 50 damage.")
                    boss_hp -= 50
                else:
                    print("The boss attacks me, but I blocked it!")

            else:
                player_hp -= boss_attack
                print(f"The boss hits me. It feels like {boss_attack} damage!")

        else:
            print("The boss's attack misses.")

        if player_hp <= 0:
            print("\nThe boss grabs my head. I feel it pull. I feel tendons snap. It fades to black.")
            died()


def bossfight_phase2():
    global player_hp
    global boss_hp
    boss_shield = 50
    print("\nThe boss screams out. It seems to be hurt, but still alright.")
    print("A shield of meat forms on the floor, and the boss picks it up.")
    print("\n" + "+" * 30)
    print("\nFinal Boss: Phase 2, The Shield")
    print("\n" + "+" * 30)

    while player_hp > 0 and boss_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"Boss Health: {boss_hp}")
        if boss_shield > 0:
            print(f"Shield: {boss_shield}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            if boss_shield > 0:
                boss_shield -= player_attack_damage
                if boss_shield <= 0:
                    print("\nI blast the shield. It shatters!")
                else:
                    print("\nI blast the shield. It cracks, but it holds.")
            else:
                boss_hp -= player_attack_damage
                print("\nI blast the boss! It screams.")

        elif choice == "2":
            print("\nI brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nI pet my cat, and it heals {healed} health.")

        else:
            print("\nThat's not an option.")
            continue

        if boss_hp <= 200:
            bossfight_phase3()
            break

        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("I parry the attack! The boss takes 50 damage.")
                    boss_hp -= 50
                else:
                    print("The boss attacks me, but I blocked it!")

            else:
                player_hp -= boss_attack
                print(f"The boss hits me. It feels like {boss_attack} damage!")

        else:
            print("The boss's attack misses.")

        if player_hp <= 0:
            print("\nThe boss grabs my head. I feel it pull. I feel tendons snap. It fades to black.")
            died()


def bossfight_phase3():
    global player_hp
    global boss_hp
    print("\nThe shield lies broken on the floor, already rotting. The boss is hurt now. Hurt bad.")
    print("I have to finish this, but the boss is in a rage now.")
    print("\n" + "+" * 30)
    print("\nFinal Boss: Phase 3, Rage")
    print("\n" + "+" * 30)

    while player_hp > 0 and boss_hp > 0:
        print("\n" + "-" * 30)
        print(f"Your Health: {player_hp}/{max_player_hp}")
        print(f"Boss Health: {boss_hp}")
        print("What do you do?")
        print("1. Attack.")
        print("2. Block")
        print("3. Use your cat as a blessed spirit (Heal)")

        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            boss_hp -= player_attack_damage
            print("\nI blast the boss! It screams.")

        elif choice == "2":
            print("\nI brace for an attack.")

        elif choice == "3":
            old_health = player_hp
            player_hp = min(player_hp + cat_heal_amount, max_player_hp)
            healed = player_hp - old_health
            print(f"\nI pet my cat, and it heals {healed} health.")

        else:
            print("\nThat's not an option.")
            continue

        if boss_hp <= 0:
            bossfight_end()
            break

        # First attack
        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("I parry the attack! The boss takes 50 damage.")
                    boss_hp -= 50
                    if boss_hp <= 0:
                        bossfight_end()
                        break
                else:
                    print("The boss attacks me, but I blocked it!")

            else:
                player_hp -= boss_attack
                print(f"The boss hits me. It feels like {boss_attack} damage!")

        else:
            print("The boss's attack misses.")

        if player_hp <= 0:
            print("\nThe boss grabs my head. I feel it pull. I feel tendons snap. It fades to black.")
            died()

        # Second (weaker) attack
        if random.random() < 0.4:
            if choice == "2":
                if parry == True and random.random() < 0.25:
                    print("I parry the second attack! The boss takes 50 damage.")
                    boss_hp -= 50
                    if boss_hp <= 0:
                        bossfight_end()
                        break
                else:
                    print("The boss's second attack comes in, but I blocked it!")

            else:
                player_hp -= boss_attack_desperate
                print(f"The boss's second attack hits me. It feels like {boss_attack_desperate} damage!")

        else:
            print("The boss's second attack misses.")

        if player_hp <= 0:
            print("\nThe boss grabs my head. I feel it pull. I feel tendons snap. It fades to black.")
            died()


def bossfight_end():
    print("\nI walk over to the crumpling boss, its head peeling back.")
    print("He's on his knees by the time his true face is revealed.")
    print("His face... it's that of a normal person. This can't be right.")
    print("\nHe cackles at my confused face. \"Kill me! DO IT NOW! KILL ME! I DARE YOU!\"")
    print("\n\"You wanna know why your friend left you before this fight? BECAUSE HE IS ME. I led you here. There were never any taxes. The IRS fell half a year ago.\"")
    print("\n\"DO IT. FINISH THIS.\"")
    print("\n1. Kill him.")
    print("2. Show mercy.")

    choice = input("\nWhat do I do? ").strip()
    if choice == "1":
        killhim()
    elif choice == "2":
        sparehim()


def killhim():
    print("\n" + "+" * 30)
    print("\nEnding: You, the IRS.")
    print("\n" + "+" * 30)
    print("\nHe raises his shotgun, the biggest mistake of his life.")
    print("The trigger is pulled. The man is dead.")
    print("\nThe room quivers with the loss of its leader. The vines search for a new host, and they find the man.")
    print("The man's body goes limp, his mind now spread. Still himself, and nothing but a narrator.")
    print("\nThis is you. You are him. You are the IRS. Find a replacement.")

    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        main()
    else:
        print("\nThanks for playing!")
        sys.exit(0)


def sparehim():
    print("\n" + "+" * 30)
    print("\nEnding: The IRS Destroyer.")
    print("\n" + "+" * 30)
    print("\nI put the shotgun down. The man screams, \"NO, NO, WHAT ARE YOU DOING?\"")
    print("I walk out the big doors.")
    print("\nThe man screams more: \"YOU CAN'T LEAVE! NO, NOT AFTER EVERYTHING I'VE DONE! NOOOoo\"")
    print("\nI see my truck. The best way down is to jump onto its roof. It's time to leave.")
    print("\nThe street lights fly by. The world may be doomed, but no IRS means no taxes.")
    print("You lived.")

    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        main()
    else:
        print("\nThanks for playing!")
        sys.exit(0)


if __name__ == "__main__":
    main()
