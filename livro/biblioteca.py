from dataclasses import dataclass
from livro import Livro

class Biblioteca:
    def __init__(self): # Inicializa a biblioteca com uma lista vazia de livros
        self.livros = []

    def adicionar_livro(self, livro: Livro): # Adiciona um livro à biblioteca
        self.livros.append(livro)

    def exibir_livros(self): # Exibe todos os livros da biblioteca
        for livro in self.livros:
            print(livro.exibir())

    def buscar_livro(self, titulo: str): # Busca um livro pelo título
        # Retorna o livro se encontrado, caso contrário retorna None
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower(): # Comparação sem case sensitive
                return livro
        return None

    def remover_livro(self, titulo: str): # Remove um livro pelo título
        livro = self.buscar_livro(titulo)
        if livro:
            self.livros.remove(livro)
            print(f"Livro '{titulo}' removido com sucesso.")
        else:
            print(f"Livro '{titulo}' não encontrado na biblioteca.")