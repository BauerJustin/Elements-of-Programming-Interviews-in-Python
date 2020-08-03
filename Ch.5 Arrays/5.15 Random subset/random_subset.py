import random

#code
def random_subset(n, k):
    elements = {}
    for i in range(k):
        index = random.randrange(i, n)
        index_mapped = elements.get(index, index)
        i_mapped = elements.get(i, i)
        elements[index] = i_mapped
        elements[i] = index_mapped
    return [elements[i] for i in range(k)]

print(random_subset(5,5))