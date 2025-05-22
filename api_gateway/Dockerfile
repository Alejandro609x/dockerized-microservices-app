# Usa una imagen base ligera de Python 3.10 (versión "slim" para reducir tamaño)
FROM python:3.10-slim  

# Establece el directorio de trabajo dentro del contenedor en /app
WORKDIR /app  

# Copia el archivo main.py desde el sistema host al directorio de trabajo del contenedor
COPY ./main.py /app/main.py  

# Copia el archivo de dependencias al contenedor
COPY ./requirements.txt /app/requirements.txt  

# Instala las dependencias listadas en requirements.txt sin guardar caché
RUN pip install --no-cache-dir -r requirements.txt  

# Comando por defecto para ejecutar el servidor Uvicorn, 
# expone el servicio en todas las interfaces (0.0.0.0) y en el puerto 8000.
# "main:app" indica que debe buscar la instancia `app` dentro del archivo `main.py`.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  

