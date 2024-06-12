import psycopg2


#Implementar la funció per crear un registre a la taula de l’exercici anterior.

#Recordatori: INSERT INTO…


cur = conn.cursor()


sql_insert = INSERT INTO nom_lliure {
    id, camp_1, camp_2,camp_3, camp4 (s%, s%, s%, s%, s%) (3,nom1,nom2,nom3,45)
}


cur.execute(sql_insert)


conn.commit()
