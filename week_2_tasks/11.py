def square_root(num):
    if num < 2: 
        return num
    
    left, right = 1, num // 2

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid 

        if square == num: 
            return mid
        elif square < num: 
            left += 1
        else:
            right -= 1

    return right

num = int(input('enter a number: '))
print(square_root(num))