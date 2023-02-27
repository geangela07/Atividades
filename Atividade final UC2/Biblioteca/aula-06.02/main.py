import psycopg2
from Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
from Modelo.classLivro import Livro




def inserirCliente():
    cursor = con.cursor()

    nomeCliente = input("Insira o nome do cliente: ")
    cpfCliente = input("Insira o CPF do Cliente: ")

    cursor.execute(f'''
    INSERT INTO "Cliente"
    VALUES (default, '{nomeCliente}','{cpfCliente}')
    
    ''')
    con.commit()

    cursor.close()

def inserirAluguel():

    cursor = con.cursor()

    idCliente = input("Insira o ID do Cliente: ")

    idLivro = input("Insira o Id do Livro: ")

    cursor.execute(f'''
    INSERT INTO "Aluguel"
    VALUES(default, '{idCliente}', '{idLivro}',default)
    ''')

    con.commit()
    cursor.close()

def inserirLivro():
    cursor = con.cursor()

    nomeLivro = input("Insira o nome do Livro: ")

    nomeAutor = input("Insira o autor do Livro: ")

    cursor.execute(f'''
    INSERT INTO "Livro"
    VALUES(default, '{nomeLivro}', '{nomeAutor}')
    ''')

    con.commit()
    cursor.close()

def verListaCliente():
    cursor = con.cursor()

    cursor.execute(f'''
    SELECT * FROM "Cliente"
    ORDER BY "ID" ASC
    ''')

    resultado = cursor.fetchall()
    for r in resultado:
        print(f'''
        ID - {r[0]}
        Nome - {r[1]}
        CPF - {r[2]}
        ''')

    cursor.close()

def verListaLivro():
    cursor = con.cursor()

    cursor.execute(f'''
    SELECT * FROM "Livro"
    ORDER BY "ID" ASC
    ''')

    resultado = cursor.fetchall()
    for r in resultado:
        print(f'''
        ID - {r[0]}
        Nome - {r[1]}
        Autor - {r[2]}
        ''')


    cursor.close()

def verListaAluguel():
    cursor = con.cursor()

    cursor.execute(f'''
    SELECT * FROM "Aluguel"
    ORDER BY "ID" ASC
    ''')
    resultado = cursor.fetchall()
    for r in resultado:
        print(f'''
        ID - {r[0]}
        ID Cliente - {r[1]}
        ID Livro - {r[2]}
        Data Aluguel - {r[3]}
        ''')

    
    cursor.close()

def atualizarCliente():
    cursor = con.cursor()
    novoCliente = input("Digite o ID do Cliente que deseja atualizar: ")

    cursor.execute(f'''
    SELECT * FROM "Cliente"
    WHERE "ID" = {novoCliente}
    ''')
    print("Cliente escolhido: ")
    resultado = cursor.fetchone()
    print(f'''
        ID - {resultado[0]}
        Nome - {resultado[1]}
        CPF - {resultado[2]}
        ''')
    
    cursor.close()

    cursor = con.cursor()

    novoNome = input("Insira o novo nome do Cliente:")
    novoCPF = input("Insira o novo cpf do Cliente:")

    cursor.execute(f'''
    UPDATE "Cliente"
    SET "Nome" = '{novoNome}', "CPF" = '{novoCPF}'
    WHERE "ID" = '{novoCliente}'
    ''')
    con.commit()

    cursor.close()


def removerCliente():
    cursor = con.cursor()
    apagarCliente = input("Digite o Id do Cliente que deseja remover: ")

    cursor.execute(f''' 
    DELETE FROM "Cliente"
    WHERE "ID" = {apagarCliente}
    ''')

    
    con.commit()
    cursor.close()




def verClienteEspecifico():
    cursor = con.cursor()
    clienteEspecifico = input("Digite o ID do Cliente que deseja ver: ")

    cursor.execute(f'''
    SELECT * FROM "Cliente"
    WHERE "ID" = {clienteEspecifico}
    ''')
    print("Cliente escolhido: ")
    resultado = cursor.fetchone()
    print(f'''
        ID - {resultado[0]}
        Nome - {resultado[1]}
        CPF - {resultado[2]}
        ''')
    cursor.close()




try:
    con = psycopg2.connect(database ="BibliotecaNova",host="localhost",port="5432",user="postgres",password="postgres")



except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro -", error) 
    

while True:
    try:


        print(''' 
        1. Ver lista de Clientes
        2. Ver lista de Alugueis
        3. Ver lista de Livros
        4. Inserir novo Aluguel
        5. Inserir novo Cliente
        6. Inserir novo Livro
        7. Atualizar Cliente
        8. Remover Cliente
        9. Ver Cliente espécifico
        0. Sair
        ''')
            
        opcoes = input("Escolha uma opção:")

        match opcoes:

            case "1":
                verListaCliente()

            case "2":
                verListaAluguel()

            case "3":
                verListaLivro()

            case "4":
                inserirAluguel()

            case "5":
                inserirCliente()

            case "6":
                inserirLivro()

            case "7":
                atualizarCliente()

            case "8":
                removerCliente()

            case "9":
                verClienteEspecifico()

            case "0":
                con.close()
                break

            case _:
                print("Opção inválida")

        input("Tecle Enter para continuar")

    except (Exception,psycopg2.Error) as error:
        print("Ocorreu um erro",error)



    
            


