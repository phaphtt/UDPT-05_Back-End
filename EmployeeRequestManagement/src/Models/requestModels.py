from src.Config import connectDatabase
import json
import datetime 

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
        self.employeeFirstName = ''
        self.employeeLastName = ''
        self.employeeLastName = '' 
        self.censorFirstName = ''
        self.censorLastName = ''
        self.positionCensor = ''
        self.checkoutDate = ''
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
            'active':self.active,
            'employeeFirstName':self.employeeFirstName,
            'employeeLastName':self.employeeLastName,
            'censorFirstName':self.censorFirstName,
            'censorLastName':self.censorLastName,
            'positionCensor':self.positionCensor,
            'checkoutDate':self.checkoutDate
        }
    def updateRequestByCensorship(self, idRequest, requestStatus, requestRejectReason):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        procedure = 'UpdateStatusRequestByCensorship'
        cursor.callproc(procedure, [idRequest, requestStatus, requestRejectReason,])
        cursor.close()
        conn.close()
        return
    
    def addRequestWFH(self,idRequestType,idEmployee,idCensor, startDayWFH, endDayWFH, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor):
        conn = connectDatabase.connect()
        
        cursor = conn.cursor()
        query = ('INSERT INTO Request (idRequestType, idEmployee, idCensor, startDayWFH, endDayWFH, reason, requestDate, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor, requestName) values ({}, {}, {}, "{}", "{}", "{}", NOW(), "{}", "{}", "{}", "{}", "{}","Yêu cầu làm việc tại nhà")'.format(idRequestType, idEmployee, idCensor, startDayWFH, endDayWFH, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

    def addRequestOT(self, idRequestType, idEmployee, idCensor, hourOT, dayOT, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor):
        conn = connectDatabase.connect()

        requestName = 'Yêu cầu xin làm thêm giờ'
        cursor = conn.cursor()
        query = ('INSERT INTO Request (idRequestType, idEmployee, idCensor, hourOT, dayOT, reason, requestDate, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor, requestName) values ({}, {}, {}, {}, {}, {}, NOW(), "{}", "{}", "{}", "{}", "{}", "{}")'.format(idRequestType, idEmployee, idCensor, hourOT, dayOT, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor, requestName))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()  
        conn.close()
        return False

    def addRequestOFF(self,idRequestType, idEmployee, idCensor, startDayOFF, numberDayOFF, noteDayOFF, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor):
        conn = connectDatabase.connect()
        
        requestName = 'Yêu cầu xin nghỉ việc'
        cursor = conn.cursor()
        query = ('INSERT INTO Request (idRequestType, idEmployee, idCensor, startDayOFF, numberDayOFF, noteDayOFF, reason, requestDate, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor, requestName) values ({}, {}, {}, {}, {}, {}, {}, NOW(), "{}", "{}", "{}", "{}", "{}", "{}")'.format(idRequestType, idEmployee, idCensor, startDayOFF, numberDayOFF, noteDayOFF, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor, requestName))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

    def addRequestCheckoutLate(self,idRequestType, idEmployee, idCensor, checkoutDate, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor):
        conn = connectDatabase.connect()
        checkCheckoutCursor = conn.cursor()
        checkCheckoutquery = ('SELECT COUNT(*) FROM CheckinCheckout WHERE idEmployee = {} AND status = "Chờ checkout" AND date = "{}"'.format(idEmployee, checkoutDate))
        checkCheckoutCursor.execute(checkCheckoutquery)
        recordCheckout = checkCheckoutCursor.fetchone()
        countCheckout = recordCheckout[0]
        checkCheckoutCursor.close()

        if(countCheckout==0):
            return False

        checkRequestCursor = conn.cursor()
        checkRequestquery = ('SELECT COUNT(*) FROM Request WHERE idEmployee = {} AND checkoutDate = "{}"'.format(idEmployee, checkoutDate))
        checkRequestCursor.execute(checkRequestquery)
        recordRequest = checkRequestCursor.fetchone()
        countRequest = recordRequest[0]
        checkRequestCursor.close()  

        if(countRequest==1):
            return False

        cursor = conn.cursor()
        query = ('INSERT INTO Request (idRequestType, idEmployee, idCensor, checkoutDate, reason, requestDate, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor, requestName) values ({}, {}, {}, "{}", "{}", NOW(), "{}", "{}", "{}", "{}", "{}","Yêu cầu xin checkout bù")'.format(idRequestType, idEmployee, idCensor, checkoutDate, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor))
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
    query = ('SELECT * FROM Request WHERE active = 1 AND idEmployee = {} AND idRequestType = {} order by id desc'.format(idEmployee, idRequestType))
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
        req.employeeFirstName = t[18]
        req.employeeLastName = t[19]
        req.censorFirstName = t[20]
        req.censorLastName = t[21]
        req.positionCensor = t[22]
        req.checkoutDate = t[23]

        data.append(req)
    cursor.close()
    conn.close()
    return data

def listRequestCensorship(idCensorship, pageIndex, pageSize, typeRequest, requestStatus):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListRequestByCensorshipId'
    cursor.callproc(procedure, [idCensorship, pageIndex, pageSize, typeRequest, requestStatus,])
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
            r.employeeFirstName = temp[6]
            r.employeeLastName = temp[7]
            data.append(r)
    return data

def requestDetailById(idCensorship, pageIndex, pageSize, typeRequest, idRequest, requestStatus):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'RequestDetailByIdRequest'
    cursor.callproc(procedure, [idCensorship, pageIndex, pageSize, typeRequest, idRequest, requestStatus,])
    listRequest = []
    request = Request()
    data = {'listRequest':[], 'detailRequest':{}}
    i = 0
    for result in cursor.stored_results():
        if(i == 0):
            for temp in result.fetchall():
                r = Request()
                r.id = temp[0]
                r.requestName = temp[1]
                r.reason = temp[2]
                r.typeName = temp[3]
                r.requestStatus = temp[4]
                r.requestDate = temp[5]
                r.employeeFirstName = temp[6]
                r.employeeLastName = temp[7]
                listRequest.append(r)
        else:
            for temp in result.fetchall():
                request.id = temp[0]
                request.idRequestType = temp[1]
                request.idCheckinCheckOut = temp[2]
                request.idEmployee = temp[3]
                request.idCensor = temp[4]
                request.requestName = temp[5]
                request.hourOT = temp[6]
                request.dayOT = temp[7]
                request.startDayOFF = temp[8]
                request.numberDayOFF = temp[9]
                request.noteDayOFF = temp[10]
                request.startDayWFH = temp[11]
                request.endDayWFH = temp[12]
                request.reason = temp[13]
                request.requestDate = temp[14]
                request.requestStatus = temp[15]
                request.requestRejectReason = temp[16]
                request.active = temp[17]
                request.employeeFirstName = temp[18]
                request.employeeLastName = temp[19]
                request.censorFirstName = temp[20]
                request.censorLastName = temp[21]
                request.positionCensor = temp[22]
                request.typeName = temp[23]
                request.checkoutDate = temp[24]
        i = i + 1
    
    data["listRequest"] = [e.getRequest() for e in listRequest]
    data["detailRequest"] = request.getRequest()
    return data

class CheckinCheckout:
    def __init__(self):
        self.id = 0
        self.idEmployee = 0
        self.startTime = ''
        self.endTime = ''
        self.date = ''
        self.status = ''
        self.active = ''
    def getCheckinHistory(self):
        return{
            'id':self.id,               
            'idEmployee':self.idEmployee,         
            'startTime':self.startTime, 
            'endTime':self.endTime, 
            'date':self.date, 
            'status':self.status,
            'active':self.active
        }

    def addCheckin(self,idEmployee,startTime):
        conn = connectDatabase.connect()
        curDate = datetime.date.today()

        checkinCursor = conn.cursor()
        checkinquery = ('SELECT COUNT(*) FROM CheckinCheckout WHERE idEmployee = {} AND date = "{}"'.format(idEmployee, curDate))
        checkinCursor.execute(checkinquery)
        recordcheckin = checkinCursor.fetchone()
        countcheckin = recordcheckin[0]
        checkinCursor.close()  

        t  = datetime.datetime.now()
        if(countcheckin > 0):
            return False
        
        if(t.hour <= 8 or t.hour >= 10):
            return False

        cursor = conn.cursor()
        query = ('INSERT INTO CheckinCheckout (idEmployee, startTime, date, status) values ({}, "{}", "{}","Chờ checkout")'.format(idEmployee, startTime, curDate))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

    def addCheckout(self,idEmployee):
        conn = connectDatabase.connect()
        curDate = datetime.date.today()
        checkoutCursor = conn.cursor()
        checkoutquery = ('SELECT COUNT(*) FROM CheckinCheckout WHERE idEmployee = {} AND date = "{}" AND status = "Chờ checkout"'.format(idEmployee, curDate))
        checkoutCursor.execute(checkoutquery)
        recordCheckout = checkoutCursor.fetchone()
        countCheckout = recordCheckout[0]
        checkoutCursor.close()  

        t  = datetime.datetime.now()
        if(countCheckout == 0):
            return False

        if(t.hour <= 16 or t.hour >= 20):
            return False

        cursor = conn.cursor()
        query = ('UPDATE CheckinCheckout SET endTime = "16:00:00", status = "Hoàn thành" WHERE idEmployee = {} AND date = "{}" AND status = "Chờ checkout"'.format(idEmployee, curDate))
        cursor.execute(query)
        if(conn.commit()):
            cursor.close()
            conn.close()
            return True
        cursor.close()
        conn.close()
        return False

# def countCheckin():
#     conn = connectDatabase.connect()
#     cursor = conn.cursor()
#     query = ('SELECT COUNT(*) FROM CheckinCheckout')
#     cursor.execute(query)
#     record = cursor.fetchone()
#     data = record[0]
#     cursor.close()
#     conn.close()
#     return data

def employeeCheckinHistory(idEmployee, pageno):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    offset = (int(pageno)-1) * 10
    query = ('SELECT * FROM CheckinCheckout WHERE idEmployee = {} LIMIT {},10'.format(idEmployee, offset))
    cursor.execute(query)
    data = []
    for t in cursor:
        checkin = CheckinCheckout()
        checkin.id = t[0]
        checkin.idEmployee = t[1]
        checkin.startTime = str(t[2])
        checkin.endTime = str(t[3])
        checkin.date = t[4]
        checkin.status = str(t[5])
        checkin.active = t[6]
        data.append(checkin)
    cursor.close()
    conn.close()
    return data


