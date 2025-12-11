nums = list(map(lambda x: int(x), input('enter list of numbers: ').split()))
target = int(input('enter the target: '))

for left in range(len(nums)):
    for right in range(left + 1, len(nums)):
        if nums[left] + nums[right] == target:
            print([left, right])
            break

