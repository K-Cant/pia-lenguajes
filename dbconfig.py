import pymysql

def getDBConnection():
    connection = pymysql.connect(
        host='mysql',         
        user='root',    
        port=30278,
        password = 'password1',
        database = 'PIA'
    )
    return connection
