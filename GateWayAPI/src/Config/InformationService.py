urlEmployeeInfor = 'https://employee-infor.herokuapp.com'
urlEmployeeTask = 'https://employee-work.herokuapp.com'
urlEmployeeRequest = 'https://employee-request.herokuapp.com'
urlCompanyActivity = 'https://company-activity.herokuapp.com'
urlDeviceRequest = 'https://device-request.herokuapp.com'
from mysql.connector import (connection)
def connect():
    conn = connection.MySQLConnection(user='phap', password='phap123456',
                                     host='db-udpt.cxchfxjlshgb.ap-southeast-1.rds.amazonaws.com',
                                     port='3307',
                                     database='EmployeeInformation')
    return conn

