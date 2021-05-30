# ProyectoFinal-Docker

## Docker
  - Jupyter Notebook
  - Dash
  - PostgreSQL

Proyecto Final EC2 disponiendo Docker para realizar visualización de datos alojados en un contenedor de base de datos desde contenedores de Jupyter Notebook y Dash

## Pasos
1. Descargar proyecto vía git clone o descargando zip.
2. Ingresar vía terminal a la carpeta del proyecto.
3. Ejecutar ```docker-compose up -d```
4. Entrar a localhost:8888 para ingresar al Notebook de Jupyter
     - Contraseña: 1234     
5. Entrar a localhost:8050 para visualizar datos en Dash    

## En caso de usar [PlayWithDocker](https://labs.play-with-docker.com/)
1. Descargar proyecto vía git clone.
2. Ejecutar ```cd ProyectoFinal-Docker```
3. Ejecutar ```docker-compose up -d```
4. Hacer click a "Open port" e ingresar:
  - 8888 para notebook de Jupyter
  - 8050 para Dash
