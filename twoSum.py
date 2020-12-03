from collections import defaultdict


def twoSum(arr, target):
    seen = defaultdict(int)
    for i, val in enumerate(arr):
        other = target - val
        if other in seen:
            return [i, seen[other]]
        seen[val] = i
    return []


arr = [2, 7, 11, 15]
target = 9

res = twoSum(arr, target)
print()
