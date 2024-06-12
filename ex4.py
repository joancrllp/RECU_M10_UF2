import psycopg2





cur = conn.cursor()


sql_read = SELECT * FROM nom_lliure

result = cur.fetchAll(sql_read)
    

for i in result:
    print("L'ID es:", i[0])
    print("El primer camp es:", i[1])
    print("El segon cap es:", i[2])
    print("El tercer cap es:", i[3])    
    print("L'int es:", i[4])
