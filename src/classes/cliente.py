from classes.linhatelefonica import Linha
from classes.usuario import Usuario
class Cliente:
    def __init__(self, data_usuario : list | tuple, data_linha : list | tuple):
        """
        Inicializa um objeto da classe Usuario e um Linha com os dados fornecidos.
        """
        self.linha = Linha(data_linha)
        self.usuario = Usuario(data_usuario)
    def obter_dados(self):
        """
        Retorna os dados de um Cliente dentro de uma tupla
        """
        return self.usuario.obter_dados() + self.linha.obter_dados()