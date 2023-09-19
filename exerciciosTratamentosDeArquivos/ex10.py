# Arquivo: ex10.py

# Abre o arquivo "numeros.txt" em modo de leitura ('r')
with open('numeros.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Divide os números e os converte em uma lista de inteiros
numeros = [int(numero) for numero in conteudo.split(",")]

# Calcula a soma dos números
soma = sum(numeros)

print(f"A soma dos números em 'numeros.txt' é {soma}.")
