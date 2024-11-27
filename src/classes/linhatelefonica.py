class Linha:
    def __init__(self, dados):
        telefone, plano = dados
        self.telefone = telefone
        self.plano = plano
    def obter_dados(self):
        return self.telefone, self.plano