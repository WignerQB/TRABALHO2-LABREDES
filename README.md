# TRABALHO2-LABREDES

1) Verifique o Docker já está instalado na sua máquina. Caso não esteja, acesse:

Para Ubuntu-> https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

Para Windows-> https://docs.docker.com/desktop/windows/install/


2) Para rodar a aplicação, execute os comandos na sequêcnia e informe o endereço do servidor:

<code>
  sudo docker run -it --rm --network=host josewigner1999/servertrabalho2:server
</code>
<div></div>
<code>
  sudo docker run -it --rm --network=host josewigner1999/clienttrabalho2:client python3 clientn.py "endereço do servidor"
</code>


3) 
