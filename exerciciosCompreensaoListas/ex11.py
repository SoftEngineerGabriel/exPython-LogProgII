nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Heitor", "Isabela", "João"]

lista = [nome.translate({ord(v): " " for v in "aeiou"}) for nome in nomes[:10]]

print(lista)
