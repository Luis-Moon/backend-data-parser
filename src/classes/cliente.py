from linhatelefonica import Linha
from usuario import Usuario
class Cliente:
    def __init__(self, data_usuario : list | tuple, data_linha : list | tuple):
        self.linha = Linha(data_linha)
        self.usuario = Usuario(data_usuario)