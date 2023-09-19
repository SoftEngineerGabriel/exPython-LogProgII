# Arquivo: ex14.py

# Abre o arquivo de entrada em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

# Remove espaços repetidos e linhas em branco repetidas
linhas_limpas = []
linha_em_branco = False

for linha in linhas:
    linha = linha.rstrip()
    if linha:
        if linha_em_branco:
            linhas_limpas.append('')
            linha_em_branco = False
        linhas_limpas.append(' '.join(linha.split()))
    else:
        linha_em_branco = True

# Abre o arquivo de saída em modo de escrita ('w')
with open('texto_limpo.txt', 'w') as arquivo_saida:
    arquivo_saida.write('\n'.join(linhas_limpas))

print("Arquivo 'texto_limpo.txt' criado com espaços e linhas em branco repetidas eliminados.")
