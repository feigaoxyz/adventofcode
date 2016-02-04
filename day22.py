#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
from collections import OrderedDict

logging.basicConfig(level=logging.DEBUG)

ATTACK = 'attack'

# magics
MISSILE = 'missle'  # 53 mana. It instantly does 4 damage.
DRAIN = 'drain'  # 73 mana. It instantly does 2 damage and heals you for 2 hit points.

SHIELD = 'shield'  # 113 mana. lasts for 6 turns. While it is active, your armor is increased by 7.
POISON = 'poison'  # 173 mana. lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
RECHARGE = 'recharge'  # 229 mana. lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

spell_costs = OrderedDict()
spell_costs[ATTACK] = 0
spell_costs[MISSILE] = 53
spell_costs[DRAIN] = 73
spell_costs[SHIELD] = 113
spell_costs[POISON] = 173
spell_costs[RECHARGE] = 229


class Player:
    def __init__(self, hp=0, mana=0, attack=0, armor=0, effects=None):
        self.hp = hp
        self.mana = mana
        self.attack = attack
        self.armor = armor
        self.effects = effects if effects else dict()

    def copy(self):
        return Player(self.hp, self.mana, self.attack, self.armor, self.effects.copy())

    def apply_effects(self):
        self.armor = 0
        for e in self.effects:
            if e == SHIELD:
                self.armor = 7
            elif e == RECHARGE:
                self.mana += 101
            elif e == POISON:
                self.hp -= 3
            self.effects[e] -= 1
        self.effects = {k: v for k, v in self.effects.items() if v > 0}

    def cast(self, other, spell):
        if spell in self.effects or spell in other.effects:
            raise KeyError('Spell already exists')

        if spell not in spell_costs:
            raise KeyError('Unknown attack method {}'.format(spell))

        if self.mana >= spell_costs[spell]:
            self.mana -= spell_costs[spell]
        else:
            raise ValueError('Not enough mana')

        if spell == ATTACK:
            other.hp -= max(1, self.attack - other.armor)
        elif spell == MISSILE:
            other.hp -= 4
        elif spell == DRAIN:
            self.hp += 2
            other.hp -= 2
        elif spell == SHIELD:
            self.effects[SHIELD] = 6
        elif spell == POISON:
            other.effects[POISON] = 6
        elif spell == RECHARGE:
            self.effects[RECHARGE] = 5

    def __str__(self):
        return 'HP: {}; Mana: {}; Armor: {}; Effects: {}'.format(
            self.hp, self.mana, self.armor, self.effects.items()
        )

    def __repr__(self):
        return str(self)


def greedy(hero: Player, boss: Player):
    if RECHARGE not in hero.effects:
        return RECHARGE
    if SHIELD not in hero.effects:
        return SHIELD
    if POISON not in boss.effects:
        return POISON
    return MISSILE


def play(hero: Player, boss: Player, strategy: callable):
    turns, hero_round = 0, True
    while boss.hp > 0 and hero.hp > 0:
        turns += 1
        logging.debug('-- Round: {}  {}'.format(turns, 'HERO' if hero_round else 'BOSS'))
        logging.debug('- Hero: {}'.format(hero))
        logging.debug('- Boss: {}'.format(boss))
        hero.apply_effects()
        boss.apply_effects()

        if hero_round:
            spell = strategy(hero, boss)
            hero.cast(boss, spell)
            logging.debug('Hero casts a {}'.format(spell))
        else:
            boss.cast(hero, ATTACK)
            logging.debug('Boss attacks')
        hero_round = not hero_round
    return boss.hp <= 0


def dfs(hero: Player, boss: Player, hard=False):
    stack = [(hero.copy(), boss.copy(), 0, [])]
    min_mana = float('inf')  # 904

    while stack:
        hero, boss, mana, ss = stack.pop()

        if hard:
            hero.hp -= 1
        hero.apply_effects()
        boss.apply_effects()

        if boss.hp <= 0:
            if mana < min_mana:
                min_mana = mana
                logging.debug('Min Mana: {} {} {} {}'.format(min_mana, hero.hp, boss.hp, ss))
            continue
        if hero.hp <= 0: continue
        if mana > min_mana: continue

        for e in spell_costs:
            if e == ATTACK or e in hero.effects or e in boss.effects:
                continue
            elif hero.mana >= spell_costs[e]:
                nh = hero.copy()
                nb = boss.copy()

                nh.cast(nb, e)
                nm = mana + spell_costs[e]

                if nb.hp <= 0:
                    min_mana = min(min_mana, nm)

                nh.apply_effects()
                nb.apply_effects()

                if nb.hp <= 0:
                    min_mana = min(min_mana, nm)

                nb.cast(nh, ATTACK)

                stack.append((nh.copy(), nb.copy(), nm, ss + [e]))
    return min_mana


# boss: Hit Points: 51 Damage: 9
# player # hp: 50 # mana: 500

_hero = Player(hp=50, mana=500)
_boss = Player(hp=51, attack=9)

# print(play(_hero, _boss, greedy))
# print(_hero, _boss)

# dfs(Player(hp=10, mana=250), Player(hp=13, attack=8))

# print('One:', dfs(_hero, _boss))  # 900
print('Two:', dfs(_hero, _boss, hard=True))  # 1216


def test():
    idx = -1
    ss = ['recharge', 'poison', 'shield', 'missle', 'poison', 'missle', 'missle', 'missle']

    def verify(p1, p2):
        nonlocal idx
        idx += 1
        return ss[idx]

    print(play(Player(hp=50, mana=500), Player(hp=51, attack=9), verify),
          sum(spell_costs[s] for s in ss))
