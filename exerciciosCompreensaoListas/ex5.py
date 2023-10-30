# Criar uma lista com os números de 1 a 30
lista = list(range(1, 31))

# Criar uma lista com os números divisíveis por 3 e 5
lista = [x for x in lista if x % 3 == 0 and x % 5 == 0]

# Imprimir a lista
print(lista)
