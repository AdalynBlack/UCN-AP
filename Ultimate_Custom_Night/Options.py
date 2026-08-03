from dataclasses import dataclass
from Options import PerGameCommonOptions, Range, Toggle, ItemSet, DeathLink

class ScoreRequiredHundreds(Range):
    """The high score required to win divided by 100.
       Locations that require a higher score than the target are removed.

       Note: When setting a score lower than 68, random animatronics will be excluded, including the ones you already excluded.
    """
    display_name = "Required Score (hundreds)"
    default = 68
    range_start = 50
    range_end = 100

class ChallengeSanity(Toggle):
    """
    Add challenges to the location and item pool.

    When excluding animatronics, challenges those animatronics are part of also get excluded.
    """
    display_name = "Challenge Sanity"
    default = 0

class ScareSanity(Toggle):
    """
    Add jumpscares and animatronic debuffs as locations. NOT compatible with death link.
    Animatronic debuffs mean any event that happens when you don't deal with the animatronic. (Example: BB taking your flashlight)
    """
    display_name = "Scare Sanity"
    default = 0

class HardLogic(Toggle):
    """
    Require unintended techniques to ward off animatronics (e.g. camstalling, defeating animatronics with less than you're expected, etc.)
    You may become softlocked - use with caution. Because of this, we recommend you type "Everything" into the YAML option called "non-local"
    """
    display_name = "Hard Logic"
    default = 0

class TrapChance(Range):
    """
    Chance of traps in the item pool.
    Traps only replace filler Power-up items.
    Current traps:
        DeeDee Trap
        Fake Audio Queue Trap
        Bankruptcy Trap
        Power Drain Trap
        XOR Trap (Extreme)
        Mute Audio Trap (Extreme)
        Monologue Trap (Extreme)
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 35

class ExtremeTrapChance(Range):
    """
    Chance of extreme traps in the item pool.
    Extreme traps can only generate, if the filler item was always rolled to be a trap.
    """
    display_name = "Extreme Trap Chance"
    range_start = 0
    range_end = 100
    default = 10

class VanillaDD(Toggle):
    """
    Enable DeeDee to randomly spawn in the night like in vanilla UCN.
    If enabled, DeeDee repels will also be added to the filler item pool.
    """
    display_name = "Vanilla DeeDee"
    default = 0

class ExcludedCharacters(ItemSet):
    """
    Exclude these animatronics from the item pool.
    Incompatible with hard_logic
    NOTE: When excluding animatronics, abilities that are only used by excluded animatronics also get removed.

    (Example: When excluding Chica, it will also remove the Change Music item from the item pool, but won't remove the
    Global Music Box, because Lefty and the Marionette also need it. If you remove them alongside Chica however,
    the GMB will be excluded as well.)
    """
    display_name = "Excluded Animatronics"
    rich_text_doc = True


@dataclass
class UCNOptions(PerGameCommonOptions):
    target_points: ScoreRequiredHundreds
    challenge_sanity: ChallengeSanity
    scare_sanity: ScareSanity
    hard_logic: HardLogic
    trap_chance: TrapChance
    trap_chance_ex: ExtremeTrapChance
    vanilla_dd: VanillaDD
    exclude_animatronics : ExcludedCharacters
    death_link: DeathLink
