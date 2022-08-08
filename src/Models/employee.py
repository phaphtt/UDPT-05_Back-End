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


class Request:
    def __init__(self):
        self.id = 0
        self.idRequestType = 0
        self.idCheckinCheckOut = 0
        self.idEmployee = 0
        self.idCensor = 0
        self.requestName = ''
        self.hourOT = ''
        self.dayOT = ''
        self.startDayOFF = ''
        self.numberDayOFF = 0
        self.noteDayOFF = ''
        self.startDayWFH = ''
        self.endDayWFH = ''
        self.reason = ''
        self.requestDate = ''
        self.requestStatus = ''
        self.requestRejectReason = ''
        self.active = ''
    def getRequest(self):
        return{
            'id':self.id,         
            'idRequestType':self.idRequestType,         
            'idCheckinCheckOut':self.idCheckinCheckOut,         
            'idEmployee':self.idEmployee,         
            'idCensor':self.idCensor, 
            'requestName':self.requestName, 
            'hourOT':self.hourOT, 
            'dayOT':self.dayOT, 
            'startDayOFF':self.startDayOFF, 
            'numberDayOFF':self.numberDayOFF, 
            'noteDayOFF':self.noteDayOFF, 
            'startDayWFH':self.startDayWFH, 
            'endDayWFH':self.endDayWFH, 
            'reason':self.reason, 
            'requestDate':self.requestDate, 
            'requestStatus':self.requestStatus, 
            'requestRejectReason':self.requestRejectReason, 
            'active':self.active
        }
    
    def addRequestWFH(self,idRequestType,idEmployee,idCensor, startDayWFH, endDayWFH, reason):
        conn = connectDatabase.connect()
        findIdCensor = conn.cursor()
        queryFindIdManager = ('SELECT idManager from Employee where id = {}'.format(idEmployee))
        findIdCensor.execute(queryFindIdManager)

        record = findIdCensor.fetchone()
        idCensor = record[0]
        findIdCensor.close()
        
        cursor = conn.cursor()
        query = ('INSERT INTO Request (idRequestType, idEmployee, idCensor, startDayWFH, endDayWFH, reason) values ({}, {}, {}, {}, {}, {})'.format(idRequestType, idEmployee, idCensor, startDayWFH, endDayWFH, reason))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

    def addRequestOT(self,idRequestType, idEmployee, hourOT, dayOT, reason):
        conn = connectDatabase.connect()
        findIdCensor = conn.cursor()
        queryFindIdManager = ('SELECT idManager from Employee where id = {}'.format(idEmployee))
        findIdCensor.execute(queryFindIdManager)

        record = findIdCensor.fetchone()
        idCensor = record[0]
        findIdCensor.close()
        
        cursor = conn.cursor()
        query = ('INSERT INTO Request (idRequestType, idEmployee, idCensor, hourOT, dayOT, reason, requestDate) values ({}, {}, {}, {}, {}, {}, NOW())'.format(idRequestType, idEmployee, idCensor, hourOT, dayOT, reason))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

    def addRequestOFF(self,idRequestType, idEmployee, startDayOFF, numberDayOFF, noteDayOFF, reason):
        conn = connectDatabase.connect()
        findIdCensor = conn.cursor()
        queryFindIdManager = ('SELECT idManager from Employee where id = {}'.format(idEmployee))
        findIdCensor.execute(queryFindIdManager)

        record = findIdCensor.fetchone()
        idCensor = record[0]
        findIdCensor.close()
        
        cursor = conn.cursor()
        query = ('INSERT INTO Request (idRequestType, idEmployee, idCensor, startDayOFF, numberDayOFF, noteDayOFF, reason, requestDate) values ({}, {}, {}, {}, {}, {}, {}, NOW())'.format(idRequestType, idEmployee, idCensor, startDayOFF, numberDayOFF, noteDayOFF, reason))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

def readRequest(idEmployee, idRequestType):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    query = ('SELECT * FROM Request WHERE idEmployee = {} AND idRequestType = {}'.format(idEmployee, idRequestType))
    cursor.execute(query)
    data = []
    for t in cursor:
        req = Request()
        req.id = t[0]
        req.idRequestType = t[1]
        req.idCheckinCheckOut = t[2]
        req.idEmployee = t[3]
        req.idCensor = t[4]
        req.requestName = t[5]
        req.hourOT = t[6]
        req.dayOT = t[7]
        req.startDayOFF = t[8]
        req.numberDayOFF = t[9]
        req.noteDayOFF = t[10]
        req.startDayWFH = t[11]
        req.endDayWFH = t[12]
        req.reason = t[13]
        req.requestDate = t[14]
        req.requestStatus = t[15]
        req.requestRejectReason = t[16]
        req.active = t[17]

        data.append(req)
    cursor.close()
    conn.close()
    return data
    
class CheckinCheckout:
    def __init__(self):
        self.id = 0
        self.idEmployee = 0
        self.startTime = ''
        self.endTime = ''
        self.date = ''
        self.checkinStatus =''
        self.active = ''
    def getCheckinHistory(self):
        return{
            'id':self.id,               
            'idEmployee':self.idEmployee,         
            'startTime':self.startTime, 
            'endTime':self.endTime, 
            'date':self.date, 
            'checkinStatus':self.checkinStatus,
            'active':self.active
        }

    def addCheckin(self,idEmployee,startTime,date):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        query = ('INSERT INTO CheckinCheckout (idEmployee, startTime, date) values ({}, {}, {})'.format(idEmployee, startTime, date))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

    def addCheckout(self,idEmployee,endTime,date):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        query = ('UPDATE CheckinCheckout SET endTime = {} WHERE idEmployee = {} AND date = {}'.format(endTime, idEmployee, date))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

def employeeCheckinHistory(idEmployee):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    query = ('SELECT * FROM CheckinCheckout WHERE idEmployee = {}'.format(idEmployee))
    cursor.execute(query)
    data = []
    for t in cursor:
        checkin = CheckinCheckout()
        checkin.id = t[0]
        checkin.idEmployee = t[1]
        checkin.startTime = str(t[2])
        checkin.endTime = str(t[3])
        checkin.date = t[4]
        checkin.checkinStatus = t[5]
        checkin.active = t[6]
        data.append(checkin)
    cursor.close()
    conn.close()
    return data
