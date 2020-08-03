import bisect
import itertools
import random

#code
def random_number_gen(values, prob):
    return values[bisect.bisect(list(itertools.accumulate(prob)), random.random())]

print(random_number_gen([3,5,7,11], [9/18,6/18,2/18,1/18]))