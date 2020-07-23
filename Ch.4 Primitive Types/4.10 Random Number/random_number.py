import random

# code
def random_number(lower,upper):
    return int(random.uniform(lower,upper+1))

print(random_number(1,6))