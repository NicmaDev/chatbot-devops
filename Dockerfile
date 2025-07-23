FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Descargar recursos de NLTK
RUN python -m nltk.downloader stopwords

# Copiar código fuente y dataset
COPY ./src /app
COPY ./data /app/data

# Entrenar modelo antes de ejecutar Flask (opcional)
RUN python chatbot/model/training.py

CMD ["python", "main.py"]
