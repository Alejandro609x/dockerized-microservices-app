# Usamos la imagen oficial de Python 3.11 en versión slim (ligera)
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de dependencias al directorio de trabajo
COPY requirements.txt .

# Instalamos las dependencias listadas en requirements.txt sin usar cache para ahorrar espacio
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente (carpeta src) dentro del contenedor
COPY src/ ./src

# Comando para ejecutar la aplicación usando Uvicorn, exponiendo el servidor en todas las interfaces (0.0.0.0) y puerto 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
