from src.Config import connectDatabase

class Employee:
    id = 0
    idManager = 0
    idDepartment = 0
    idEmployee = 0
    firstname = ''
    lastname = ''
    dayOfBirth = ''
    gender = ''
    email = ''
    phoneNumber = ''
    address = ''
    maritalStatus = ''
    position = ''
    active = ''
    departmentName=''
    def getInformation(self):
        return{
            'id':self.id,
            'idManager':self.idManager,
            'idDepartment':self.idDepartment,
            'idEmployee':self.idEmployee,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'dayOfBirth':self.dayOfBirth,
            'gender':self.gender,
            'email':self.email,
            'phoneNumber':self.phoneNumber,
            'address':self.address,
            'maritalStatus':self.maritalStatus,
            'position':self.position,
            'active':self.active,
            'departmentName':self.departmentName
        }
    def updateInformation(self, id, firstname, lastname, idDepartment, position, dayOfBirth, gender, email, phoneNumber, address, maritalStatus):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        procedure = 'UpdateEmployeeById'
        cursor.callproc(procedure, [id, firstname, lastname, idDepartment, position, dayOfBirth, gender, email, phoneNumber, address, maritalStatus,])
        cursor.close()
        conn.close()
        return

class EmployeeManager(Employee):
    manager_idEmployee = ''
    manager_firstname = ''
    manager_lastname = ''
    manager_gender = ''
    manager_idDepartment = 0
    manager_position = ''
    manager_email = ''
    manager_phoneNumber = ''
    manager_departmentName = ''
    def getInformation(self):
        return{
            'id':self.id,
            'idManager':self.idManager,
            'idDepartment':self.idDepartment,
            'idEmployee':self.idEmployee,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'dayOfBirth':self.dayOfBirth,
            'gender':self.gender,
            'email':self.email,
            'phoneNumber':self.phoneNumber,
            'address':self.address,
            'maritalStatus':self.maritalStatus,
            'position':self.position,
            'active':self.active,
            'manager_idEmployee':self.manager_idEmployee,
            'manager_firstname':self.manager_firstname,
            'manager_lastname':self.manager_lastname,
            'manager_gender':self.manager_gender,
            'manager_idDepartment':self.manager_idDepartment,
            'manager_position':self.manager_position,
            'manager_email':self.manager_email,
            'manager_phoneNumber':self.manager_phoneNumber,
            'manager_departmentName':self.manager_departmentName
        }

def employeeInfor(id):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'GetInforEmployeeById'
    cursor.callproc(procedure, [id,])
    for result in cursor.stored_results():
        emp = EmployeeManager()
        temp = result.fetchall()[0]
        emp.id = temp[0]
        emp.idManager = temp[1]
        emp.idDepartment = temp[2]
        emp.idEmployee = temp[3]
        emp.firstname = temp[4]
        emp.lastname = temp[5]
        emp.dayOfBirth = temp[6]
        emp.gender = temp[7]
        emp.email = temp[8]
        emp.phoneNumber = temp[9]
        emp.address = temp[10]
        emp.maritalStatus = temp[11]
        emp.position = temp[12]
        emp.active = temp[13]
        emp.manager_idEmployee = temp[14]
        emp.manager_firstname = temp[15]
        emp.manager_lastname = temp[16]
        emp.manager_gender = temp[17]
        emp.manager_idDepartment = temp[18]
        emp.manager_position = temp[19]
        emp.manager_email = temp[20]
        emp.manager_phoneNumber = temp[21]
        emp.manager_departmentName = temp[22]
        return emp


def ListEmployee(idManager, pageIndex, pageSize):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListEmployeeByManagerId'
    data=[]
    cursor.callproc(procedure, [idManager, pageIndex, pageSize,])
    for result in cursor.stored_results():
        for temp in result.fetchall():
            emp = Employee()
            emp.id = temp[0]
            emp.firstname = temp[1]
            emp.lastname = temp[2]
            emp.idEmployee = temp[3]
            emp.departmentName = temp[4]
            emp.position = temp[5]
            data.append(emp)
    cursor.close()
    conn.close()
    return data
