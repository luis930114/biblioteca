
# Project Title

Aplicación web sobre una biblioteca

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:
- Docker
- Python (versión 3.10)
- Django 5.0.4
- Django Rest Framework 3.15.1

## Instalación y Configuración

1. Clona este repositorio en tu máquina local:
   ```bash
    git clone https://github.com/luis930114/biblioteca.git
   ```
2. Accede al directorio del proyecto
3. Crea un entorno virtual (opcional pero recomendado): 
```bash   
python -m venv venv
```
4. Activa el entorno virtual:
   ```bash
   windows: venv\Scripts\activate
   En macOS y Linux: source venv/bin/activate
   ```
5. Instala las dependencias del proyecto: 
```bash
   pip install -r requirements.txt
```
6. Ejecutar Django:
  Para ejecutar el servidor de desarrollo de Django, Asegúrate de que estás en el directorio raíz del proyecto 
7. Ejecuta el siguiente comando
```bash
   python manage.py runserver
```
8. Ejecutar las Pruebas Unitarias
Para ejecutar las pruebas unitarias del proyecto, sigue estos pasos:
```bash
python manage.py test prestamos
```
10. también se puede utilizar docker, corriendo el siguiente comando
   9.1. Crear la imagen del contenedor
      ```bash
      docker build -t image_biblioteca .
      ```
   9.2 Correr el contenedor
   ```bash
   docker run -p 8080:8000 image_biblioteca
   ```

## API Reference

#### Get all books

```http
  GET /api/books 
```



#### Create book

```http
  POST /api/books
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`   | `string` | **Required**. titulo del libro |
| `author`  | `string` | **Required**. author del libro  |
| `isbn`   | `string` | **Required**. codigo del libro |
| `genre`   | `string` | **Required**. genero del libro |




## Authors

- [@luis930114](https://github.com/luis930114)
