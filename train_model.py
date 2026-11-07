
import pickle
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = load_breast_cancer()
X = data.data[:, :5]
y = data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy * 100)
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")
