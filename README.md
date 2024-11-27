# Projeto de Gerenciamento de Usuários e Linhas Telefônicas

Este projeto simula a manipulação de dados para sistemas de telecomunicações, organizando informações de usuários e suas respectivas linhas telefônicas em dois objetos distintos, utilizando uma arquitetura modular e orientada a objetos. 

---

## 🎯 **Descrição**
O programa processa uma lista de dados brutos contendo informações de clientes (nome, e-mail, endereço, telefone e plano) e organiza essas informações em instâncias de classes `Usuario` e `Linha` e as armazena em um objeto `Cliente`, permitindo:
- Criação e manipulação de objetos `Cliente`, `Usuario` e `LinhaTelefonica`.
- Armazenamento de clientes em um container (`GerenciadorClientes`).
- Processamento flexível de dados com diferentes métodos de filtragem (split e regex).
- Exibição de dados formatados no formato especificado.

---

## 🚀 **Como Executar**
### 1. Pré-requisitos
Certifique-se de que você tenha instalado:
- Python 3.10 ou superior

### 2. Instalação
Clone este repositório:
   ```
   git clone https://github.com/Luis-Moon/backend-data-parser.git
   cd backend-data-parser
   ```


### 3. Execução
No diretório raiz do projeto, execute o arquivo `main.py`:
```
python src/main.py
```

### 4. Saída Esperada
Ao executar o programa, você deve ver algo assim:
```
O cliente, Bob, com email, bob@xyzzzzzz.com, morador do endereço, Rua 12 de Abril, dono da linha, +5500000000000 com plano contratado de 40GB
O cliente, Alice, com email, alice@xyzzzzzz.com, morador do endereço, Rua Brasil, dono da linha, +5500111111111 com plano contratado de 10GB
```

---

## 📜 **Funcionalidades**
1. **Processador de Dados**
   - Classe: `Processador` (`services/processador.py`)
   - Métodos:
     - `processar`: Processa os dados brutos, permitindo o uso de filtros baseados em `split` ou expressões regulares.

2. **Gerenciador de Clientes**
   - Classe: `GerenciadorClientes` (`services/gerenciador.py`)
   - Funcionalidades:
     - Armazena objetos `Cliente` em uma lista.
     - Métodos para adicionar, listar, e limpar clientes.
     - Executa funções lambda em cada cliente.

3. **Modelo de Domínio**
   - **`Usuario` (`classes/usuario.py`)**
     - Representa os dados de um cliente: nome, e-mail e endereço.
   - **`Linha` (`classes/linhatelefonica.py`)**
     - Representa os dados de uma linha telefônica: número e plano.
   - **`Cliente` (`classes/cliente.py`)**
     - Combina `Usuario` e `Linha` em um único objeto.

4. **Funções Auxiliares**
   - Arquivo: `services/funcs_auxiliares.py`
   - Exibe os dados formatados no formato especificado.

---
## 📊 **Executando Testes Unitários**

Para executar os testes unitários localizados na pasta `/test/`, siga os passos abaixo:

1. Instale o `pytest` utilizando o `pip`:
    ```
    pip install pytest
    ```

2. No terminal, navegue até a raiz do projeto.

3. Execute o `pytest`:
    ```
    pytest
    ```

Esses comandos rodarão todos os testes unitários encontrados na pasta `/test/`.

---

## 💭 **Futuras Possibilidades**
   - Devido a estrutura `GerenciadorClientes` a possibilidade de migração para bancos sql seria simples


## 📝 **Autor**
| [<img src="https://avatars.githubusercontent.com/u/72164903?s=400&u=2a35fe5b04036cc0cc68ee7456936b32fa5a5588&v=4" width=115><br><sub>Luis Felipe Hilário Carmona</sub>](https://github.com/Luis-Moon) | 
| :---: |