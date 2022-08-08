from src.Config import InformationService

class Account:
    def __init__(self):
        self.id = 0
        self.idRole = 0
        self.idEmployee = 0
        self.username = ''
        self.password = ''
        self.active = ''
    def getAccount(self):
        return{
            'id':self.id,
            'idRole':self.idRole,
            'idEmployee':self.idEmployee,
            'username':self.username,
            'password':self.password,
            'active':self.active
        }

def checkLogin(username, password):
    conn = InformationService.connect()
    Countcursor = conn.cursor()
    queryCount = ('SELECT COUNT(*) FROM Account WHERE username = {} AND password = {}'.format(username, password))
    Countcursor.execute(queryCount)
    record = Countcursor.fetchone()
    count = record[0]
    Countcursor.close()
    if(count==0):
        return 0

    idcursor = conn.cursor()
    queryid = ('SELECT idRole,idEmployee FROM Account WHERE username = {} AND password = {}'.format(username, password))
    idcursor.execute(queryid)
    record = idcursor.fetchone()
    idRole = record[0]
    idEmployee = record[1]
    idcursor.close()

    query = ('SELECT roleName FROM Role WHERE id = {}'.format(idRole))
    cursor = conn.cursor()
    cursor.execute(query)
    record = cursor.fetchone()
    roleName = record[0]
    cursor.close()

    data = {
        "roleName":roleName,
        "idEmployee":idEmployee,
        "username":username,
        "password":password
        }

    conn.close()
    return data