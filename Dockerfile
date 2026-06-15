FROM python:3.11-slim

WORKDIR /app

# Instalamos Flask directamente para mantenerlo simple
RUN pip install --no-cache-dir flask

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]