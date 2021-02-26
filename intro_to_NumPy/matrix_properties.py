import numpy as np
'''
x = np.array([3,5])
y = np.array([[3,5,1],[1,3,9]])
z = y.transpose()


print('x shape is:\n',x.shape, '\nz shape is:\n ', z.shape)
'''


'''
def operations(h, w):
    A = np.random.random([h, w])
    B = np.random.random([h, w])

    s = A + B

    return A, B, s

print(operations(3,2))
'''

######### MAX, MIN & NORM ##########

def operations(A, B):

    s = A + B

    return np.linalg.norm(s)

print(operations([3,1],[2,1]))