# Arquivo: ex12.py

# Função para converter bytes em megabytes
def bytes_to_mb(bytes):
    return bytes / (1024 * 1024)

# Abre o arquivo "usuarios.txt" em modo de leitura ('r')
with open('usuarios.txt', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

usuarios = []

# Processa os dados do arquivo e calcula o espaço ocupado em MB
for linha in linhas:
    partes = linha.strip().split()
    nome = partes[0]
    espaco_bytes = int(partes[1])
    espaco_mb = bytes_to_mb(espaco_bytes)
    usuarios.append((nome, espaco_mb))

# Ordena a lista de usuários pelo espaço ocupado
usuarios.sort(key=lambda x: x[1], reverse=True)

# Abre o arquivo "relatorio.txt" em modo de escrita ('w')
with open('relatorio.txt', 'w') as arquivo_saida:
    arquivo_saida.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    arquivo_saida.write("-" * 60 + "\n")
    arquivo_saida.write("Nr. Usuário Espaço utilizado % do uso\n")

    total_espaco_mb = 0
    for i, (nome, espaco_mb) in enumerate(usuarios, start=1):
        arquivo_saida.write(f"{i} {nome.ljust(15)} {espaco_mb:.2f} MB {espaco_mb / sum([user[1] for user in usuarios]) * 100:.2f}%\n")
        total_espaco_mb += espaco_mb

    arquivo_saida.write(f"\nEspaço total ocupado: {total_espaco_mb:.2f} MB\n")
    arquivo_saida.write(f"Espaço médio ocupado: {total_espaco_mb / len(usuarios):.2f} MB\n")

print("Relatório gerado com sucesso em 'relatorio.txt'!")
