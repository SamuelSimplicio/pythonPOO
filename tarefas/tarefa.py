from dataclasses import dataclass
from datetime import date

@dataclass
class Tarefa:
    titulo: str
    descricao: str
    data_vencimento: date
    categoria: str
    concluida: bool = False

    def exibir(self):
        status = "✔️ Concluída" if self.concluida else "⏳ Pendente"
        return (
            f"Título: {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Data de Vencimento: {self.data_vencimento}\n"
            f"Categoria: {self.categoria}\n"
            f"Status: {status}\n"
        )
