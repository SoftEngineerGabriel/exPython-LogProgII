nomes_arquivos = ["teste3.py", "teste4.py"]


for nome_arquivo in nomes_arquivos:
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"o `{nome_arquivo}` criado com sucesso!")

    print(f"o `{nome_arquivo}` criado com sucesso!")
