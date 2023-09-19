# Arquivo: ex2.py

# Abre o arquivo "texto.txt" em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo 'texto.txt':")
print(conteudo)
