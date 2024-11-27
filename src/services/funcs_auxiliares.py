from classes.cliente import Cliente

def print_dados_cliente(cliente : Cliente):
    nome, email, endereco, telefone, plano = cliente.get_dados()
    print(f"O cliente, {nome}, com eamil; {email}, morador do endereço, {endereco}, dono da linha, {telefone} com plano contratado de {plano}")