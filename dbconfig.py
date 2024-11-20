import pymysql
import cryptography

def getDBConnection():
    connection = pymysql.connect(
        host='mysql',         
        user='root',    
        port=3306,
        password = 'password1',
        database = 'PIA'
    )
    return connection

def create_tables():
    connection = getDBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id int auto_increment primary key, username varchar(255) not null, email text not null, password_user text not null)")
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
