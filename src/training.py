from joblib import dump
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from constants import MODEL_PATH


def load_data():
    iris = load_iris()
    return iris.data, iris.target, iris.target_names


def train_model(X, y):
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model


def save_model(model, target_names, path: str = MODEL_PATH):
    dump({"model": model, "target_names": target_names}, path)
    return path


if __name__ == "__main__":
    X, y, target_names = load_data()
    model = train_model(X, y)
    save_model(model, target_names)
    print(f"Saved trained model to {MODEL_PATH}")
