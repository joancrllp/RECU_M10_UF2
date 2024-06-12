import psycopg2

cur = conn.cursor()
sql =  CREATE TABLE nom_lliure (
            id SERIAL PRIMARY KEY,
            camp1 VARCHAR(255) NOT NULL,
            camp2 VARCHAR(255) NOT NULL,
            camp3 VARCHAR(255) NOT NULL,
            camp4 BIGINT NOT NULL
        );
        


cur.execute(sql)   
cur.commit()
