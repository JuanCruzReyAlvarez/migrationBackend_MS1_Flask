# IMAGEN:

FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor

WORKDIR /app

COPY . .

# Dependencias de la aplicación

RUN pip install --no-cache-dir -r requirements.txt

# Expongo 5000, su interfaz Grafica en ReactJS expone 3000

EXPOSE 5000

# Comando para ejecutar la aplicación Flask

CMD ["python", "index.py"]
