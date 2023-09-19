# Arquivo: ex6.py

# Abre o arquivo "texto.txt" em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Divide o conteúdo em palavras
palavras = conteudo.split()

numero_de_palavras = len(palavras)

print(f"O arquivo 'texto.txt' contém {numero_de_palavras} palavras.")
