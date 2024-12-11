import psycopg2

conexion = psycopg2.connect(user='postgres', password='postgres', host='localhost', port='5432', database='test_db')

cursor = conexion.cursor()
sentencia = 'SELECT * FROM PUBLIC.PERSON'
cursor.execute(sentencia)
resultado = cursor.fetchall()
print(resultado)
cursor.close()
conexion.close()