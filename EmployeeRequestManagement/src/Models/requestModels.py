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