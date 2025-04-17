from transacoes.utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)

# CATEGORIAS
categoria_receita = cadastrar_categoria("Receita")
categoria_contas = cadastrar_categoria("Contas")
categoria_viagem = cadastrar_categoria("Viagem")

# tr
cadastrar_transacao(
    descricao="Salario",
    valor=5000,
    categoria=categoria_receita
)

cadastrar_transacao(
    descricao="Moradia",
    valor=-1500,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao="Bonus",
    valor=750,
    categoria=categoria_receita
)

cadastrar_transacao(
    descricao="Viagem",
    valor=-2000,
    categoria=categoria_viagem
)

saldo_total = saldo_total()
print(f"Saldo total: {saldo_total}")