# Arquivo: ex1.py

# Abre o arquivo "texto.txt" em modo de escrita ('w')
with open('texto.txt', 'w') as arquivo:
    # Escreve o texto no arquivo
    arquivo.write("Olá, mundo!")

print("Arquivo 'texto.txt' criado e texto escrito com sucesso!")
