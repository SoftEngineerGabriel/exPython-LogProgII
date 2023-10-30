nomes_arquivos = ["ex3.py"]


for nome_arquivo in nomes_arquivos:
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"o `{nome_arquivo}` criado com sucesso!")

    print(f"o `{nome_arquivo}` criado com sucesso!")
