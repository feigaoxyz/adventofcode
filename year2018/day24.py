import sys
import re
from copy import deepcopy
from enum import Enum
import operator as op

from common import load_input

IMMUNE, INFECTION = "immune", "infection"


class Group:
    def __init__(
        self,
        number_units,
        hit_points,
        weak_to,
        immune_to,
        attack_damage,
        attack_type,
        initiative,
        army,
        uid,
    ):
        self.number_units = number_units
        self.hit_points = hit_points
        self.weak_to = [] if weak_to is None else weak_to
        self.immune_to = [] if immune_to is None else immune_to
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative
        self.army = army
        self.uid = uid

        self.attack_target = None
        self.been_selected = False

    @property
    def effective_power(self):
        return self.number_units * self.attack_damage

    @property
    def select_order_key(self):
        return (-self.effective_power, -self.initiative)

    def defend_order_key(self, attacker):
        return (
            -real_attack_damage(attacker, self),
            -self.effective_power,
            -self.initiative,
        )

    def attack_order_key(self):
        return -self.initiative

    def attacked_by(self, attacker):
        damage = real_attack_damage(attacker, self)
        self.number_units = max(0, self.number_units - damage // self.hit_points)

    def __str__(self):
        return f"({self.army} {self.uid} with {self.number_units} units weak {self.weak_to} immune {self.immune_to} attack {self.attack_type})"

    def __repr__(self):
        return str(self)


def real_attack_damage(attacker, defender):
    damage = attacker.effective_power
    if attacker.attack_type in defender.immune_to:
        damage = 0
    elif attacker.attack_type in defender.weak_to:
        damage = damage * 2
    return damage


class Fight:
    def __init__(self, groups):
        self.groups = groups[::]
        self._groups = groups[::]

    def target_selection_phase(self):
        self.groups.sort(key=op.attrgetter("select_order_key"))
        for attacker in self.groups:
            opponents = [
                d
                for d in self.groups
                if d.army != attacker.army and d.been_selected is False
            ]
            opponents.sort(key=lambda d: d.defend_order_key(attacker))
            if opponents and real_attack_damage(attacker, opponents[0]) > 0:
                attacker.attack_target = opponents[0].uid
                opponents[0].been_selected = True

    def attacking_phase(self):
        self.round_units_lost = 0
        self.groups.sort(key=op.attrgetter("initiative"), reverse=True)
        for a in self.groups:
            tid = a.attack_target
            for d in self.groups:
                if d.uid == tid:
                    units = d.number_units
                    d.attacked_by(a)
                    self.round_units_lost += units - d.number_units

    def round_end(self):
        groups = []
        for g in self.groups:
            if g.effective_power:
                g.attack_target = None
                g.been_selected = False
                groups.append(g)
        self.groups = groups
        all_immune = all(g.army == IMMUNE for g in self.groups)
        all_infection = all(g.army == INFECTION for g in self.groups)
        return (
            len(self.groups) <= 1
            or all_immune
            or all_infection
            or (self.round_units_lost == 0)
        )

    def reset(self):
        self.groups = [deepcopy(g) for g in self._groups]

    def simulate(self, boost=0):
        self.reset()
        self.boost(immune=boost)
        while True:
            self.target_selection_phase()
            self.attacking_phase()
            if self.round_end():
                break
        return all([g.army == IMMUNE for g in self.groups])

    def boost(self, immune=0, infection=0):
        for g in self.groups:
            if g.army == IMMUNE:
                g.attack_damage += immune
            elif g.army == INFECTION:
                g.attack_damage += infection

    def __str__(self):
        return str(self.groups)


def preprocess(raw):
    is_immunse = True
    groups = []
    for idx, line in enumerate(raw.splitlines()):
        if not line:
            pass
        elif line.startswith("Infection"):
            is_immunse = False
        elif line.startswith("Immune"):
            is_immunse = True
        else:
            units, hp, damage, init = map(int, re.findall(r"\d+", line))
            weak = re.findall("weak to ([\w, ]+)", line)
            weak_to = weak[0].split(", ") if weak else None
            immune = re.findall("immune to ([\w, ]+)", line)
            immune_to = immune[0].split(", ") if immune else None
            attack_type = re.findall(r"(\w+) damage", line)[0]
            groups.append(
                Group(
                    units,
                    hp,
                    weak_to,
                    immune_to,
                    damage,
                    attack_type,
                    init,
                    IMMUNE if is_immunse else INFECTION,
                    uid=idx,
                )
            )
    return Fight(groups)


def fn_p1(data):
    data.simulate()
    return sum(g.number_units for g in data.groups)


def fn_p2(data):
    low = 0
    high = 2000
    while low < high:
        mid = (low + high) // 2
        result = data.simulate(mid)
        if result:
            high = mid
        else:
            low = mid + 1
    data.simulate(low)
    print(low)
    return sum(g.number_units for g in data.groups if g.army == IMMUNE)


if __name__ == "__main__":
    raw_data = """Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
    """.strip()
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 26937
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 4893 (boost 28)
