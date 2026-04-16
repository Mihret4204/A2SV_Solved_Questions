def binarysearchrecursive(nums, left, right, target):
 
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarysearchrecursive(nums, mid + 1, right, target)
    else:
        return binarysearchrecursive(nums, left, mid - 1, target)