import joblib
import numpy as np

class Model:

    def __init__(self):
        self.model = joblib.load("src/weights/gradboost.joblib")
        self.vectorizer = joblib.load("src/weights/tfifd.joblib")

    def predict(self, text: str):
        preprocess_text = self.preprocess(text)
        vectorized_text = self.vectorizer.transform(np.array([preprocess_text]))
        return int(self.model.predict(vectorized_text)[0])

    def preprocess(self, text: str):
        return text.lower()