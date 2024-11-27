from classes.cliente import Cliente
class  GerenciadorClientes:
    def __init__(self):
        """
        Inicializa um container de Clientes
        """
        self.clientes = []
    def criar_clientes(self, dados : list):
        """
        Itera sobre lista de dados de clientes os adicionando ao container
        """
        for dados_cliente in dados:
            self.adicionar_cliente(dados_cliente )
    def adicionar_cliente(self,dados_cliente):
        """
        Usando se dos dados de um cliente, cria-se objeto Cliente e armazena em container
        """
        self.clientes.append(Cliente(dados_cliente[0:3],dados_cliente[3:]))
    def deletar_todos(self):
        """
        Deleta todos os clientes do container
        """
        self.clientes.clear()
    def obter_clientes(self):
        """
        Retorna todos os clientes do container
        """
        return self.clientes
    def executar_lambda(self, lambda_func):
        """
        Executa uma função lambda sobre todos os clientes do container
        """
        for cliente in self.obter_clientes():
            lambda_func(cliente)