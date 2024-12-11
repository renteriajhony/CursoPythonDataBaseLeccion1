import psycopg2

conexion = psycopg2.connect(user='postgres', password='postgres', host='localhost', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            # Recuperamos todos los valores de la tabla
            # sentencia = 'SELECT * FROM PUBLIC.PERSON'
            # cursor.execute(sentencia)
            # resultado = cursor.fetchall()
            # print(resultado)

            #Recuperamos solo un registro
            # sentencia = 'SELECT id_person, name, last_name, email FROM PUBLIC.PERSON WHERE id_person = 1'
            # cursor.execute(sentencia)
            # resultado = cursor.fetchone()
            # print(resultado)

            #Recuperamos solo un registro
            sentencia = 'SELECT id_person, name, last_name, email FROM PUBLIC.PERSON WHERE id_person = %s'
            my_value_var = int (input('Ingresa el id de la persona: '))
            cursor.execute(sentencia, (my_value_var,))
            resultado = cursor.fetchone()
            print(resultado)


except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    conexion.close()