def eh_bissexto(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

ano = 2024

if eh_bissexto(ano):
    lista = [(ano, 1, dia) for dia in range(1, 32)]
else:
    lista = [(ano, 1, dia) for dia in range(1, 31)]

print(lista)
