# K-means Clustering

<p align=center>
  <img width="35%" src="https://upload.wikimedia.org/wikipedia/commons/7/7b/Kmeans_animation_withoutWatermark.gif">
</p>

Sample of K-means Clustering

### K-means Clustering 란?
> k-평균 알고리즘(K-means algorithm)은 주어진 데이터를 k개의 클러스터로 묶는 알고리즘으로, 각 클러스터와 거리 차이의 분산을 최소화하는 방식으로 동작한다. 이 알고리즘은 자율 학습의 일종으로, 레이블이 달려 있지 않은 입력 데이터에 레이블을 달아주는 역할을 수행한다. 이 알고리즘은 EM 알고리즘을 이용한 클러스터링과 비슷한 구조를 가지고 있다.
[WIKIPEDIA](https://ko.wikipedia.org/wiki/K-%ED%8F%89%EA%B7%A0_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

### Demonstration of the standard K-means algorithm

<p align=center>
  <img src="https://github.com/Xenia101/K-means-Clustering/blob/master/img/kmeans.PNG?raw=true">
</p>

1. 군집의 수 K 정의 및 초기 K개 군집의 중심을 무작위로 선택

2. 각 데이터 오브젝트들은 가장 가까이 있는 평균값을 기준으로 묶음

3. 클러스터의 중심점을 재계산

4. 각 데이터 오브젝트의 소속 클러스터가 바뀌지 않을 때 까지 2, 3 과정을 반복

## 예시

- Load the Data

```python
iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target
```

- Show scatter plot of data

<p align=center>
  <img width="35%" src="https://github.com/Xenia101/K-means-Clustering/blob/master/img/kmeans%20graph.PNG">
</p>
                        
```python
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()
```

- Do Kmeans

```python
kmeams = KMeans(n_clusters = 3, n_jobs = 4, random_state=21) # Three color(Kinds) of point / n_clusters = 3
kmeams.fit(X)

kmeams.cluster_centers_ # centers of clustering

[[5.77358491 2.69245283]
[5.006      3.418    ]
[6.81276596 3.07446809]]
```

- Show new scatter plot of data

<p align=center>
  <img width="35%" src="https://github.com/Xenia101/K-means-Clustering/blob/master/img/new%20graph.PNG?raw=true">
</p>

```python
new_y = kmeams.labels_

plt.scatter(X[:, 0], X[:, 1], c=new_y)
plt.show()
```

