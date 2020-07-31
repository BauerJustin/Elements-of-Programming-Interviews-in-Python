import random

# code
def random_sampling(size, A):
    for i in range(size):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]
    return A

print(random_sampling(5, [1,2,3,4,5,6,7,8,9,10]))