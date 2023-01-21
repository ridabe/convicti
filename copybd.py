import pandas as pd
import mysql.connector
from hashlib import sha256

cnx = mysql.connector.connect(
    host="127.0.0.1",
    database="sale_control",
    port=3306,
    user="root",
    password="root"
)

cur = cnx.cursor()

planilha = pd.read_excel('app/db/usuario.xlsx')
print(planilha)
for i, dados in enumerate(planilha["nivel"]):
    nome = planilha.loc[i, "nome"]
    unidadeid = planilha.loc[i, "unidadeid"]
    email = planilha.loc[i, "e-mail"]
    senha = "123mudar"
    nivel = planilha.loc[i, "nivel"]

    dados = (nome, int(unidadeid), email, senha, int(nivel))
    stmt_insert = "INSERT INTO usuario (nome, unidade_id, email, senha, nivel) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(stmt_insert, dados)
    cnx.commit()

# planilha = pd.read_excel('app/db/diretoria.xlsx')
# for i, dados in enumerate(planilha["diretor"]):
#     nome = planilha.loc[i, "nome"]
#     diretor_id = planilha.loc[i, "diretor"]
#
#     dados = (nome, int(diretor_id))
#     stmt_insert = "INSERT INTO diretoria (nome_diretoria,diretor_id) VALUES (%s, %s)"
#     cur.execute(stmt_insert, dados)
#     cnx.commit()
#
# planilha = pd.read_excel('app/db/unidade.xlsx')
# for i, dados in enumerate(planilha["gerenteid"]):
#     unidade = planilha.loc[i, "unidade"]
#     latlong= planilha.loc[i, "latlong"]
#     split = latlong.split(',')
#     lat = split[0]
#     long = split[1]
#     gerenteid = planilha.loc[i, "gerenteid"]
#     diretoriaid = planilha.loc[i, "diretoriaid"]
#
#     dados = (unidade, lat, long, int(gerenteid), int(diretoriaid))
#     stmt_insert = "INSERT INTO unidade (unidade,lat, lon, gerente_id, diretoria_id) VALUES (%s, %s, %s, %s, %s)"
#     cur.execute(stmt_insert, dados)
#     cnx.commit()

cnx.close()

