# Arquivo: ex3.py

# Abre o arquivo "texto.txt" em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

numero_de_linhas = len(linhas)

print(f"O arquivo 'texto.txt' contém {numero_de_linhas} linhas.")
