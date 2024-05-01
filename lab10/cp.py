import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="suppliers", user="postgres",
                        password="Kraken@98", port=5432)
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)