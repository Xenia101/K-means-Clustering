import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

plt.scatter(X[:,0], X[:,1], c=y)
plt.show()
