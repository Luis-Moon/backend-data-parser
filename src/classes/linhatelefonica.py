class Linha:
    def __init__(self, dados):
        """
        Inicializa um objeto da classe Linha com os dados fornecidos.
        """
        telefone, plano = dados
        self.telefone = telefone
        self.plano = plano
    def obter_dados(self):
        """
        Retorna os dados de um objeto Linha dentro de uma tupla
        """
        return self.telefone, self.plano