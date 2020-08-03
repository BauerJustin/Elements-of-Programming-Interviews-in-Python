import random

# code
def random_sampling(size, A):
    for i in range(size):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]
    return A

def random_permutation(size):
    A = list(range(size))
    return random_sampling(size, A)

print(random_permutation(5))