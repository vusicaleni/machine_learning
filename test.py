import numpy as np
from scipy import sparse
import pandas as pd
from IPython.display import display

import matplotlib.pyplot as plt
#%matplotlib inline 

x = np.array([[1,2,3], [6,8,9]])
eye = np.eye(6)

print("numPy array:\n", eye)
sparse_martrix = sparse.csr_matrix(eye)
#print("\nnScipy spase CSR matrix:\n", sparse_martrix)
#print("x:\n{}".format(x))

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation:\n", eye_coo)

x = np.linspace(-10, 10, 100)

y = np.sin(x)
plt.plot(x,y, marker="x")
plt.show()
data = {'name':["John", "Anna", "Peter", "Linda", ], 'Location': ["New york", "Paris," "Berlin","London"], 'Age':[24, 13, 53, 33] }
data_pandas = pd.DataFrame(data)
#Ipython. display allows "pretty printing of dataframes"
display(data_pandas)
display(data_pandas.Age > 30)
display(data_pandas.Location == "London")

