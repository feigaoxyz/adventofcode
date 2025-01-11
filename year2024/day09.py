import sys
from copy import deepcopy


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, "r") as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")
        return ""


sample_raw_data = """
2333133121414131402
""".strip()
# 12345
# 2333133121414131402


def preprocess(raw: str):
    disk = list()
    for idx, ls in enumerate(raw):
        disk.append([idx // 2 if idx % 2 == 0 else -1, int(ls)])
    # print(disk)
    return disk


def checksum(disk):
    cs = st = 0
    for did, ls in disk:
        if did != -1:
            cs += (st + st + ls - 1) * ls // 2 * did
        st += ls
    return cs


def fn_p1(disk):
    # move
    i = 0  # head
    j = len(disk) - 1  # tail
    while True:
        # move head to first free
        while i < len(disk) and disk[i][0] != -1:
            i += 1
        # move tail to last file
        while j >= 0 and disk[j][0] == -1:
            j -= 1
        # all processed
        if i >= j:
            break
        if disk[i][1] == disk[j][1]:  # free = file
            disk[i][0] = disk[j][0]
            disk[j][0] = -1
        elif disk[i][1] < disk[j][1]:  # free < file
            disk[i][0] = disk[j][0]
            disk = (
                disk[:j]
                + [[disk[j][0], disk[j][1] - disk[i][1]], [-1, disk[i][1]]]
                + disk[j + 1 :]
            )
        else:  # free > file
            disk = (
                disk[:i] + [disk[j][::], [-1, disk[i][1] - disk[j][1]]] + disk[i + 1 :]
            )
            j += 1
            disk[j][0] = -1
        # print(disk, i, j)

    # print(disk)

    return checksum(disk)


def fn_p2(disk):
    # print("start:", disk)
    # move
    j = len(disk) - 1  # tail
    while True:
        # move tail to last file
        while j >= 0 and disk[j][0] == -1:
            j -= 1
        if j < 0:
            break
        i = 0  # head
        # move head to first free
        while i < len(disk) and (
            disk[i][0] != -1 or (disk[i][0] == -1 and disk[i][1] < disk[j][1])
        ):
            i += 1
        if i > j:
            # print("break", i, j)
            j -= 1
            continue
        # print("before step:", i, j, disk)
        if disk[i][1] == disk[j][1]:  # free = file
            disk[i][0] = disk[j][0]
            disk[j][0] = -1
            i += 1
            j -= 1
        elif disk[i][1] < disk[j][1]:  # free < file
            j -= 1
        else:  # free > file
            disk = (
                disk[:i]
                + [[disk[j][0], disk[j][1]], [-1, disk[i][1] - disk[j][1]]]
                + disk[i + 1 :]
            )
            j += 1
            disk[j][0] = -1
            i += 1
            j -= 1
        # print("after step:", i, j, disk)

    # print("finish:", disk)

    return checksum(disk)


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 1928
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: 2858

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 6421128769094
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 6448168620520
