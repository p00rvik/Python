from functools import reduce
def sum(a,b):
    return a + b

number = [1, 2, 3, 4, 5]
new = reduce(sum,number)
# new = reduce(lambda a, b: a + b, number)
print(new)
