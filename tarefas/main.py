from datetime import date
from tarefa import Tarefa
from gerenciador import GerenciadorDeTarefas

gerenciador = GerenciadorDeTarefas()

# Criando algumas tarefas
t1 = Tarefa("Estudar POO", "Revisar herança e polimorfismo", date(2025, 4, 20), "Estudos")
t2 = Tarefa("Pagar contas", "Energia e água", date(2025, 4, 15), "Financeiro")
t3 = Tarefa("Academia", "Treino de pernas", date(2025, 4, 16), "Saúde")

# Adicionando
gerenciador.adicionar_tarefa(t1)
gerenciador.adicionar_tarefa(t2)
gerenciador.adicionar_tarefa(t3)

# Listando todas
print("📋 Todas as tarefas:")
gerenciador.listar_tarefas()

# Listar por categoria
print("\n📂 Tarefas da categoria 'Estudos':")
gerenciador.listar_tarefas("Estudos")

# Marcar uma como concluída
gerenciador.marcar_como_concluida("Estudar POO")

# Listar vencidas
print("\n⏰ Tarefas vencidas:")
gerenciador.listar_vencidas()
