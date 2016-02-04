#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Item:
    def __init__(self, vs):
        self.name = vs[0]
        self.cost, self.damage, self.armor = map(int, vs[1:])


# Weapons:    Cost  Damage  Armor
weapons = """
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""
weapons = [Item(weapon.split()) for weapon in weapons.strip().splitlines()]

# Armor:      Cost  Damage  Armor
armors = """
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""
armors = [Item(armor.split()) for armor in armors.strip().splitlines()]

# Rings:      Cost  Damage  Armor
rings = """
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3
"""
rings = [Item(ring.split()) for ring in rings.strip().splitlines()]


def shopping():
    from itertools import combinations as comb
    for w in list(comb(weapons, 1)):
        for a in list(comb(armors, 0)) + list(comb(armors, 1)):
            for r in list(comb(rings, 0)) + list(comb(rings, 1)) + list(comb(rings, 2)):
                yield list(w) + list(a) + list(r)


from functools import namedtuple

Person = namedtuple('Person', ['hp', 'attack', 'defense'])


def defeat(p1: Person, p2: Person):
    while p1.hp > 0 and p2.hp > 0:
        hit = max(1, p1.attack - p2.defense)
        p2 = p2._replace(hp=p2.hp - hit)
        p1 = p1._replace(hp=p1.hp - max(1, p2.attack - p1.defense))
    return p2.hp <= 0


# Boss
# Hit Points: 103
# Damage: 9
# Armor: 2

def part_one():
    best_cost = float('inf')
    for items in shopping():
        cost = sum(item.cost for item in items)
        boss = Person(103, 9, 2)
        player = Person(100,
                        sum(item.damage for item in items),
                        sum(item.armor for item in items))
        if defeat(player, boss):
            best_cost = min(best_cost, cost)
    return best_cost


print('One:', part_one())

def part_two():
    best_cost = 0
    for items in shopping():
        cost = sum(item.cost for item in items)
        boss = Person(103, 9, 2)
        player = Person(100,
                        sum(item.damage for item in items),
                        sum(item.armor for item in items))
        if not defeat(player, boss):
            best_cost = max(best_cost, cost)
    return best_cost


print('One:', part_two())
