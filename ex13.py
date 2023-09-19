# Arquivo: ex13.py

def paginate_file(input_filename, output_filename, line_length, lines_per_page):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()

    page_number = 1
    page_content = []

    with open(output_filename, 'w') as output_file:
        for line in lines:
            line = line.strip()
            if len(line) > line_length:
                raise ValueError("A linha é mais longa do que o comprimento máximo permitido.")
            
            page_content.append(line)

            if len(page_content) == lines_per_page:
                output_file.write("\n".join(page_content))
                output_file.write(f"\n\nPágina {page_number}, arquivo original: {input_filename}\n\n")
                page_content = []
                page_number += 1

        if page_content:
            output_file.write("\n".join(page_content))
            output_file.write(f"\n\nPágina {page_number}, arquivo original: {input_filename}\n\n")

    print("Arquivo paginado com sucesso!")

# Chamando a função para paginar o arquivo
paginate_file('input.txt', 'output.txt', 76, 60)
