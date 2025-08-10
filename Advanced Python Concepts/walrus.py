'''Example 1:'''

def slow():
    print("Slow function running...")
    print("Slow function running...")
    print("Slow function running...")
    print("Slow function running...")
    print("Slow function running...")
    return 2

if((a := slow()) > 3):
    print(f"Result is {a}")

else:
    print("Result is not greater than 3")

'''Example 2:'''

import random
def get_score_data():
    return random.randrange(1, 10)

scores = [score for _ in range(20) if (score := get_score_data()) >= 5]
print(scores)  # List of scores >= 5
