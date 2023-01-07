"""Genshin Impact is an action RPG available for PlayStation, PC, and Mobile devices. It has an in-depth combat system that requires multiple calculations for a variety of stats.
This program seeks to take a character and their stats, and be able to plan out damage numbers for them depending on the multiple factors that come into play with Genshin Impact."""

#First, we will need to describe the character class, as well as the stats each character will use:
class Character:
    level = 1
    base_attack = 39
    base_defense = 162
    talent_level_attack = 1
    talent_level_skill = 1
    talent_level_ultimate = 1
    dmg_bonus = 1.0
    crit_rate = 0.05
    crit_damage = 0.5
    elemental_mastery = 0
    artifact_attack = 0
    total_attack = base_attack + artifact_attack
    ability_stat = total_attack
    

#Let's describe the damage calculation
def dmg(base, dmg_bonus, dmg_reduction, defense, resistance, amp, special=1, flat=1):
    damage = ((base * special) + flat) * (1 + dmg_bonus - dmg_reduction) * defense * resistance * amp
    return damage

#Let's define base damage
base = ability_mod * ability_stat #Ability stat will vary by character. Most characters use Attack, while others use Defense, and even HP

#Let's define 
[1, 2, 3] * 3
