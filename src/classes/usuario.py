class Usuario:
    def __init__(self, dados):
        """
        Inicializa um objeto da classe Usuario com os dados fornecidos.
        """
        nome, email, endereco = dados
        self.nome = nome
        self.email = email
        self.endereco = endereco
    def obter_dados(self):
        """
        Retorna os dados de um Usuario dentro de uma tupla
        """
        return self.nome, self.email, self.endereco
    