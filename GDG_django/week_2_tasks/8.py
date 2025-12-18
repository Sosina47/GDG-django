nums = list(map(lambda x: int(x), input().split()))
left, right = 0, len(nums) - 1
while left < right:
    if nums[left] != 0:
        left += 1
    else:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
        right -= 1

print(nums)

