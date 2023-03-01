import psycopg2
from Controle.classConexao import Conexao
from Modelo.classEmpresa import Empresa
from Modelo.classFornecedor import Fornecedor




def inserirFornecedor():
    cursor = con.cursor()

    nomeFornecedor = input("Insira o nome do Fornecedor: ")

    cnpjFornecedor = input("Insira o CNPJ do Fornecedor: ")

    cursor.execute(f'''
    INSERT INTO "Fornecedor"
    VALUES (default, '{nomeFornecedor}','{cnpjFornecedor}')
    
    ''')
    con.commit()

    cursor.close()

def inserirEmpresa():

    cursor = con.cursor()

    nomeEmpresa = input("Insira o nome da Empresa: ")

    endereçoEmpresa = input("Insira o endereço da Empresa:")

    cnpjEmpresa = input("Insira o cnpj da Empresa:")

    cursor.execute(f'''
    INSERT INTO "Empresa"
    VALUES( default,'{nomeEmpresa}', '{cnpjEmpresa}','{endereçoEmpresa}')
    ''')

    con.commit()
    cursor.close()

def inserirCompra():
    cursor = con.cursor()

    idEmpresa = input("Insira o id da Empresa: ")

    idFornecedor = input("Insira o id do Fornecedor: ")

    cursor.execute(f'''
    INSERT INTO "Compra"
    VALUES( default,'{idEmpresa}', '{idFornecedor}',default)
    ''')

    con.commit()
    cursor.close()

def verListaEmpresa():
    cursor = con.cursor()

    cursor.execute(f'''
    SELECT * FROM "Empresa"
    ORDER BY "ID" ASC
    ''')

    resultado = cursor.fetchall()
    for r in resultado:
        print(f'''
        ID - {r[0]}
        Nome - {r[1]}
        CNPJ - {r[2]}
        ''')

    cursor.close()

def verListaFornecedor():
    cursor = con.cursor()

    cursor.execute(f'''
    SELECT * FROM "Fornecedor"
    ORDER BY "ID" ASC
    ''')

    resultado = cursor.fetchall()
    for r in resultado:
        print(f'''
        ID - {r[0]}
        Nome - {r[1]}
        CNPJ - {r[2]}
        ''')


    cursor.close()

def verListaCompra():
    cursor = con.cursor()

    cursor.execute(f'''
    SELECT * FROM "Compra"
    ORDER BY "ID" ASC
    ''')
    resultado = cursor.fetchall()
    for r in resultado:
        print(f'''
        ID - {r[0]}
        ID Empresa - {r[1]}
        ID Fornecedor - {r[2]}
        Data Compra - {r[3]}
        ''')

    
    cursor.close()

def atualizarFornecedor():
    cursor = con.cursor()
    novoFornecedor = input("Digite o ID do Fornecedor que deseja atualizar: ")

    cursor.execute(f'''
    SELECT * FROM "Fornecedor"
    WHERE "ID" = {novoFornecedor}
    ''')
    print("Fornecedor Escolhido: ")
    resultado = cursor.fetchone()
    print(f'''
        ID - {resultado[0]}
        Nome - {resultado[1]}
        CNPJ - {resultado[2]}
        ''')
    
    cursor.close()

    cursor = con.cursor()

    novoNome = input("Insira o novo nome do Fornecedor:")
    novoCNPJ = input("Insira o novo cnpj do Fornecedor:")

    cursor.execute(f'''
    UPDATE "Fornecedor"
    SET "Nome" = '{novoNome}', "CNPJ" = '{novoCNPJ}'
    WHERE "ID" = '{novoFornecedor}'
    ''')
    con.commit()

    cursor.close()


def removerCompra():
    cursor = con.cursor()
    apagarCompra = input("Digite o Id da Compra que deseja remover: ")

    cursor.execute(f''' 
    DELETE FROM "Compra"
    WHERE "ID" = {apagarCompra}
    ''')

    
    con.commit()
    cursor.close()




def verFornecedorEspecifico():
    cursor = con.cursor()
    fornecedorEspecifico = input("Digite o ID do Fornecedor que deseja ver: ")

    cursor.execute(f'''
    SELECT * FROM "Fornecedor"
    WHERE "ID" = {fornecedorEspecifico}
    ''')
    print("Fornecedor escolhido: ")
    resultado = cursor.fetchone()
    print(f'''
        ID - {resultado[0]}
        Nome - {resultado[1]}
        CNPJ - {resultado[2]}
        ''')
    cursor.close()




try:
    con = psycopg2.connect(database ="EmpresaAtc",host="localhost",port="5432",user="postgres",password="postgres")



except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro -", error) 
    

while True:
    try:


        print(''' 
        1. Ver lista de Empresas
        2. Ver lista de Fornecedores
        3. Ver lista de Compras
        4. Inserir novo Fornecedor
        5. Inserir nova Empresa
        6. Inserir nova Compra
        7. Atualizar Fornecedor
        8. Remover Compra
        9. Ver Fornecedor espécifico
        0. Sair
        ''')
            
        opcoes = input("Escolha uma opção:")

        match opcoes:

            case "1":
                verListaEmpresa()

            case "2":
                verListaFornecedor()

            case "3":
                verListaCompra()

            case "4":
                inserirFornecedor()

            case "5":
                inserirEmpresa()

            case "6":
                inserirCompra()

            case "7":
                atualizarFornecedor()

            case "8":
                removerCompra()

            case "9":
                verFornecedorEspecifico()

            case "0":
                con.close()
                break

            case _:
                print("Opção inválida")

        input("Tecle Enter para continuar")

    except (Exception,psycopg2.Error) as error:
        print("Ocorreu um erro",error)



    
            

