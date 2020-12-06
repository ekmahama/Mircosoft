"""
Search in Rotated Sorted Array Leetcode 33
"""


def search(arr, target):
    """
    Return index of the arr
    """
    if not arr:
        return -1

    # find the pivot
    left, right = 0, len(arr)-1
    while left < right:
        mid = left + (right-left)//2
        if arr[mid] < arr[right]:
            left = mid + 1
        else:
            right = mid

    # find the subarry that has the target
    start = left
    left, right = 0, len(arr)-1
    if target >= arr[start] and target <= arr[right]:
        left = start
    else:
        right = start

    # binary search
    while left <= right:
        mid = left + (right - left)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
