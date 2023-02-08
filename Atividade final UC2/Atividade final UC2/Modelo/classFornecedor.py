class Fornecedor:
    def __init__(self,id,nome,cnpj):
        self._id = id
        self._nome = nome
        self._cnpj = cnpj

    def imprimirFornecedor(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        CNPJ - {self._cnpj}
        ''')

    def consultarFornecedorPorID(self):

        sql = f'''
        SELECT * FROM "Fornecedor"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def consultarCompras(self):
        sql = f'''
        SELECT * FROM "Compras"
        WHERE "ID_Fornecedor" = '{self._id}
        '''
        return sql

    def inserirFFornecedor(self):
        sql = f'''
        INSERT INTO "Fornecedor"
        VALUES(default,'{self._nome}','{self._cnpj}')
        '''
        return sql
        