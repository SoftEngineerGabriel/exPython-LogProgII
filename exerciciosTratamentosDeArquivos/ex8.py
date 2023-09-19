# Arquivo: ex8.py

# Abre o arquivo "texto.txt" em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Adiciona a frase ao final do conteúdo
conteudo += "\nIsso é incrível!"

# Abre o arquivo "texto.txt" em modo de escrita ('w')
with open('texto.txt', 'w') as arquivo:
    arquivo.write(conteudo)

print("Frase adicionada ao final do arquivo 'texto.txt' com sucesso!")
