from src.Config import connectDatabase

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
        self.typeName = ''
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
            'typeName':self.typeName, 
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

    def addRequestOT(self, idRequestType, idEmployee, idCensor, hourOT, dayOT, reason):
        conn = connectDatabase.connect()

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

    def addRequestOFF(self,idRequestType, idEmployee, idCensor, startDayOFF, numberDayOFF, noteDayOFF, reason):
        conn = connectDatabase.connect()
        
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

def listRequestCensorship(idCensorship, pageIndex, pageSize, typeRequest):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListRequestByCensorshipId'
    cursor.callproc(procedure, [idCensorship, pageIndex, pageSize, typeRequest,])
    data = []
    for result in cursor.stored_results():
        for temp in result.fetchall():
            r = Request()
            r.id = temp[0]
            r.requestName = temp[1]
            r.reason = temp[2]
            r.typeName = temp[3]
            r.requestStatus = temp[4]
            r.requestDate = temp[5]
            data.append(r)
    return data

class CheckinCheckout:
    def __init__(self):
        self.id = 0
        self.idEmployee = 0
        self.startTime = ''
        self.endTime = ''
        self.date = ''
        self.active = ''
    def getCheckinHistory(self):
        return{
            'id':self.id,               
            'idEmployee':self.idEmployee,         
            'startTime':self.startTime, 
            'endTime':self.endTime, 
            'date':self.date, 
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
        checkin.active = t[5]
        data.append(checkin)
    cursor.close()
    conn.close()
    return data


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
        checkin.active = t[5]
        data.append(checkin)
    return data
