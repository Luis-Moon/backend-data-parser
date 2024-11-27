import pytest
from src.services.processador import Processador

def test_processar_com_split():
    dados = ["Bob, bob@xyzzzzzz.com, Rua 12 de Abril, +5500000000000, 40GB"]
    processador = Processador()
    resultado = processador.processar(dados, tipo_filtro="split")
    assert resultado == [["Bob", "bob@xyzzzzzz.com", "Rua 12 de Abril", "+5500000000000", "40GB"]]

def test_processar_com_regex():
    dados = ["Alice, alice@xyzzzzzz.com, Rua Brasil, +5500111111111, 10GB"]
    processador = Processador()
    resultado = processador.processar(dados, tipo_filtro="regex")
    assert resultado == [("Alice", "alice@xyzzzzzz.com", "Rua Brasil", "+5500111111111", "10GB")]

def test_processar_lista_vazia():
    dados = []
    processador = Processador()
    resultado = processador.processar(dados, tipo_filtro="split")
    assert resultado == []


