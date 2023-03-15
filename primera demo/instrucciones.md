# Vamos a correr un contenedor con una imagen base y vamos a instalar git

Analizar el Dockerfile y correr los siguientes comandos:

docker build -t ajeetraina/alpine-git .
docker tag ajeetraina/alpine-git ajeetraina/labs-git:v1.0
docker run -itd ajeetraina/labs-git:v1.0 /bin/sh

listar contenedores --> docker ps
obtener id del contenedor

docker attach ID_CONTENEDOR

Verificar que git está instalado --> git --version
