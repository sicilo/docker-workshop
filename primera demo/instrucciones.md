docker build -t ajeetraina/alpine-git .
docker tag ajeetraina/alpine-git ajeetraina/labs-git:v1.0
docker run -itd ajeetraina/labs-git:v1.0 /bin/sh