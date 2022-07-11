from src.Config import connectDatabase

class Employee:
    def __init__(self):
        self.id = 0
        self.idManager = 0
        self.idDepartment = 0
        self.idEmployee = 0
        self.firstName = ''
        self.lastName = ''
        self.dayOfBirth = ''
        self.gender = ''
        self.email = ''
        self.phoneNumber = ''
        self.address = ''
        self.maritalStatus = ''
        self.position = ''
        self.active = ''
    def getEmployee(self):
        return{
            'id':self.id,
            'idManager':self.idManager,
            'idDepartment':self.idDepartment,
            'idEmployee':self.idEmployee,
            'firstName':self.firstName,
            'lastName':self.lastName,
            'dayOfBirth':self.dayOfBirth,
            'gender':self.gender,
            'email':self.email,
            'phoneNumber':self.phoneNumber,
            'address':self.address,
            'maritalStatus':self.maritalStatus,
            'position':self.position,
            'active':self.active
        }

def employeeInfor():
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    query = ('SELECT * FROM Employee WHERE id = 1')
    cursor.execute(query)
    data = []
    for t in cursor:
        emp = Employee()
        emp.id = t[0]
        emp.idManager = t[1]
        emp.idDepartment = t[2]
        emp.idEmployee = t[3]
        emp.firstName = t[4]
        emp.lastName = t[5]
        emp.dayOfBirth = t[6]
        emp.gender = t[7]
        emp.email = t[8]
        emp.phoneNumber = t[9]
        emp.address = t[10]
        emp.maritalStatus = t[11]
        emp.position = t[12]
        emp.active = t[13]
        data.append(emp)
    cursor.close()
    conn.close()
    return data