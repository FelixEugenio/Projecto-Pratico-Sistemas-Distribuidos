import xmlrpc.client
# Conectar-se ao servidor XML-RPC
s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Obter entrada do usuário para dois valores
# Solicitar entradas do usuário
x = input("Digite o 1º valor: ")
y = input("Digite o 2º valor: ")

# Validar se as entradas são números inteiros
try:
    x = int(x)
    y = int(y)

    print(f"Tipo de x: {type(x)}")

    # Verificar se é possível dividir por zero
    if y == 0:
        print("Erro: Não é possível dividir por zero.")
    elif x % y == 0:  # Verificar se x é divisível por y
        division_result = x / y
        print(f"O valor {x} é divisível por {y}. O resultado da divisão é {division_result}.")
    else:
        print(f"O valor {x} não é divisível por {y}.")
except ValueError:
    print("Erro: Por favor, insira apenas números inteiros.")


