from categoria import Categoria
from transacao import Transacao

LISTA_CATEGORIAS = []
LISTA_TRANSACOES = []
# Lista de categorias e transações

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)
    LISTA_CATEGORIAS.append(nova_categoria)
    # Adiciona nova categoria à lista de categorias

    return nova_categoria


def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(
        descricao=descricao,
        valor=valor,
        categoria=categoria,
    )
    LISTA_TRANSACOES.append(nova_transacao)
    # Adiciona nova transação à lista de transações
    return nova_transacao

def saldo_total():
    total = 0.0
    # Inicializa o saldo total como 0.0
    for t in LISTA_TRANSACOES:
        total += t.valor
        # Adiciona o valor de cada transação ao saldo total
    
    return total