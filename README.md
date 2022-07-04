# TRABALHO2-LABREDES

Desenvolvedores: Ana Carolina Carvalho Cassiano e José Wigner Quintino Bindacco
<div></div>
Professor: Dr. Alexandre Pereira do Carmo
<div></div>
Disciplina de Laboratório de Redes
<br>
<br>

1. Verifique se o Docker já está instalado na sua máquina. Caso não esteja, acesse:

Para instalar no Ubuntu-> https://docs.docker.com/engine/install/ubuntu/

Para instalar no Windows-> https://docs.docker.com/desktop/windows/install/

<br>

2. Para rodar a aplicação, execute os comandos na sequêcnia e informe o endereço do servidor:

<code>
  sudo docker run -it --rm --network=host josewigner1999/servertrabalho2:server python3 server.py <i>endereço do servidor</i>
</code>
<div></div>
<code>
  sudo docker run -it --rm --network=host josewigner1999/clienttrabalho2:client python3 clientn.py <i>endereço do servidor</i>
</code>

<br>
<br>

3. Para enviar uma mensagem, é necessário seguir o seguinte padrão:
<br>
{Destinatário}: {Mensagem}
<br>
Exemplo: 
<br>
Alexandre: Esse trabalho 2 está muito bom, merece nota máxima!
<br>
<br>
4. Para sair do programa <i>clientn.py</i> digite "SAIR".
