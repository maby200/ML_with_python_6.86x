import numpy as np

def randomization(n):
    
    if n > 0:
        A = np.random.random([n,1]) # it can also be np.random.rand(n,1)
        #
    return A



n = int(input('enter a positive number: '))

print(randomization(n))