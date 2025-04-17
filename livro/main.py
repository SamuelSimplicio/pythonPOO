from dataclasses import dataclass
from biblioteca import Biblioteca
from livro import Livro
# Exemplo de uso das classes Livro e Biblioteca

opcoes = {
    1: "Adicionar Livro",
    2: "Exibir Livros",
    3: "Buscar Livro",
    4: "Remover Livro",
    5: "Sair"
}

biblioteca = Biblioteca()

while True:
    print("\nMenu:")
    for chave, valor in opcoes.items():
        print(f"{chave}. {valor}")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Tente novamente.")
        continue

    if opcao == 1:
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        ano = int(input("Ano de publicação: "))
        editora = input("Editora do livro: ")
        livro = Livro(titulo, autor, ano, editora)
        biblioteca.adicionar_livro(livro)
        print(f"Livro '{titulo}' adicionado com sucesso.")
    elif opcao == 2:
        biblioteca.exibir_livros()
    elif opcao == 3:
        titulo = input("Título do livro a buscar: ")
        livro = biblioteca.buscar_livro(titulo)
        if livro:
            print(livro.exibir())
        else:
            print(f"Livro '{titulo}' não encontrado na biblioteca.")
    elif opcao == 4:
        titulo = input("Título do livro a remover: ")
        biblioteca.remover_livro(titulo)
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
# from livro import Livro