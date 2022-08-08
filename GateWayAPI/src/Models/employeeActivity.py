from src.Config import connectDatabase

class EmployeeActivity:
    def __init__(self):
        id = 0
        idEmployee = 0
        idActivity = 0
        type = ''
        active = ''
    def getEmployeeActivity(self):
        return{
            'id':self.id,
            'idEmployee':self.idEmployee,
            'idActivity':self.idActivity,
            'type':self.type,
            'active':self.active
        }
    def insertFollowInformation(self, idEmployee, idActivity):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        procedure = 'InsertFollowActivity'
        cursor.callproc(procedure, [idEmployee, idActivity,])
        cursor.close()
        conn.close()
        return
    def insertRegisterInformation(self, idEmployee, idActivity):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        procedure = 'InsertRegisterActivity'
        cursor.callproc(procedure, [idEmployee, idActivity,])
        cursor.close()
        conn.close()
        return
    