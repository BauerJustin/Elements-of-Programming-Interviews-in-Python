import random
import itertools

# code
def random_sampling(size, A):
    current = list(itertools.islice(A,size))
    num = size
    for item in A:
        num += 1
        index = random.randrange(num)
        if index < size:
            current[index] = item
    return current

print(random_sampling(5, [1,2,3,4,5,6,7,8,9,10]))