# Arquivo: ex7.py

# Abre o arquivo "texto.txt" em modo de leitura ('r')
with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Substitui "mundo" por "Python"
conteudo_modificado = conteudo.replace("mundo", "Python")

# Abre o arquivo "modificado.txt" em modo de escrita ('w')
with open('modificado.txt', 'w') as arquivo_modificado:
    arquivo_modificado.write(conteudo_modificado)

print("Conteúdo modificado e salvo em 'modificado.txt' com sucesso!")
