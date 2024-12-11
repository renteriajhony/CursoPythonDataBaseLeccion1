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
            # sentencia = 'SELECT id_person, name, last_name, email FROM PUBLIC.PERSON WHERE id_person = %s'
            # my_value_var = int (input('Ingresa el id de la persona: '))
            # cursor.execute(sentencia, (my_value_var,))
            # resultado = cursor.fetchone()
            # print(resultado)

            # uso de fetchAll
            # sentencia = 'SELECT id_person, name, last_name, email FROM PUBLIC.PERSON WHERE id_person IN %s'
            # # primary_keys = ((1,2,),)
            # entrada = input('Ingresa id \'s a buscar (separados por comas, Ej: 1,2,3): ')
            # primary_keys = (tuple(entrada.split(',')),)
            # cursor.execute(sentencia, primary_keys)
            # resultado = cursor.fetchall()
            # for registro in resultado:
            #     print(registro)

            # #Insertar un registro
            # sentencia = 'INSERT INTO PUBLIC.PERSON(name,last_name,email) VALUES (%s,%s, %s)'
            # valores = ('Luis2', 'Diaz2', 'ldiaz2@mail.com')
            # cursor.execute(sentencia, valores)
            # # conexion.commit() Se utiliza cuando abrimos conexion sin with
            # registers = cursor.rowcount
            # print(f'Registros insertados {registers}')

            # Insertar varios registros
            # sentencia = 'INSERT INTO PUBLIC.PERSON(name,last_name,email) VALUES (%s,%s, %s)'
            # valores = (
            #     ('Jhony', 'Renteria', 'jrenteria@mail.com'),
            #     ('Pedro', 'Martinez', 'pmartinez@mail.com'),
            #     ('Ana', 'Rios', 'arios@mail.com')
            # )
            # cursor.executemany(sentencia, valores)
            # registers = cursor.rowcount
            # print(f'Registros insertados:  {registers}')

            # Actualizar registros
            # sentencia = 'UPDATE PUBLIC.PERSON SET name=%s, last_name=%s, email=%s WHERE id_person =%s'
            # valores = ('JhonyEEE', 'RenteriaA', 'jrenteria@mail.com.CO',1)
            # cursor.execute(sentencia, valores)
            # registers = cursor.rowcount
            # print(f'Registro Actualizado:  {registers}')

            # Actualizar Multiples registros
            sentencia = 'UPDATE PUBLIC.PERSON SET name=%s, last_name=%s, email=%s WHERE id_person =%s'
            valores = (
                ('Jhony', 'Renteria', 'jrenteria@mail.com',1),
                ('Pedro', 'Maturana', 'pmaturana@mail.com',2),
                ('Ana', 'Rios', 'arios@mail.com', 3)
            )
            cursor.executemany(sentencia, valores)
            registers = cursor.rowcount
            print(f'Registros Actualizados:  {registers}')

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    conexion.close()