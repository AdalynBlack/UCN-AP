from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, MultiWorld
from BaseClasses import ItemClassification as ItemC

class UcnItem(Item):
    game = "Ultimate Custom Night"


class UcnItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemC = ItemC
    game_id: str = ""
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


item_data_table: Dict[str, UcnItemData] = {
        # Characters
        "Freddy Fazbear": UcnItemData(502100, ItemC.progression_skip_balancing, "char1unlocked"),
        "Bonnie": UcnItemData(502101, ItemC.progression_skip_balancing, "char2unlocked"),
        "Chica": UcnItemData(502102, ItemC.progression_skip_balancing, "char3unlocked"),
        "Foxy": UcnItemData(502103, ItemC.progression_skip_balancing, "char4unlocked"),
        "Toy Freddy": UcnItemData(502104, ItemC.progression_skip_balancing, "char5unlocked"),
        "Toy Bonnie": UcnItemData(502105, ItemC.progression_skip_balancing, "char6unlocked"),
        "Toy Chica": UcnItemData(502106, ItemC.progression_skip_balancing, "char7unlocked"),
        "Mangle": UcnItemData(502107, ItemC.progression_skip_balancing, "char8unlocked"),
        "BB": UcnItemData(502108, ItemC.progression_skip_balancing, "char9unlocked"),
        "Withered Chica": UcnItemData(502109, ItemC.progression_skip_balancing, "char31unlocked"),
        "Withered Bonnie": UcnItemData(502110, ItemC.progression_skip_balancing, "char17unlocked"),
        "JJ": UcnItemData(502111, ItemC.progression_skip_balancing, "char10unlocked"),
        "Marionette": UcnItemData(502112, ItemC.progression_skip_balancing, "char38unlocked"),
        "Golden Freddy": UcnItemData(502113, ItemC.progression_skip_balancing, "char37unlocked"),
        "Springtrap": UcnItemData(502114, ItemC.progression_skip_balancing, "char11unlocked"),
        "Phantom Freddy": UcnItemData(502115, ItemC.progression_skip_balancing, "char44unlocked"),
        "Phantom Mangle": UcnItemData(502116, ItemC.progression_skip_balancing, "char41unlocked"),
        "Phantom BB": UcnItemData(502117, ItemC.progression_skip_balancing, "char46unlocked"),
        "Nightmare Freddy": UcnItemData(502118, ItemC.progression_skip_balancing, "char12unlocked"),
        "Nightmare Bonnie": UcnItemData(502119, ItemC.progression_skip_balancing, "char47unlocked"),
        "Nightmare Fredbear": UcnItemData(502120, ItemC.progression_skip_balancing, "char15unlocked"),
        "Nightmare": UcnItemData(502121, ItemC.progression_skip_balancing, "char16unlocked"),
        "Jack-O-Chica": UcnItemData(502122, ItemC.progression_skip_balancing, "char14unlocked"),
        "Nightmare Mangle": UcnItemData(502123, ItemC.progression_skip_balancing, "char13unlocked"),
        "Nightmarionne": UcnItemData(502124, ItemC.progression_skip_balancing, "char26unlocked"),
        "Nightmare BB": UcnItemData(502125, ItemC.progression_skip_balancing, "char42unlocked"),
        "Old Man Consequences": UcnItemData(502126, ItemC.progression_skip_balancing, "char50unlocked"),
        "Circus Baby": UcnItemData(502127, ItemC.progression_skip_balancing, "char18unlocked"),
        "Ballora": UcnItemData(502128, ItemC.progression_skip_balancing, "char19unlocked"),
        "Funtime Foxy": UcnItemData(502129, ItemC.progression_skip_balancing, "char49unlocked"),
        "Ennard": UcnItemData(502130, ItemC.progression_skip_balancing, "char20unlocked"),
        "Trash and the Gang": UcnItemData(502131, ItemC.progression_skip_balancing, "char25unlocked"),
        "Helpy": UcnItemData(502132, ItemC.progression_skip_balancing, "char43unlocked"),
        "Happy Frog": UcnItemData(502133, ItemC.progression_skip_balancing, "char28unlocked"),
        "Mr. Hippo": UcnItemData(502134, ItemC.progression_skip_balancing, "char29unlocked"),
        "Pigpatch": UcnItemData(502135, ItemC.progression_skip_balancing, "char30unlocked"),
        "Orville Elephant": UcnItemData(502136, ItemC.progression_skip_balancing, "char45unlocked"),
        "Nedd Bear": UcnItemData(502137, ItemC.progression_skip_balancing, "char48unlocked"),
        "Rockstar Freddy": UcnItemData(502138, ItemC.progression_skip_balancing, "char21unlocked"),
        "Rockstar Bonnie": UcnItemData(502139, ItemC.progression_skip_balancing, "char22unlocked"),
        "Rockstar Chica": UcnItemData(502140, ItemC.progression_skip_balancing, "char23unlocked"),
        "Rockstar Foxy": UcnItemData(502141, ItemC.progression_skip_balancing, "char24unlocked"),
        "Music Man": UcnItemData(502142, ItemC.progression_skip_balancing, "char34unlocked"),
        "El Chip": UcnItemData(502143, ItemC.progression_skip_balancing, "char35unlocked"),
        "Molten Freddy": UcnItemData(502144, ItemC.progression_skip_balancing, "char27unlocked"),
        "Funtime Chica": UcnItemData(502145, ItemC.progression_skip_balancing, "char36unlocked"),
        "Scrap Baby": UcnItemData(502146, ItemC.progression_skip_balancing, "char33unlocked"),
        "Afton": UcnItemData(502147, ItemC.progression_skip_balancing, "char32unlocked"),
        "Lefty": UcnItemData(502148, ItemC.progression_skip_balancing, "char39unlocked"),
        "Phone Guy": UcnItemData(502149, ItemC.progression_skip_balancing, "char40unlocked"),

        # Abilities
        "Left Door": UcnItemData(502150, ItemC.progression_skip_balancing, "leftdoorunlocked"),
        "Right Door": UcnItemData(502151, ItemC.progression_skip_balancing, "rightdoorunlocked"),
        "Music Box": UcnItemData(502152, ItemC.progression_skip_balancing, "musicboxunlocked"),
        "Change Music": UcnItemData(502153, ItemC.progression_skip_balancing, "changemusicunlocked"),
        "Global Music Box": UcnItemData(502154, ItemC.progression_skip_balancing, "globalmusicunlocked"),
        "Mask": UcnItemData(502155, ItemC.progression_skip_balancing, "maskunlocked"),
        "Side Vent": UcnItemData(502156, ItemC.progression_skip_balancing, "rightventunlocked"),
        "Forward Vent": UcnItemData(502157, ItemC.progression_skip_balancing, "forwardventunlocked"),
        "Snare": UcnItemData(502158, ItemC.progression_skip_balancing, "snareunlocked"),
        "Flashlight": UcnItemData(502159, ItemC.progression_skip_balancing, "flashlightunlocked"),
        "Bonnie Plush": UcnItemData(502160, ItemC.progression_skip_balancing, "bonplushunlocked"),
        "Nightmare Mangle Plush": UcnItemData(502161, ItemC.progression_skip_balancing, "mplushunlocked"),
        "Circus Baby Plush": UcnItemData(502162, ItemC.progression_skip_balancing, "babyplushunlocked"),
        "Deathcoin": UcnItemData(502163, ItemC.progression_skip_balancing, "dcoinunlocked"),
        "Audio Lure": UcnItemData(502164, ItemC.progression_skip_balancing, "lureunlocked"),
        "Heater": UcnItemData(502165, ItemC.progression_skip_balancing, "heaterunlocked"),
        "Shock": UcnItemData(502166, ItemC.progression_skip_balancing, "shockunlocked"),
        "Silent Ventilation": UcnItemData(502167, ItemC.useful, "sventunlocked"),
        "Power AC": UcnItemData(502168, ItemC.progression_skip_balancing, "acunlocked"),
        "Power Generator": UcnItemData(502169, ItemC.progression_skip_balancing, "generatorunlocked"),

        # Challenges
        "Bears Attack 1" : UcnItemData(502170, ItemC.progression_skip_balancing, "challenge1unlocked"),
        "Bears Attack 2": UcnItemData(502171, ItemC.progression_skip_balancing, "challenge2unlocked"),
        "Bears Attack 3" : UcnItemData(502172, ItemC.progression_skip_balancing, "challenge3unlocked"),
        "Pay Attention 1" : UcnItemData(502173, ItemC.progression_skip_balancing, "challenge4unlocked"),
        "Pay Attention 2" : UcnItemData(502174, ItemC.progression_skip_balancing, "challenge5unlocked"),
        "Ladies Night 1" : UcnItemData(502175, ItemC.progression_skip_balancing, "challenge6unlocked"),
        "Ladies Night 2" : UcnItemData(502176, ItemC.progression_skip_balancing, "challenge7unlocked"),
        "Ladies Night 3" : UcnItemData(502177, ItemC.progression_skip_balancing, "challenge8unlocked"),
        "Creepy Crawlies 1" : UcnItemData(502178, ItemC.progression_skip_balancing, "challenge9unlocked"),
        "Creepy Crawlies 2" : UcnItemData(502179, ItemC.progression_skip_balancing, "challenge10unlocked"),
        "Nightmares Attack" : UcnItemData(502180, ItemC.progression_skip_balancing, "challenge11unlocked"),
        "Springtrapped" : UcnItemData(502181, ItemC.progression_skip_balancing, "challenge12unlocked"),
        "Old Friends" : UcnItemData(502182, ItemC.progression_skip_balancing, "challenge13unlocked"),
        "Chaos 1" : UcnItemData(502183, ItemC.progression_skip_balancing, "challenge14unlocked"),
        "Chaos 2" : UcnItemData(502184, ItemC.progression_skip_balancing, "challenge15unlocked"),
        "Chaos 3" : UcnItemData(502185, ItemC.progression_skip_balancing, "challenge16unlocked"),

        # TODO Challenge Bundles
        # "Challenge Bundle: Bears Attack" : UcnItemData(502186, type=IC.progression_skip_balancing, game_id="challengebundle1"),
        # "Challenge Bundle: Pay Attention" : UcnItemData(50217, type=IC.progression_skip_balancing, game_id="challengebundle2"),
        # "Challenge Bundle: Ladies Night" : UcnItemData(502188, type=IC.progression_skip_balancing, game_id="challengebundle3"),
        # "Challenge Bundle: Creepy Crawlies" : UcnItemData(502189, type=IC.progression_skip_balancing, game_id="challengebundle4"),
        # "Challenge Bundle: Uniques" : UcnItemData(502190, type=IC.progression_skip_balancing, game_id="challengebundle5"),
        # "Challenge Bundle: Chaos" : UcnItemData(502191, type=IC.progression_skip_balancing, game_id="challengebundle6"),

        # Filler Items
        "Fnaf Sister Location Office": UcnItemData(502186, ItemC.filler, "office1unlocked"),
        "Fnaf 3 Office": UcnItemData(502187, ItemC.filler, "office2unlocked"),
        "Fnaf 4 Office": UcnItemData(502188, ItemC.filler, "office3unlocked"),
        "Frigid Power-up": UcnItemData(502189, ItemC.filler, "i1"),
        "3 Coins Power-up": UcnItemData(502190, ItemC.filler, "i2"),
        "Battery Power-up": UcnItemData(502191, ItemC.filler, "i3"),
        "DeeDee Repel": UcnItemData(502198, ItemC.filler, "i4"),

        # Traps
        "DeeDee Trap": UcnItemData(502192, ItemC.trap, "ddtrap"),
        "XOR Trap": UcnItemData(502193, ItemC.trap, "xortrap"),
        "Fake Audio Queue Trap": UcnItemData(502194, ItemC.trap, "audiotrap"),
        "Bankruptcy Trap": UcnItemData(502195, ItemC.trap, "losecointrap"),
        "Power Drain Trap": UcnItemData(502196, ItemC.trap, "powerdowntrap"),
        "Mute Audio Trap": UcnItemData(502197, ItemC.trap, "mutesoundtrap"),
        "Monologue Trap": UcnItemData(502199, ItemC.trap, "hippotrap"),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
mandatory_items = [name for name, data in item_data_table.items() if "unlock" in data.game_id and "challenge" not in data.game_id]
challenge_items = [name for name, data in item_data_table.items() if "challenge" in data.game_id]
powerup_items = [name for name in item_data_table.keys() if "Power-up" in name]
severe_traps = ["XOR Trap", "Mute Audio Trap", "Monologue Trap"]
trap_items = [name for name in item_data_table.keys() if "Trap" in name and name not in severe_traps]
trap_ids = [data.game_id for data in item_data_table.values() if "trap" in data.game_id]