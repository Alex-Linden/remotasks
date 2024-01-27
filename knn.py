import sklearn.neighbors as neighbors
import numpy as np

# define training data and target values
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([0, 0, 1, 1])

# train model
knn = neighbors.KNeighborsClassifier(n_neighbors = 3)
knn.fit(X, y)

# generate new, unseen data
# X2 will be used for prediction, and y2 is ground truth
X2 = np.array([[0, 0, 1], [1.1, 1.1, 1]])

y2 = np.array([0, 1])

# use the trained model to make predictions on X2
output = knn.predict(X2)

print("Predicted output: ", output)
print("Ground truth: ", y2)
