# Criar uma string
string = "Olá, mundo!"

# Criar uma lista com as palavras da string
lista = string.split()

# Criar uma lista com as palavras da string que tenham mais de 3 letras
lista = [x for x in lista if len(x) > 3]

# Imprimir a lista
print(lista)
