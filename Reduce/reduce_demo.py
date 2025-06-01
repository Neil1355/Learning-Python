from functools import reduce
numbers = [5, 12, 7, 20, 9, 15, 3, 25]
count_greater_than_10 = reduce(lambda count, x: count + (1 if x > 10 else 0), numbers,0)
print(count_greater_than_10)


n = [1,2,3,4,5]
factorial = reduce(lambda x, y: x * y, n)
print(f"The factorial of {n} is {factorial}")