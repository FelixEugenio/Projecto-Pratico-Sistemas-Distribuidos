import xmlrpc.client

# Conectar-se ao servidor XML-RPC
s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Obter entrada do usuário para dois valores
x = int(input("Digite o 1º valor: "))
y = int(input("Digite o 2º valor: "))

# Exibir o tipo de x
print(f"Tipo de x: {type(x)}")  # Isso irá imprimir <class 'int'>

# Chamar a função 'isDivided_function' no servidor e exibir a mensagem de divisibilidade
if s.isDivided_function(x, y):  # Se for divisível
    division_result = x / y
    print(f"O valor {x} é divisível por {y}. O resultado da divisão é {division_result}.")
else:  # Se não for divisível
    print(f"O valor {x} não é divisível por {y}.")

# Exibir a lista de métodos disponíveis no servidor
print(f"Métodos disponíveis no servidor: {s.system.listMethods()}")
