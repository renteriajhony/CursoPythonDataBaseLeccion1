import psycopg2 as bd

conexion = bd.connect(user='postgres', password='postgres', host='localhost', port='5432', database='test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO PUBLIC.PERSON(name,last_name,email) VALUES (%s,%s, %s)'
    valores = (
        ('Jhony', 'Renteria', 'jrenteria@mail.com'),
        ('Pedro', 'Maturana', 'pmaturana@mail.com'),
        ('Ana', 'Rios', 'arios@mail.com')
    )
    cursor.executemany(sentencia, valores)

    sentencia = 'UPDATE PUBLIC.PERSON SET name=%s, last_name=%s, email=%s WHERE id_person =%s'
    valores = (
        ('Jhony', 'Renteria', 'jrenteria@mail.com.co', 1),
        ('Pedro', 'Maturana', 'pmaturana@mail.com.co', 2),
        ('Ana', 'Rios', 'arios@mail.com.co', 3)
    )
    cursor.executemany(sentencia, valores)
    conexion.commit()
    print('Termina la transaction')

except Exception as error:
    conexion.rollback()
    print(f'Ocurrio un error se realiza rollBack de la transaccion: {error}')
finally:
    conexion.close()