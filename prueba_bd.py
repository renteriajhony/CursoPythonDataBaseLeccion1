import psycopg2

conexion = psycopg2.connect(user='postgres', password='postgres', host='localhost', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM PUBLIC.PERSON'
            cursor.execute(sentencia)
            resultado = cursor.fetchall()
            print(resultado)
            cursor.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    conexion.close()