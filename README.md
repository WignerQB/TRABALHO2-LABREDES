# TRABALHO2-LABREDES

1) Verifique se o Docker já está instalado na sua máquina. Caso não esteja, acesse:

Para instalar no Ubuntu:
<code>
  sudo apt-get update
  sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
  sudo mkdir -p /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu      \$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
</code>

Para instalar no Windows-> https://docs.docker.com/desktop/windows/install/


2) Para rodar a aplicação, execute os comandos na sequêcnia e informe o endereço do servidor:

<code>
  sudo docker run -it --rm --network=host josewigner1999/servertrabalho2:server python3 server.py <i>endereço do servidor</i>
</code>
<div></div>
<code>
  sudo docker run -it --rm --network=host josewigner1999/clienttrabalho2:client python3 clientn.py <i>endereço do servidor</i>
</code>
