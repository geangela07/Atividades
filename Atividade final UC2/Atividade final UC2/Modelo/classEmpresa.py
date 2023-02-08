class Empresa:
    def __init__(self,id,nome,cnpj,endereco):
        self._id = id
        self._nome = nome
        self._cnpj = cnpj
        self._endereco = endereco

    def imprimirEmpresa(self):
        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        CNPJ - {self._cnpj}
        ''')

    def consultarEmpresaPorID(self):
        sql = f'''
        SELECT * FROM "Empresa"
        WHERE "ID" = '{self._id}
        '''
        return sql

    def consultarCompras(self):
        sql = f'''
        SELECT * FROM "Compras"
        WHERE "ID_Empresa" = '{self._id}'
        '''
        return sql

    def inserirEmpresa(self):
        sql = f'''
        INSERT INTO "Empresa"
        VALUES(default,'{self._nome}','{self._cnpj}')

        '''
        return sql