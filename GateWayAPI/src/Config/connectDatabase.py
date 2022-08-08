from mysql.connector import (connection)
def connect():
    conn = connection.MySQLConnection(user='sql6503851', password='ZnymiZ3f13',
                                     host='sql6.freemysqlhosting.net',
                                     port='3306',
                                     database='sql6503851')
    return conn