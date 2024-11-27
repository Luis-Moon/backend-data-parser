import pytest
from src.classes.usuario import Usuario
from src.classes.linhatelefonica import Linha
from src.classes.cliente import Cliente

def test_usuario():
    dados = ["Bob", "bob@xyzzzzzz.com", "Rua 12 de Abril"]
    usuario = Usuario(dados)
    assert usuario.nome == "Bob"
    assert usuario.email == "bob@xyzzzzzz.com"
    assert usuario.endereco == "Rua 12 de Abril"
    assert usuario.obter_dados() == ("Bob", "bob@xyzzzzzz.com", "Rua 12 de Abril")

def test_linha():
    dados = ["+5500000000000", "40GB"]
    linha = Linha(dados)
    assert linha.telefone == "+5500000000000"
    assert linha.plano == "40GB"
    assert linha.obter_dados() == ("+5500000000000", "40GB")

def test_cliente():
    dados_usuario = ["Alice", "alice@xyzzzzzz.com", "Rua Brasil"]
    dados_linha = ["+5500111111111", "10GB"]
    cliente = Cliente(dados_usuario, dados_linha)

    assert cliente.usuario.nome == "Alice"
    assert cliente.usuario.email == "alice@xyzzzzzz.com"
    assert cliente.usuario.endereco == "Rua Brasil"
    assert cliente.linha.telefone == "+5500111111111"
    assert cliente.linha.plano == "10GB"
    assert cliente.obter_dados() == (
        "Alice", "alice@xyzzzzzz.com", "Rua Brasil",
        "+5500111111111", "10GB"
    )
