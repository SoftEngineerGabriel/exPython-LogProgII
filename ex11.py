# Arquivo: ex11.py

import re

# Função para verificar se um endereço IP é válido
def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True

# Abre o arquivo de entrada em modo de leitura ('r')
with open('enderecos.txt', 'r') as arquivo_entrada:
    enderecos = arquivo_entrada.read().splitlines()

enderecos_validos = []
enderecos_invalidos = []

# Verifica cada endereço IP
for endereco in enderecos:
    if is_valid_ip(endereco):
        enderecos_validos.append(endereco)
    else:
        enderecos_invalidos.append(endereco)

# Abre o arquivo de saída em modo de escrita ('w')
with open('relatorio_enderecos.txt', 'w') as arquivo_saida:
    arquivo_saida.write("[Endereços válidos:]\n")
    arquivo_saida.write("\n".join(enderecos_validos))
    arquivo_saida.write("\n[Endereços inválidos:]\n")
    arquivo_saida.write("\n".join(enderecos_invalidos))

print("Relatório gerado com sucesso em 'relatorio_enderecos.txt'!")
