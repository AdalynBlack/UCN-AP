from random import randint, choice


def get_deathlink_msg(player: str, scarer: str) :
    special_message = {
        "Freddy": [
            f"{player} honked Freddy's nose.",
            f"{player} wasn't ready for Freddy.",
            f"{player} broke rule 4."
        ],
        "Chica": [
            f"{player} forgot that Chica hates repetitive music.",
            f"Chica wasn't a fan of {player}'s playlist.",
            f"{player} skipped Chica's favorite song."
        ],
        "Foxy": [
            f"Foxy showed everyone that {player} was the nightguard.",
            f"{player} couldn't protect their booty (treasure) from Foxy",
            f"{player} had bad Foxy RNG... or maybe it was just a skill issue."
        ],
        "Toy Freddy": [
            f"{player} has a bigger skill issue than Toy Freddy.",
            f"{player} couldn't help Toy Freddy beat a vacuum cleaner.",
            f"{player} died to Toy Freddy. They should play something simpler, like Minesweeper!"
        ],
        "Toy Bonnie": [
            f"{player} thought that Sans was Ness.",
            f"{player} forgot they had a spare Freddy head to trick {scarer}.",
            f"{player} called Toy Bonnie a chipmunk."
        ],
        "Toy Chica": [
            f"{player} forgot they had a spare Freddy head to trick {scarer}.",
            f"{player} wanted to get a weird death link message.",
            f"{player} was killed by William Afton."
        ],
        "Mangle": [
            f"{player} was mangled by Mangle.",
            f"{player} was taken apart and put back together by Mangle.",
            f"Mangle shuffled {player}'s limbs around like they were a Rubik's cube."
        ],
        "Withered Chica": [
            f"{player} didn't pay enough attention to the vent monitor.",
            f"{player} tried to use a forward vent that doesn't use power.",
            f"{player} died to a character that got stuck in a vent."
        ],
        "Withered Bonnie": [
            f"{player} lost the 50% chance to Unscrew 2.",
            f"There's a 1/10,000 chance that wasn't {player}'s fault.",
            f"{player} is facing the consequences of this failure."
        ],
        "Golden Freddy": [
            f"{player} figured out Golden Freddy's identity.",
            f"{player} had the reaction time of a snail.",
            f"{player} got a heart attack from a jpeg."
        ],
        "Marionette": [
            f"{player}'s strings were cut by the Marionette.",
            f"{player} turned off the music and died from it.",
            f"Their life seconds numbering, Tick, tock, tick, tock, It stopped short, Never to go again, When {player} died."
        ],
        "Springtrap": [
            f"{player} went to Vegas with the wrong Dave.",
            f"{player} will not come back.",
            f"{player} got springlocked."
        ],
        "Nightmare Freddy": [
            f"{player} got hit by Freddle Fury.",
            f"{player} had a bad dream, but they couldn't wake up.",
            f"{player} must have liked the noise of Freddles."
        ],
        "Nightmare Bonnie": [
            f"{player} Got turned into a marketable plushie with the help of {scarer}.",
            f"{player} didn't give Nightmare Bonnie the WiFi password.",
            f"{player} died to a hallucination."
        ],
        "Nightmare Fredbear": [
            f"{player} got bite of 87'd by Nightmare Fredbear.",
            f"{player} was taken apart and put back together by Nightmare Fredbear.",
            f"Ferdinand von Bernard would never have done that to {player}!"
        ],
        "Nightmare": [
            f"{player} forgot the cool jpeg jumpscare wasn't in this game.",
            f"{player} Broke Their Mind.",
            f"{player} couldn't see the very obvious red eyes in the right door before opening cams."
        ],
        "Jack'O Chica": [
            f"Jack'O Chica was too hot to handle for {player}.",
            f"Jack'O Chica helped {player} cool of a bit.",
            f"{player} was scorched, but at least they smell like roasted pumpkins now."
        ],
        "Nightmare Mangle": [
            f"{player} Got turned into a marketable plushie with the help of {scarer}.",
            f"{player} got incorrectly reassembled by Nightmare Mangle.",
            f"The foxy plush was too expensive for {player}."
        ],
        "Nightmarionne": [
            f"{player} just HAD to leaver their cursor there...",
            f"{player}, is dragged to a nightmare they won't wake from.",
            f"{player} went AFK at the worst possible time."
        ],
        "Nightmare BB": [
            f"{player} is helping Nightmare BB count his teeth.",
            f"{player} had a little too much fun with Nightmare BB.",
            f"{player} couldn't flash Nightmare BB in time."
        ],
        "Circus Baby": [
            f"{player} Got turned into a marketable plushie with the help of {scarer}.",
            f"{player} has Joined Them For A Bite.",
            f"{player} wanted some ice cream."
        ],
        "Ballora": [
            f"{player} found out why it's not the best idea to play FNaF games without stereo headphones.",
            f"{player} couldn't handle Ballora's dance lessons.",
            f"{player} has worse hearing than a purple corpse."
        ],
        "Funtime Foxy": [
            f"{player}'s attention span was too short to watch Funtime Foxy's showtime.",
            f"{player} took their final bow.",
            f"{player} won't beat their multiworld without the death coin at this rate."
        ],
        "Ennard": [
            f"{player} is slowly turning purple.",
            f"{player} got a new Friend Inside Them.",
            f"{player} shouldn't have gone to the private room."
        ],
        "Happy Frog": [
            f"{player} underestimated Happy Frog.",
            f"{player} died to Happy Frog's ninja skills.",
            f"{player} couldn't place an audio lure in a good enough spot."
        ],
        "Mr. Hippo": [
            f"{player} is willingly, or unwillingly listening to a never ending story.",
            f"{player} manually sent themselves a Monologue Trap.",
            f"{player}, you have met a terrible, terrible demise. But, uh, y'know I-I don't feel too bad about it all. After all,... Read more"
        ],
        "Pigpatch": [
            f"{player} got buried by Pigpatch.",
            f"{player}'s death was quite pathetic.",
            f"{player} just wanted to hear an epic banjo solo."
        ],
        "Nedd Bear": [
            f"{player} died to an obscure secondary character.",
            f"{player} died to bootleg Fredbear.",
            f"Nedd bear left a big mark on {player}."
        ],
        "Orville Elephant": [
            f"Orville hopes you liked his Archipelago act! If you didn't blame {player}.",
            f"{player} witnessed a deadly magic trick.",
            f"{player} tried to address the elephant in the ducts."
        ],
        "Rockstar Freddy": [
            f"{player} tried to trick Rockstar Freddy.",
            f"{player} did not deposit 5 coins.",
            f"{player}'s life was no longer profitable for Fazbear.co"
        ],
        "Rockstar Bonnie": [
            f"{player} perfectly timed a ventilation reset at a 13 second interval",
            f"{player} is terrible at I Spy.",
            f"{player} couldn't find a guitar."
        ],
        "Rockstar Chica": [
            f"{player} slipped up.",
            f"{player} couldn't figure out how to double click on a sign.",
            f"{player} couldn't trick this old bird."
        ],
        "Rockstar Foxy": [
            f"{player} bet their entire life (not just savings), and lost it all.",
            f"{player} couldn't stop playing with fire.",
            f"{player} touched Rockstar Foxy's parrot and paid the price."
        ],
        "Music Man": [
            f"{player} was louder than a FNaF 4 jumpscare.",
            f"{player} failed the Vibe Check.",
            f"{player} disturbed the Music Man's nest."
        ],
        "Molten Freddy": [
            f"{player} got their connection terminated by {scarer}.",
            f"{player} wasn't ready for Molten Freddy's surprise.",
            f"{player} wasn't ready for round 2."
        ],
        "Scrap Baby": [
            f"{player} got their connection terminated by {scarer}.",
            f"Scrap Baby stabbed {player} with scissors 61 times.",
            f"{player} is just a skater hater."
        ],
        "Afton": [
            f"{player} got their connection terminated by {scarer}.",
            f"{player} died from peanut allergies.",
            f"Afton came back for {player}."
        ],
        "Lefty": [
            f"{player} got their connection terminated by {scarer}.",
            f"{player} was silenced by Lefty",
            f"{player} was Lured, Encapsulated, Fused, Transported and Exterminated."
        ],
        "Plushtrap": [
            f"{player} had a little too much fun with Plushtrap.",
            f"{player} was chased to death.",
            f"{player} couldn't watch a camera for 3 seconds."
        ],
        "Bonnet": [
            f"{player} failed to boop Bonnet's nose.",
            f"{player} can't point and click on a nose.",
            f"{player} died to a hand puppet."
        ],
        "Nightmare Chica": [
            f"{player} didn't press '4' to save themselves.",
            f"{player} forgot the heater doesn't work on Nightmare Chica here",
            f"{player} was sure the first night is never really that bad in any of the games."
        ]
        # ,
        # "Fredbear": [
        #     f"{player} did this to themselves... embarrassing really...",
        #     f"{player} went for a check that didn't exist",
        #     f"{player} went for a win condition they didn't pick"
        # ]
    }

    if randint(1, 3) != 1:
        return choice(special_message[scarer])

    regular_msgs = [
        f"{player} got jumpscared by {scarer}.",
        f"{player} shouldn't have picked {scarer}.",
        f"{player} figured out the crying child's name but {scarer} got to them before they could tell anyone."
    ]
    return choice(regular_msgs)