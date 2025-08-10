number = [2,3,4,6]
def square(x):
    return x * x

new= list(map(square, number))
# new= list(map(lambda x: x * x, number))
print(new)
