FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade pip

CMD ["python", "procesador.py", "datos.csv", "v1"]

