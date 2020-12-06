
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""


def searchRange(nums, target):
    res = [-1, -1]
    if not nums:
        return res
    res[0] = findStartIndex(nums, target)
    res[1] = findEndIndex(nums, target)
    return res


def findStartIndex(nums, target):
    index = -1
    start, end = 0, len(nums)-1
    while start <= end:
        mid = start + (end-start)//2

        if nums[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
        if nums[mid] == target:
            index = mid
    return index


def findEndIndex(nums, target):
    index = -1
    start, end = 0, len(nums)-1
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
        if nums[mid] == target:
            index = mid
    return index


nums = [5, 7, 7, 8, 8, 8, 8, 10]
target = 8
r = searchRange(nums, target)
