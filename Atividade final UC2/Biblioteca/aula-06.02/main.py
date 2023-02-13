import psycopg2
from Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
from Modelo.classLivro import Livro

def menuClientes(conexao):
    print("Lista de clientes")
    resultado = conexao.consultarBanco('''
    SELECT * FROM "Cliente"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")
    for cliente in resultado:
        print(f"{cliente[0]} | {cliente[1]}")

    print(f'''
    Escolha uma das opções:
    1. Ver cliente específico
    2. Inserir novo cliente
    0. Voltar para o menu principal
    ''')
    opcoes = input("Digite o número da opção desejada: ")
    match opcoes:
        case "1":
            while True:
                clienteID = input("Digite o ID do cliente")
                clienteEscolhido = Cliente(clienteID,None,None)
                resultado = conexao.consultarBanco(clienteEscolhido.consultarClientePorID())
                if resultado != []:
                    clienteEscolhido._nome = resultado[0][1]
                    clienteEscolhido._cpf = resultado[0][1]
                    clienteEscolhido.imprimirCliente()

                    while True:
                        print(f'''
                        Escolha uma das opções:
                        1. Ver alugueis
                        0. Voltar para o menu principal
                        ''')
                        opcoes = input("Digite o numero da opção: ")
                        match opcoes:
                            case "1":
                                print(f"Alugueis do Cliente {clienteEscolhido._nome}")
                                resultado = conexao.consultarBanco(clienteEscolhido.)


