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
