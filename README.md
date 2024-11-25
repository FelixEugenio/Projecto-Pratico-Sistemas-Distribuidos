Sistema Cliente-Servidor para Verificação de Divisibilidade
Descrição do Projeto
Este projeto implementa um sistema cliente-servidor simples utilizando sockets em Python, onde o servidor recebe dois números inteiros do cliente, verifica se o primeiro número é divisível pelo segundo e envia o resultado de volta ao cliente. O cliente solicita ao usuário que insira os números, envia esses números ao servidor e exibe o resultado da verificação de divisibilidade.

Objetivo
O objetivo do trabalho é desenvolver um sistema cliente-servidor onde o servidor implementa a função isDivisivel(x, y) para verificar se o primeiro número, x, é divisível pelo segundo número, y. A comunicação entre o cliente e o servidor é realizada utilizando sockets, sendo o servidor responsável pela verificação e o cliente responsável por enviar os dados e exibir o resultado.

Arquitetura do Sistema
A arquitetura do projeto segue o modelo cliente-servidor. O cliente envia dois números inteiros ao servidor, que realiza a verificação de divisibilidade e retorna o resultado para o cliente. A comunicação é estabelecida via sockets TCP/IP.

Componentes:

Servidor:
Espera por conexões de clientes.
Recebe os valores x e y enviados pelo cliente.
Executa a função isDivisivel(x, y).
Retorna o resultado (True/False ou erro) ao cliente.
Cliente:
Solicita ao usuário que insira dois números inteiros.
Envia os números para o servidor.
Recebe e exibe o resultado da verificação de divisibilidade.
Implementação
Função isDivisivel(x, y)
Esta função realiza a verificação se o número x é divisível por y. A lógica é simples: se o resto da divisão de x por y for igual a zero, então x é divisível por y.

python
Copiar código
def isDivisivel(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x % y == 0
x % y: Verifica o resto da divisão de x por y.
Se o resto for 0, retorna True (indicando que x é divisível por y).
Caso contrário, retorna False.
Implementação do Servidor
O servidor ficará aguardando conexões dos clientes, receberá os valores, processará a verificação de divisibilidade e retornará o resultado. O código para o servidor é o seguinte:

python
Copiar código
import socket

def isDivisivel(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x % y == 0

def servidor():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('localhost', 12345))
    servidor_socket.listen(1)
    print("Servidor esperando por conexão...")

    while True:
        cliente_socket, endereco_cliente = servidor_socket.accept()
        print(f"Conexão estabelecida com {endereco_cliente}")

        dados = cliente_socket.recv(1024).decode('utf-8')
        x, y = map(int, dados.split(','))

        resultado = isDivisivel(x, y)

        cliente_socket.send(str(resultado).encode('utf-8'))
        cliente_socket.close()

if __name__ == "__main__":
    servidor()
Explicação do Servidor:

O servidor utiliza a função socket.socket() para criar um socket TCP.
O servidor se conecta ao localhost na porta 12345 e aguarda conexões.
Quando um cliente se conecta, o servidor recebe os números enviados, executa a verificação de divisibilidade e envia o resultado para o cliente.
Implementação do Cliente
O cliente solicita ao usuário dois números inteiros, envia esses números ao servidor e exibe o resultado recebido. O código para o cliente é o seguinte:

python
Copiar código
import socket

def cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 12345))

    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

    cliente_socket.send(f"{x},{y}".encode('utf-8'))

    resultado = cliente_socket.recv(1024).decode('utf-8')

    print(f"O resultado da verificação de divisibilidade é: {resultado}")
    cliente_socket.close()

if __name__ == "__main__":
    cliente()
Explicação do Cliente:

O cliente solicita dois números ao usuário.
Conecta-se ao servidor na localhost e envia os números para a verificação.
Depois, o cliente recebe o resultado (True ou False) e exibe para o usuário.
Funcionamento do Sistema
O servidor é executado primeiro e fica aguardando conexões na porta 12345.
O cliente é executado e solicita ao usuário dois números inteiros.
O cliente envia os números ao servidor.
O servidor processa os números e executa a função isDivisivel(x, y) para verificar a divisibilidade.
O servidor retorna o resultado (True ou False) para o cliente.
O cliente exibe o resultado da verificação para o usuário.
Exemplo de Execução
No Cliente:

bash
Copiar código
Digite o primeiro número: 10
Digite o segundo número: 2
O resultado da verificação de divisibilidade é: True
No Servidor:

bash
Copiar código
Servidor esperando por conexão...
Conexão estabelecida com ('127.0.0.1', 56789)
Como Executar o Projeto
Pré-requisitos
Python 3.x instalado no sistema.
Rede local ou localhost para comunicação entre cliente e servidor.
Passos para Execução
Executar o Servidor: Abra um terminal e execute o código do servidor:

bash
Copiar código
python servidor.py
O servidor ficará aguardando conexões na porta 12345.

Executar o Cliente: Abra outro terminal e execute o código do cliente:

bash
Copiar código
python cliente.py
O cliente solicitará dois números ao usuário e, após enviar os dados ao servidor, exibirá o resultado da verificação de divisibilidade.

Conclusão
Este projeto demonstra como criar uma comunicação simples entre um cliente e um servidor utilizando sockets em Python. O servidor realiza a verificação de divisibilidade entre dois números inteiros, e o cliente envia os números e exibe o resultado. Este sistema é extensível para suportar outras funcionalidades e serve como uma boa introdução à programação de redes e ao modelo cliente-servidor.

Bibliografia
Socket Programming in Python: Documentação oficial do Python sobre Sockets
Divisibilidade em Matemática: Sophia Pitt - Divisibilidade
Licença
Este projeto está licenciado sob a Licença MIT.




