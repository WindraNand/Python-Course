# lambda = single expression that return a value

squared = lambda num : num * num
print(squared(2))

addTwo = lambda num : num + 2
minusTwo = lambda num : num - 2
divideTwo = lambda num : num / 2

print(divideTwo(4))
print(minusTwo(5))
print(addTwo(5))

sum = lambda a , b : a + b

print(sum(2, 45))

######################################


def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

###############################



numbers = [1, 2, 3, 5]

squarednums = map(lambda num : num * num, numbers)

print(list(squarednums))

#################################

lambda num : num % 2 != 0

odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))

#################################

from functools import reduce

lambda acc, curr: acc + curr
numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)




names = ["win", "dra1", "mon"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)