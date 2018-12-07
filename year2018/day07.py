import sys

from copy import deepcopy
from common import load_input
from collections import defaultdict


def preprocess(raw):
    forward = defaultdict(set)
    backward = defaultdict(set)
    for line in raw.splitlines():
        parts = line.split()
        up, down = parts[1], parts[7]
        forward[up].add(down)
        backward[down].add(up)
        if down not in forward:
            forward[down] = set()
    return forward, backward


def first_available(forward, backward):
    candidates = [x for x in forward if len(backward[x]) == 0]
    choose = min(candidates)
    for down in forward[choose]:
        backward[down].remove(choose)
    del forward[choose]
    return choose, forward, backward


def fn_p1(data):
    forward, backward = data
    seq = []
    while forward:
        candidates = [x for x in forward if len(backward[x]) == 0]
        choose = min(candidates)
        for down in forward[choose]:
            backward[down].remove(choose)
        del forward[choose]
        seq.append(choose)
    return "".join(seq)


def finish_time(char, start=0):
    work_duration = 60
    return start + (ord(char) - ord("A")) + 1 + work_duration


def fn_p2(data):
    forward, backward = data
    timer = 0
    workers = set()
    seq = []
    pending = dict.fromkeys(forward.keys(), 0)
    while forward:
        if len(workers) < 5:
            candidates = [x for x in forward if len(backward[x]) == 0]
            choose = min(candidates, key=lambda c: pending[c])
            start = max(timer, pending[choose])
            finish = finish_time(choose, start)
            workers.add((finish, choose))
            for down in forward[choose]:
                backward[down].remove(choose)
                pending[down] = max(finish, pending[down])
            del forward[choose]
            del pending[choose]
        else:
            finished = min(workers)
            timer = finished[0]
            seq.append(finished)
            workers.remove(finished)
        print(choose, workers, seq, pending)
    seq += sorted(list(workers))
    return max(seq), "".join(p[1] for p in seq)


if __name__ == "__main__":
    raw_data = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
    """.strip()
    data = preprocess(raw_data)
    # print("Part 1 Example:", fn_p1(deepcopy(data)))
    # print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: AHJDBEMNFQUPVXGCTYLWZKSROI
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 1031 'AHJXDUBENGMQFTPYVCLWZKSROI'
