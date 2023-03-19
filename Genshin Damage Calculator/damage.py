import random

def damage_calc(character, enemy):
    base_damage = ((character.base_dmg * character.base_mult) + character.added_base_dmg) * (1 + character.dmg_bonus - enemy.dmg_red) * (enemy.def_mult * enemy.res_mult) * character.amp_mult
    crit_chance = None
    character.crit()

    if crit_chance:
        crit_damage = base_damage * character.crit_multiplier
        return crit_damage
    return base_damage

class Character:
    def __init__(self, hp, attack, defense, elem_mastery, element, level=1, crit_rate=.05, crit_damage=50):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.em = elem_mastery
        self.element = element
        self.level = level
        self.crit_rate = crit_rate
        self.crit_multiplier = 1 + (crit_damage / 100)
    
    def crit(self):
        crit_chance = None

        if random.randint(0, 1) < self.crit_rate:
            crit_chance == True
        else:
            crit_chance == False

class Enemy:
    pass

