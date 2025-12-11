nums = list(map(lambda x: int(x), input().split()))
left = right = 0

while left < len(nums) and right < len(nums):
    if nums[left] == 0:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
        right += 1
    else:
        left += 1

print(nums)
