# Criar uma função para verificar se um número é primo
def eh_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Criar uma lista com os números de 1 a 20
lista = list(range(2, 21))

# Criar uma lista com os números primos de 1 a 20
lista = [x for x in lista if eh_primo(x)]

# Imprimir a lista
print(lista)
