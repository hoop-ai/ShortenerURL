# Imagen base
FROM python:3.11-slim

# Setea el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Expone el puerto
EXPOSE 8000

# Comando para correr FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
