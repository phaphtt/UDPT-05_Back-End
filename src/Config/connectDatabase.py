from mysql.connector import (connection)
def connect():
    conn = connection.MySQLConnection(user='phap', password='phap123456',
                                     host='db-udpt.cxchfxjlshgb.ap-southeast-1.rds.amazonaws.com',
                                     port='3307',
                                     database='EmployeeRequest')
    return conn