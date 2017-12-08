from common import load_input

input_data = load_input(__file__.split('.')[0] + '_in.txt')

PART1_DOC = """
Part 1:  A passphrase consists of a series of words (lowercase letters) \
separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.
"""


def is_passphrase_valid(phrase: str, rearrange=False) -> bool:
    words = phrase.split()
    if rearrange:
        words = [''.join(sorted(w)) for w in words]
    return len(words) > 1 and len(words) == len(set(words))


def count_valid_passphrases(lines: str, rearrange=False) -> int:
    return sum(
        is_passphrase_valid(phrase, rearrange)
        for phrase in lines.splitlines())


fn_p1 = count_valid_passphrases
print("Part 1:", fn_p1(input_data))

PART2_DOC = """
Part 2: Now, a valid passphrase must contain no two words that are anagrams of
each other - that is, a passphrase is invalid if any word's letters can be
rearranged to form any other word in the passphrase.
"""

fn_p2 = count_valid_passphrases
print("Part 2:", fn_p2(input_data, rearrange=True))
