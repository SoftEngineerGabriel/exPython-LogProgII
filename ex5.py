# Arquivo: ex5.py

# Abre o arquivo "texto.txt" em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo_texto:
    conteudo_texto = arquivo_texto.read()

# Abre o arquivo "copia.txt" em modo de leitura ('r')
with open('copia.txt', 'r') as arquivo_copia:
    conteudo_copia = arquivo_copia.read()

# Abre o arquivo "combinado.txt" em modo de escrita ('w')
with open('combinado.txt', 'w') as arquivo_combinado:
    # Escreve o conteúdo combinado nos arquivos de destino
    arquivo_combinado.write(conteudo_texto + "\n" + conteudo_copia)

print("Conteúdo dos arquivos 'texto.txt' e 'copia.txt' combinados em 'combinado.txt' com sucesso!")
