import joblib
import os
import sys

# Asegurar que src/ esté en el path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.append(project_root)

class InferenceEngine:
    def __init__(self):
        self.model = joblib.load("model.pkl")
        self.vectorizer = joblib.load("vectorizer.pkl")

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]

if __name__ == "__main__":
    engine = InferenceEngine()
    while True:
        msg = input("Tú: ")
        print("Chatbot predice:", engine.predict(msg))


