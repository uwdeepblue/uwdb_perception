import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load sample dataset
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Initialize k-NN classifier
knn = cv2.ml.KNearest_create()

# Train the classifier
knn.train(np.array(X_train, dtype=np.float32), cv2.ml.ROW_SAMPLE, np.array(y_train, dtype=np.int32))

# Test the classifier
_, results, _, _ = knn.findNearest(np.array(X_test, dtype=np.float32), k=3)

# Calculate accuracy
accuracy = accuracy_score(y_test, results.ravel())
print(f"Accuracy of k-NN classifier: {accuracy * 100:.2f}%")

# Plotting the results
plt.figure(figsize=(12, 6))

# Plot the training data
plt.subplot(1, 2, 1)
for i, color in zip(range(3), ['r', 'g', 'b']):
    idx = np.where(y_train == i)
    plt.scatter(X_train[idx, 0], X_train[idx, 1], c=color, label=data.target_names[i], s=10)
plt.title('Training Data')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.legend()

# Plot the test data with predictions
plt.subplot(1, 2, 2)
for i, color in zip(range(3), ['r', 'g', 'b']):
    idx = np.where(y_test == i)
    plt.scatter(X_test[idx, 0], X_test[idx, 1], c=color, label=f'True {data.target_names[i]}', s=10)
for i, color in zip(range(3), ['r', 'g', 'b']):
    idx = np.where(results.ravel() == i)
    plt.scatter(X_test[idx, 0], X_test[idx, 1], c=color, marker='x', label=f'Predicted {data.target_names[i]}', s=10)
plt.title('Test Data with Predictions')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.legend()

plt.tight_layout()
plt.show()
