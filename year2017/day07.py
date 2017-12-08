from common import load_input

input_data = load_input(__file__.split('.')[0] + '_in.txt')

PART1_DOC = """Part 1:
Find the root of tree.
"""


def find_bottom(tower: str) -> str:
    """
    disk_name (weight) -> disk_name1, disk_name2 ...
    e.g.
    yvpwz (50)
    vfosh (261) -> aziwd, tubze, dhjrv
    """
    parent = dict()
    for line in tower.splitlines():
        parts = line.split(' -> ')
        if len(parts) == 2:
            base = parts[0].split()[0]
            tops = parts[1].split(', ')
            for top in tops:
                parent[top] = base
    disk = line.split()[0]
    while disk in parent:
        disk = parent[disk]
    return disk


PART2_DOC = """Part 2:
Given that exactly one program is the wrong weight, what would its
weight need to be to balance the entire tower?
"""


def change_weight(tower: str) -> (str, int):
    weight_disk = dict()  # weight of each disk alone
    weight_acc = dict()  # weight of all disk on it including itself

    # parse structure
    children = dict()
    parent = dict()
    for line in tower.splitlines():
        parts = line.split(' -> ')
        base, weight = parts[0].split()
        weight_disk[base] = int(weight[1:-1])
        if len(parts) == 2:
            children[base] = []
            for child in parts[1].split(', '):
                parent[child] = base
                children[base].append(child)
    # print(parent, children)

    # find root
    root = base
    while root in parent:
        root = parent[root]

    # update weights
    for disk, weight in weight_disk.items():
        while True:
            weight_acc[disk] = weight_acc.get(disk, 0) + weight
            if disk in parent:
                disk = parent[disk]
            else:
                break
    # print(weight_acc)

    # find abnormal
    def find_abnormal_children(node: str) -> list:
        children_weights = [weight_acc[child] for child in children[node]]
        if len(set(children_weights)) <= 1:
            # all child same accumulated weight
            # or no child
            return []
        elif len(children_weights) == 2:
            # two children with different accumulated weight
            return children[node]
        else:
            # find the minority
            majority = (children_weights[0]
                        if children_weights[0] == children_weights[1]
                        else children_weights[2])
            for child in children[node]:
                if weight_acc[child] != majority:
                    return [child]

    node = root
    while True:
        # print(node)
        abnormal = find_abnormal_children(node)
        if len(abnormal) == 0:
            # node is wrong
            p = parent[node]
            others = [child for child in children[p] if child != node]
            return node, weight_disk[node] + (weight_acc[others[0]]
                                              - weight_acc[node])
        elif len(abnormal) == 1:
            # one abnormal child
            node = abnormal[0]
        else:
            # two abnormal children
            if find_abnormal_children(abnormal[0]):
                node = abnormal[0]
            else:
                node = abnormal[1]


exampel = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

# fn_p1 = find_bottom
# print("Part 1 Test:", fn_p1(exampel))
# print("Part 1:", fn_p1(input_data))  # mwzaxaj

fn_p2 = change_weight
print("Part 2 example:", fn_p2(exampel))
print("Part 2:", fn_p2(input_data))  # ('vrgxe', 1219)
