# Arquivo: ex4.py

# Abre o arquivo "texto.txt" em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo_origem:
    conteudo = arquivo_origem.read()

# Abre o arquivo "copia.txt" em modo de escrita ('w')
with open('copia.txt', 'w') as arquivo_destino:
    arquivo_destino.write(conteudo)

print("Conteúdo do arquivo 'texto.txt' copiado para 'copia.txt' com sucesso!")
