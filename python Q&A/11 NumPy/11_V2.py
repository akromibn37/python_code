import numpy as np

rentalrates = np.array([int(e) for e in input().split()])
sales = np.ndarray((4,5))
for k in range(4):
    sales[k,] = [int(e) for e in input().split()]
totalsales = np.sum(sales,axis=0)
d = np.argmax(totalsales)
days = ['Mon','Tue','Wed','Thu','Fri']
print(days[d],totalsales[d])
salevalues = np.dot(rentalrates,sales)
print(' '.join([str(e) for e in salevalues]))
