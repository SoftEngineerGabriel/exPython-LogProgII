# Arquivo: ex9.py

# Abre o arquivo "texto.txt" em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Remove os espaços em branco e conta as letras
numero_de_letras = len(conteudo.replace(" ", ""))

print(f"O arquivo 'texto.txt' contém {numero_de_letras} letras (excluindo espaços).")
