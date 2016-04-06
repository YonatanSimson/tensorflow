import numpy as np
scores = np.array([3.0, 1.0, 0.2])
def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    w = np.exp(x)
    return w/np.sum(w, axis=0)
print(softmax(scores *10))
print(softmax(scores /10))

b = 1
a = b
for i in xrange(10**6):
    a = a + 1e-6
print a - b

