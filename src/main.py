from classes.cliente import Cliente
from services.processador import Processador
from services.gerenciador import GerenciadorClientes
from services.funcs_auxiliares import print_dados_cliente

data = [
"Bob, bob@xyzzzzzz.com, Rua 12 de Abril, +5500000000000, 40GB",
"Alice, alice@xyzzzzzz.com, Rua Brasil, +5500111111111, 10GB"
]


if __name__ == "__main__":
    data = Processador().processar(data)
    gerenciador = GerenciadorClientes()
    gerenciador.criar_clientes(data)
    gerenciador.executar_lambda(print_dados_cliente)