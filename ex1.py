import psycopg2


conn = psycopg2.connect(parametres)

parametres = {
    database = joancruz_DB,
    user = joancruz,
    password = 1234 ,
    host = localhost,
    port = 3031
}


cur = conn.cursor



print(cur)

