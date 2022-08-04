from src.Config import connectDatabase

class Department:
    id = 0
    departmentName = ''
    def getDepartment(self):
        return {
            'id':self.id,
            'departmentName':self.departmentName
        }

def listDepartment():
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListDepartment'
    cursor.callproc(procedure)
    data = []
    for result in cursor.stored_results():
        for temp in result.fetchall():
            department = Department()
            department.id = temp[0]
            department.departmentName = temp[1]
            data.append(department)
    cursor.close()
    conn.close()
    return data