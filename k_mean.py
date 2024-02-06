from sklearn import datasets
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans, GaussianMixture

# Generate a sample dataset
dataset = datasets.make_blobs(n_samples=500, n_features=3, center_box=(-10.0, 10.0), cluster_std=2.0)
X, y = dataset

# Perform K-Means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
kmeans_labels = kmeans.predict(X)

# Perform GMM clustering
gmm = GaussianMixture(n_components=3)
gmm.fit(X)
gmm_labels = gmm.predict(X)

# Create a 3D scatter plot to visualize the K-Means clustering
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans_labels, s=50, cmap='viridis')
ax.set_xlabel('X0')
ax.set_ylabel('X1')
ax.set_zlabel('X2')
ax.set_title('K-Means Clustering')

# Create a 3D scatter plot to visualize the GMM clustering
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=gmm_labels, s=50, cmap='viridis')
ax.set_xlabel('X0')
ax.set_ylabel('X1')
ax.set_zlabel('X2')
ax.set_title('Gaussian Mixture Model Clustering')

# Show the plots
plt.show()
