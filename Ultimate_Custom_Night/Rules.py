from worlds.generic.Rules import set_rule
from BaseClasses import MultiWorld, CollectionState
from .RuleDataTables import animatronic_rule_table, challenge_rule_table
from .Locations import challenge_locations, scare_locations, secret_scares


def has_item(state: CollectionState, item_name: str, player: int):
    return state.has(item_name, player)

def can_beat_animatronic(state: CollectionState, animatronic: str, player: int, challenge: bool):
    if not challenge and not has_item(state, animatronic, player):
        return False

    required_abilities = animatronic_rule_table[animatronic]
    if required_abilities is None:
        return True

    if "Wildcard" in required_abilities:
        if animatronic in ["Jack-O-Chica", "Ballora"]:
            if has_item(state, "Left Door", player) and has_item(state, "Right Door", player):
                return True
        elif "Foxy" in animatronic:
            if has_item(state, "Bonnie", player):
                return True
        return False

    for ability in required_abilities:
        if has_item(state, ability, player):
            return True

    return False

def can_beat_challenge(state: CollectionState, player: int, challenge_id: str):
    if not has_item(state, challenge_id, player):
        return False

    if "Pay Attention" in challenge_id:
        challenge_id = "Pay Attention"
    elif "Bears Attack 3" in challenge_id:
        challenge_id = "Bears Attack 2"

    for animatronic in challenge_rule_table[challenge_id]:
        if not can_beat_animatronic(state, animatronic, player, True):
            return False

    return True

def can_reach_score(state: CollectionState, player: int, score: int, hard_logic: bool, gmb_in_pool):
    reachable_score = 0
    for animatronic in animatronic_rule_table.keys():
        if can_beat_animatronic(state, animatronic, player, False):
                reachable_score += 200

        if reachable_score >= score:
            if score >= 8000 and not hard_logic:
                if not has_item(state, "Deathcoin", player) or \
                   not has_item(state, "Power Generator", player):
                    return False

                if gmb_in_pool and not has_item(state, "Global Music Box", player):
                    return False

            return True

    return False

def has_all_animatronics(state: CollectionState, player: int):
    for animatronic in animatronic_rule_table.keys():
        if not has_item(state, animatronic, player):
            return False
    return True

def create_score_rule(world: MultiWorld, player: int, score: int, hard_logic: bool, gmb: bool):
    set_rule(world.get_location(f"{score}pts", player), lambda state: can_reach_score(state, player, score, hard_logic, gmb))

def create_challenge_rule(world: MultiWorld, player: int, location: str):
    challenge_id = location.split(": ")[1]
    set_rule(world.get_location(location, player), lambda state: can_beat_challenge(state, player, challenge_id))

def create_scare_rule(world: MultiWorld, player: int, location: str):
    animatronic = location.split(": ")[1]
    if animatronic not in secret_scares.keys():
        set_rule(world.get_location(location, player), lambda state: has_item(state, animatronic, player))
    else:
        set_rule(world.get_location(location, player), lambda state: has_all_animatronics(state, player))

    # Sets rules on entrances and advancements that are always applied
def set_scorerules(multiworld: MultiWorld, player: int, max_score: int, hard_logic: bool, gmb: bool):
    for i in range(100, max_score + 100, 100):
        # Lambda func would use the last value to be reachable for each location without helper func. eg: 100pts can_beat(10000)
        create_score_rule(multiworld, player, i, hard_logic, gmb)

def set_challenge_rules(multiworld: MultiWorld, player: int, excluded: list):
    for challenge in challenge_locations:
        if challenge not in excluded:
            create_challenge_rule(multiworld, player, challenge)

def set_scaresanity_rules(multiworld: MultiWorld, player: int, excluded: list):
    for scare in scare_locations:
        if scare not in excluded:
            create_scare_rule(multiworld, player, scare)
