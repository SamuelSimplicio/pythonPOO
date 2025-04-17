from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    ano: int
    editora: str

    def exibir(self):
        return f"{self.titulo} - {self.autor} ({self.ano}) - {self.editora}"