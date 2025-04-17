from tarefa import Tarefa
from datetime import datetime

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self,categoria: str  =None):
        tarefas_filtradas = self.tarefas if categoria is None else[
            tarefa for tarefa in self.tarefas if tarefa.categoria == categoria
            ]
        for tarefa in tarefas_filtradas:
            print(tarefa.exibir())

    def marcar_como_concluida(self, titulo: str):
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == titulo.lower():
                tarefa.concluida = True
                print(f"Tarefa '{titulo}' marcada como concluída.")
                return
        print(f"Tarefa '{titulo}' não encontrada.")


    def listar_vencidas(self):
        hoje = datetime.today()
        for tarefa in self.tarefas:
            if tarefa.data_vencimento < hoje and not tarefa.concluida:
                print("VENCIDA")
                print(tarefa.exibir())

