from collections import defaultdict


def threeSum(nums, target):
    myDict = defaultdict(int)
    for i, val in enumerate(nums):
        myDict[val] = i

    for i, val1 in enumerate(nums):
        for j, val2 in enumerate(nums):
            other = target - (val1 + val2)
            if other in myDict:
                if myDict[other] == i or myDict[other] == j:
                    continue
                return [i, j, myDict[other]]
    return []


arr = [1, 2, 6, 0, 12, 3]
target = 15
res = threeSum(arr, target)
print()
