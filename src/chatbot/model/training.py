import sys
import os

# Agrega src/ al path si no está ya
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.append(project_root)
    
import pandas as pd
import joblib
from chatbot.ai_recognition import AIRecognitionModel
from sklearn.metrics import classification_report

# Preprocesamiento
import nltk
import string
from nltk.corpus import stopwords
nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [t for t in tokens if t not in stopwords.words('spanish')]
    return ' '.join(tokens)

# Leer dataset
from utils.config import DATASET_PATH
df = pd.read_csv(DATASET_PATH)

# Preprocesar
df['text'] = df['text'].apply(preprocess)

X = df['text'].tolist()
y = df['label'].tolist()

# Entrenar
model = AIRecognitionModel()
model.train(X, y)

# Guardar
joblib.dump(model.model, "model.pkl")
joblib.dump(model.vectorizer, "vectorizer.pkl")

# Métricas
y_pred = [model.predict(t) for t in X]
print("\n=== MÉTRICAS DEL MODELO ===\n")
print(classification_report(y, y_pred))
