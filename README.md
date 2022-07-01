# TRABALHO2-LABREDES

1) Verifique o Docker já está instalado na sua máquina. Caso não esteja, acesse:
Para Ubuntu-> https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
Para Windows-> https://docs.docker.com/desktop/windows/install/


2) Buildando a imagem:

sudo docker build -t josewigner1999/


3) Para rodar o container:

sudo docker run -it --rm --network=host josewigner1999/servertrabalho2:server

sudo docker run -it --rm --network=host josewigner1999/clienttrabalho2:client


