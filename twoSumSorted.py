def twoSum(arr, target):
    left = 0
    right = len(arr)-1
    while True:
        if arr[left]+arr[right] == target:
            return [left+1, right+1]
        elif arr[left]+arr[right] < target:
            left += 1
        else:
            right -= 1


arr = [2, 7, 11, 15]
target = 9
twoSum(arr, target)
print()
