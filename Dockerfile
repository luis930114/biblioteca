# Utilizamos la imagen oficial de Python como base
FROM python:3.10

# Establecemos el directorio de trabajo en /code
WORKDIR /code

# Copiamos el archivo de requisitos al directorio de trabajo
COPY requirements.txt /code/

# Instalamos las dependencias de Python
RUN pip install -r requirements.txt

# Copiamos el código de la aplicación al directorio de trabajo
COPY . /code/

# Comando por defecto para ejecutar la aplicación (ajústalo según tu configuración)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

