import numpy as np
x = np.array([[1,2],[3,4]])
print(np.sum(x,axis=1))
zero=np.zeros((10,10))
print(zero)
a = np.array([[0,1,2,3], [4,5,6,7], [8,9,10,11]])
print(a[2,0])
print(type(a[-1]))
firstcol=a[:,0]
print(firstcol)
print(len(firstcol))
print(a[1:,2:])
a_gt_5 = a>5
print(a_gt_5)
elements_gt_5=a[a>5]
print(elements_gt_5)
elements_gt_5 = a[a_gt_5]
print(elements_gt_5)

a = np.array([[0,1,2,3], [4,5,6,7], [8,9,10,11], [1,2,3,6], [2,4,6,4],[4,5,6,7]])
print(a.shape)
print(a[:,1])
print(len(a[2:,2:]))

x = np.zeros((6,4))
print(len(x[2:,2:]))
print(x[2:,2:])
print(x[-1,-1])
