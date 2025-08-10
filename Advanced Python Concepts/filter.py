def is_grerter_than_five(x):
    return x > 5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = list(filter(is_grerter_than_five, numbers))
# new = list(filter(lambda x: x > 5, numbers))
print(new)
