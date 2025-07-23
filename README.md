## 🤖 Chatbot IA con DevOps
Este proyecto implementa un chatbot inteligente capaz de detectar si un texto fue escrito por un humano o por una inteligencia artificial, utilizando técnicas de procesamiento de lenguaje natural y aprendizaje automático. Toda la solución está contenida y automatizada con herramientas DevOps.

---

## 🛠️ Tecnologías utilizadas
Python 3.9

Flask – API web para el chatbot

scikit-learn – Modelo de clasificación

NLTK – Preprocesamiento del texto

Docker & Docker Compose – Contenerización

GitHub Actions – CI/CD automatizado

Prometheus + Grafana – Monitorización

## 🚀 ¿Cómo correr el proyecto?
1. Clona el repositorio
```bash
Copiar
Editar
git clone https://github.com/tu-usuario/chatbot-devops.git
cd chatbot-devops
```

2. Levanta todo con Docker
```bash
Copiar
Editar
docker-compose up --build
```
Esto levantará:

El chatbot en http://localhost:5000

Prometheus en http://localhost:9090

Grafana en http://localhost:3000

---

## 🧠 Entrenamiento del modelo
Cada vez que se construye el contenedor, se entrena automáticamente el modelo con los datos de data/dataset.csv. El modelo generado (model.pkl, vectorizer.pkl) se guarda en /app/.

💬 Cómo usar el chatbot
Puedes enviarle texto al endpoint /predict para saber si lo escribió un humano o una IA:

```bash
Copiar
Editar
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "Hola, ¿cómo estás?"}'
```
Respuesta esperada:

```json
Copiar
Editar
{"prediction": "humano"}
```
---

## 🧪 Pruebas
Para correr las pruebas manualmente:

```bash
Copiar
Editar
PYTHONPATH=src pytest tests/
```
Las pruebas también se ejecutan automáticamente mediante GitHub Actions con cada push o pull request.

---

## 📊 Monitorización
Se expone el endpoint /metrics con estadísticas de uso para Prometheus. Grafana permite visualizar:

Número total de peticiones

Tiempo promedio de respuesta

Tasa de errores HTTP

Accede a:

Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (usuario: admin, clave: admin)

---

## 📁 Estructura del proyecto
```bash
Copiar
Editar
chatbot-devops/
├── data/                  # Dataset real para entrenamiento
├── src/                   # Código fuente del chatbot
│   ├── main.py            # API Flask
│   ├── chatbot/           # Módulos del bot
│   └── utils/             # Config y logs
├── tests/                 # Pruebas automatizadas
├── monitoring/            # Configuración de Prometheus
├── Dockerfile             # Imagen del chatbot
├── docker-compose.yml     # Orquestación de servicios
├── requirements.txt       # Dependencias del proyecto
└── .github/workflows/     # Pipeline CI/CD
```
---

## ✅ Estado del proyecto
Fase	Estado
Planificación	✅ Completada
Codificación	✅ Completada
Entrenamiento	✅ Completado
Pruebas	✅ Automatizadas
CI/CD	✅ GitHub Actions
Despliegue local	✅ Docker
Monitorización	✅ Prometheus + Grafana

---

📌 Autor
Desarrollado por Nicolás
