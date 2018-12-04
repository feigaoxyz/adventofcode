import sys
import re

from common import load_input


def preprocess(raw_data):
    lines = raw_data.splitlines()
    lines.sort()
    sleeping = dict()
    for line in lines:
        minute, desc = re.match(r"\[\d+-\d+-\d+ \d+:(\d+)\] (.*)", line).groups()
        if desc.count("#"):
            guard_id = int(re.search(r"\d+", desc).group())
            if guard_id not in sleeping:
                sleeping[guard_id] = [0 for _ in range(60)]
        elif desc.count("asleep"):
            sleep_time = int(minute)
        elif desc.count("wakes"):
            wake_time = int(minute)
            for t in range(sleep_time, wake_time):
                sleeping[guard_id][t] += 1
        else:
            raise ValueError
    return sleeping


def fn_p1(sleeping):
    guard, sleep = max(sleeping.items(), key=lambda p: sum(p[1]))
    return guard * max(enumerate(sleep), key=lambda p: p[1])[0]


def fn_p2(data):
    guard, sleep = max(data.items(), key=lambda p: max(p[1]))
    return guard * max(enumerate(sleep), key=lambda p: p[1])[0]


if __name__ == "__main__":
    example = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up<Paste>
    """.strip()
    data = preprocess(example)
    print("Part 1 example:", fn_p1(data))
    print("Part 2 example:", fn_p2(data))

    raw_data = load_input(sys.argv[1]).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(data))  # answer: 67558
    print("Part 2:", fn_p2(data))  # answer: 78990
