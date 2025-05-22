#Imagen base ligera de Python 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copia el código fuente de tu app (la carpeta src/)
COPY src/ ./src

# Comando que inicia tu API con Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
