import psycopg2 as bd

conexion = bd.connect(user='postgres', password='postgres', host='localhost', port='5432', database='test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO PUBLIC.PERSON(name,last_name,email) VALUES (%s,%s, %s)'
    valores = (
        ('Maria', 'Renteria', 'mrenteria@mail.com'),
        ('Camila', 'Martinez', 'cmartinez@mail.com')
    )
    cursor.executemany(sentencia, valores)
    conexion.commit()
    print('Termina la transaction')

except Exception as error:
    conexion.rollback()
    print(f'Ocurrio un error se realiza rollBack de la transaccion: {error}')
finally:
    conexion.close()