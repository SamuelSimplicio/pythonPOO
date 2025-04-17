from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao: # representa uma transação financeira
    descricao: str
    valor: float
    categoria: Categoria

    def exibir(self):
        print(
            f"DESCRICAO: {self.descricao} VALOR {self.valor} CATEGORIA {self.categoria.nome}"
        )