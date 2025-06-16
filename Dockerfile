# Dockerfile
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copia los archivos de requirements e instala dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando de ejecución
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
