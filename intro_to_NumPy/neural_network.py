import numpy as np

'''
def neural_network(inputs, weights):
    
    weights_t = np.transpose(weights)
    a = np.matmul(weights_t, inputs)

    return np.tanh(a)

print(neural_network(np.array([2,1]),np.array([2,2])))

'''


def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    if x <= y:
        return x*y
    else:
        return x/y

#print(scalar_function(2, 3))

vfunc = np.vectorize(scalar_function)
print(vfunc)


def vector_function(x,y):

    x = np.array(x)
    y = np.array(y)
    
    return np.vectorize()

