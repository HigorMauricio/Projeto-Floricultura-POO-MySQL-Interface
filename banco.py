import mysql.connector
def criar_conexao(host, usario, senha, banco):
    return mysql.connector.connect(host=host, user=usario, password=senha, database=banco)

def fechar_conexao(con):
    con.close()

def inserir_dados(nome, cor):
    con = criar_conexao('localhost', 'root', '', 'floriculturadados')
    cursor = con.cursor()
    sql = 'insert into flores (nome, cor) values (%s, %s)'
    valores = (nome, cor)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()
    fechar_conexao(con)

def deletar_dados(nome, cor):
    con = criar_conexao('localhost', 'root', '', 'floriculturadados')
    cursor = con.cursor()
    sql = 'delete from flores where nome=%s and cor=%s limit 1'
    valores = (nome, cor)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()
    fechar_conexao(con)

def mostarar_flores():
    con = criar_conexao('localhost', 'root', '', 'floriculturadados')
    cursor = con.cursor()
    sql = 'select * from flores order by nome, cor'
    cursor.execute(sql)
    res = cursor.fetchall()
    con.close()
    return res
