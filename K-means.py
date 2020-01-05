from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

plt.scatter(X[:,0], X[:,1], c=y)
plt.show()

kmeams = KMeans(n_clusters = 3, n_jobs = 4, random_state=21)
kmeams.fit(X)

print(kmeams.cluster_centers_)

new_y = kmeams.labels_

plt.scatter(X[:, 0], X[:, 1], c=new_y)
plt.show()
