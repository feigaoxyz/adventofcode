with open('12.in', 'r') as f:
    lines = f.read().splitlines()

line = lines[0]

import re

nums = re.findall(r'(-?\d+)', line)

print('One:', sum(map(int, nums)))

import json

js = json.loads(line)

def sum_js(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, list):
        return sum(sum_js(child) for child in obj)
    if isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        else:
            return sum(sum_js(child) for child in obj.values())
    return 0

print('Two:', sum_js(js))
