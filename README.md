<h1>Sistema Cliente-Servidor para Verificação de Divisibilidade</h1>

<h2>Descrição do Projeto</h2>

<p>Este projeto implementa um sistema cliente-servidor simples utilizando sockets em Python, onde o servidor recebe dois números inteiros do cliente, verifica se o primeiro número é divisível pelo segundo e envia o resultado de volta ao cliente. O cliente solicita ao usuário que insira os números, envia esses números ao servidor e exibe o resultado da verificação de divisibilidade.</p>

<h3>Objetivo</h3>

<p>O objetivo do trabalho é desenvolver um sistema cliente-servidor onde o servidor implementa a função <code>isDivisivel(x, y)</code> para verificar se o primeiro número, <code>x</code>, é divisível pelo segundo número, <code>y</code>. A comunicação entre o cliente e o servidor é realizada utilizando sockets, sendo o servidor responsável pela verificação e o cliente responsável por enviar os dados e exibir o resultado.</p>

<h2>Arquitetura do Sistema</h2>

<p>A arquitetura do projeto segue o modelo cliente-servidor. O cliente envia dois números inteiros ao servidor, que realiza a verificação de divisibilidade e retorna o resultado para o cliente. A comunicação é estabelecida via sockets TCP/IP.</p>

<h3>Componentes:</h3>
<ul>
  <li><strong>Servidor:</strong>
    <ul>
      <li>Espera por conexões de clientes.</li>
      <li>Recebe os valores <code>x</code> e <code>y</code> enviados pelo cliente.</li>
      <li>Executa a função <code>isDivisivel(x, y)</code>.</li>
      <li>Retorna o resultado (True/False ou erro) ao cliente.</li>
    </ul>
  </li>
  <li><strong>Cliente:</strong>
    <ul>
      <li>Solicita ao usuário que insira dois números inteiros.</li>
      <li>Envia os números para o servidor.</li>
      <li>Recebe e exibe o resultado da verificação de divisibilidade.</li>
    </ul>
  </li>
</ul>

<h2>Implementação</h2>

<h3>Função <code>isDivisivel(x, y)</code></h3>

<p>Esta função realiza a verificação se o número <code>x</code> é divisível por <code>y</code>. A lógica é simples: se o resto da divisão de <code>x</code> por <code>y</code> for igual a zero, então <code>x</code> é divisível por <code>y</code>.</p>

<pre><code>
def isDivided_function(x, y):
        return x % y == 0
</code></pre>

<ul>
  <li><code>x % y</code>: Verifica o resto da divisão de <code>x</code> por <code>y</code>.</li>
  <li>Se o resto for 0, retorna <code>True</code> (indicando que <code>x</code> é divisível por <code>y</code>).</li>
  <li>Caso contrário, retorna <code>False</code>.</li>
</ul>

<h3>Implementação do Servidor</h3>

<p>O servidor ficará aguardando conexões dos clientes, receberá os valores, processará a verificação de divisibilidade e retornará o resultado. O código para o servidor é o seguinte:</p>

<pre><code>
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    # Register introspection functions
    server.register_introspection_functions()
    
    # Register function to check divisibility
    def isDivided_function(x, y):
        return x % y == 0
    server.register_function(isDivided_function, 'isDivided_function')

    # Run the server's main loop
    print("Server is running...")
    server.serve_forever()
</code></pre>

<h4>Explicação do Servidor:</h4>
<ul>
  <li>O servidor utiliza a função <code>socket.socket()</code> para criar um socket TCP.</li>
  <li>O servidor se conecta ao <code>localhost</code> na porta <code>12345</code> e aguarda conexões.</li>
  <li>Quando um cliente se conecta, o servidor recebe os números enviados, executa a verificação de divisibilidade e envia o resultado para o cliente.</li>
</ul>

<h3>Implementação do Cliente</h3>

<p>O cliente solicita ao usuário dois números inteiros, envia esses números ao servidor e exibe o resultado recebido. O código para o cliente é o seguinte:</p>

<pre><code>
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
</code></pre>

<h4>Explicação do Cliente:</h4>
<ul>
  <li>O cliente solicita dois números ao usuário.</li>
  <li>Conecta-se ao servidor na <code>localhost</code> e envia os números para a verificação.</li>
  <li>Depois, o cliente recebe o resultado (True ou False) e exibe para o usuário.</li>
</ul>

<h2>Funcionamento do Sistema</h2>

<ol>
  <li>O <strong>servidor</strong> é executado primeiro e fica aguardando conexões na porta <code>12345</code>.</li>
  <li>O <strong>cliente</strong> é executado e solicita ao usuário dois números inteiros.</li>
  <li>O <strong>cliente</strong> envia os números ao servidor.</li>
  <li>O <strong>servidor</strong> processa os números e executa a função <code>isDivisivel(x, y)</code> para verificar a divisibilidade.</li>
  <li>O <strong>servidor</strong> retorna o resultado (True ou False) para o cliente.</li>
  <li>O <strong>cliente</strong> exibe o resultado da verificação para o usuário.</li>
</ol>

<h3>Exemplo de Execução</h3>

<h4>No Cliente:</h4>
<pre><code>
Digite o primeiro número: 10
Digite o segundo número: 2
O resultado da verificação de divisibilidade é: True
</code></pre>

<h4>No Servidor:</h4>
<pre><code>
Servidor esperando por conexão...
Conexão estabelecida com ('127.0.0.1', 56789)
</code></pre>

<h2>Como Executar o Projeto</h2>

<h3>Pré-requisitos</h3>

<ul>
  <li>Python 3.x instalado no sistema.</li>
  <li>Rede local ou <code>localhost</code> para comunicação entre cliente e servidor.</li>
</ul>

<h3>Passos para Execução</h3>

<ol>
  <li><strong>Executar o Servidor:</strong>
    <p>Abra um terminal e execute o código do servidor:</p>
    <pre><code>python servidor.py</code></pre>
    <p>O servidor ficará aguardando conexões na porta <code>12345</code>.</p>
  </li>
  <li><strong>Executar o Cliente:</strong>
    <p>Abra outro terminal e execute o código do cliente:</p>
    <pre><code>python cliente.py</code></pre>
    <p>O cliente solicitará dois números ao usuário e, após enviar os dados ao servidor, exibirá o resultado da verificação de divisibilidade.</p>
  </li>
</ol>

<h2>Conclusão</h2>

<p>Este projeto demonstra como criar uma comunicação simples entre um cliente e um servidor utilizando sockets em Python. O servidor realiza a verificação de divisibilidade entre dois números inteiros, e o cliente envia os números e exibe o resultado. Este sistema é extensível para suportar outras funcionalidades e serve como uma boa introdução à programação de redes e ao modelo cliente-servidor.</p>

<h2>Bibliografia</h2>

<ul>
  <li><a href="https://docs.python.org/3/library/socket.html">Socket Programming in Python</a> - Documentação oficial do Python sobre Sockets</li>
  <li><a href="https://www.sophia.pitt.edu/divisibility-operations">Divisibilidade em Matemática</a> - Sophia Pitt - Divisibilidade</li>
</ul>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a <a href="LICENSE">Licença MIT</a>.</p>
