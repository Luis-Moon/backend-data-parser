import pytest
from src.services.gerenciador import GerenciadorClientes
from src.classes.cliente import Cliente

def test_criar_clientes():
    dados = [
        ["Bob", "bob@xyzzzzzz.com", "Rua 12 de Abril", "+5500000000000", "40GB"],
        ["Alice", "alice@xyzzzzzz.com", "Rua Brasil", "+5500111111111", "10GB"]
    ]
    gerenciador = GerenciadorClientes()
    gerenciador.criar_clientes(dados)

    assert len(gerenciador.obter_clientes()) == 2

def test_adicionar_cliente():
    dados_cliente = ["Bob", "bob@xyzzzzzz.com", "Rua 12 de Abril", "+5500000000000", "40GB"]
    gerenciador = GerenciadorClientes()
    gerenciador.adicionar_cliente(dados_cliente)

    clientes = gerenciador.obter_clientes()
    assert len(clientes) == 1
    assert clientes[0].usuario.nome == "Bob"

def test_deletar_todos():
    dados = [
        ["Bob", "bob@xyzzzzzz.com", "Rua 12 de Abril", "+5500000000000", "40GB"],
        ["Alice", "alice@xyzzzzzz.com", "Rua Brasil", "+5500111111111", "10GB"]
    ]
    gerenciador = GerenciadorClientes()
    gerenciador.criar_clientes(dados)
    gerenciador.deletar_todos()

    assert len(gerenciador.obter_clientes()) == 0

def test_executar_lambda():
    dados = [
        ["Bob", "bob@xyzzzzzz.com", "Rua 12 de Abril", "+5500000000000", "40GB"]
    ]
    gerenciador = GerenciadorClientes()
    gerenciador.criar_clientes(dados)

    def lambda_exemplo(cliente):
        assert cliente.usuario.nome == "Bob"
    
    gerenciador.executar_lambda(lambda_exemplo)
