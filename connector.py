from PyQt5.QtSql import QSqlDatabase, QSqlQuery


# Function for connection to MsSQL.
def connect():
    conn = QSqlDatabase.addDatabase("QODBC")
    conn.setDatabaseName('DRIVER={SQL Server};'
                          'SERVER=WIN-G20TG01SDBK;'
                          'DATABASE=Trade Statistics;')
    if conn.open():
        print("--------------------->open DB success.")
    else:
        print("Error")
    return conn


# Function for cities displaying.
def get_cities_from_sql(conn, city=''):
    cursor = QSqlQuery()
    text = '''
    Select TOP 100 Schedule.id, Schedule.departure as 'Отправка', Schedule.arrival as 'Прибытие', 
    City_route.arrival as 'Город отправки',City_route.destination as 'Город прибытия' 
    From Schedule JOIN City_route ON Schedule.fkey_cities = City_route.id 
    Where City_route.arrival = '{}'
    '''.format(city.upper())

    print(cursor.exec(text))
    return cursor
