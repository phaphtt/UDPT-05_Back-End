from src.Config import connectDatabase

class DeviceRequest:
    id = 0
    idEmployee = 0
    idITManager = 0
    idDevice = 0
    requestName = ''
    reason = ''
    type = ''
    noteRequest = ''
    requestDate = ''
    requestStatus = ''
    requestITRejectReason = ''
    requestManagerRejectReason = ''
    active = ''
    def getInformation(self):
        return{
            'id':self.id,
            'idEmployee':self.idEmployee,
            'idITManager':self.idITManager,
            'idDevice':self.idDevice,
            'requestName':self.requestName,
            'reason':self.reason,
            'type':self.type,
            'noteRequest':self.noteRequest,
            'requestDate':self.requestDate,
            'requestStatus':self.requestStatus,
            'requestITRejectReason':self.requestITRejectReason,
            'requestManagerRejectReason':self.requestManagerRejectReason,
            'active':self.active
        }
    def insertInformation(self, idEmployee, requestName, type, reason, noteRequest):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        procedure = 'InsertDeviceRequest'
        cursor.callproc(procedure, [idEmployee, requestName, type, reason, noteRequest,])
        cursor.close()
        conn.close()
        return
    def updateInformationByITManager(self, requestStatus, requestITRejectReason, idITManager, id):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        procedure = 'UpdateDeviceRequestByITManager'
        cursor.callproc(procedure, [requestStatus, requestITRejectReason, idITManager, id,])
        cursor.close()
        conn.close()
        return
    def updateInformationByPresident(self, requestStatus, requestManagerRejectReason, id):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        procedure = 'UpdateDeviceRequestByPresident'
        cursor.callproc(procedure, [requestStatus, requestManagerRejectReason, id,])
        cursor.close()
        conn.close()
        return

def ListDeviceRequestByEmployeeId(idEmployee):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListDeviceRequestByEmployeeId'
    cursor.callproc(procedure, [idEmployee,])
    data = []
    for result in cursor.stored_results():
        for temp in result.fetchall():
            dr = DeviceRequest()
            dr.id=temp[0]
            dr.idEmployee=temp[1]
            dr.idITManager=temp[2]
            dr.idDevice=temp[3]
            dr.requestName=temp[4]
            dr.reason=temp[5]
            dr.type=temp[6]
            dr.noteRequest=temp[7]
            dr.requestDate=temp[8]
            dr.requestStatus=temp[9]
            dr.requestITRejectReason=temp[10]
            dr.requestManagerRejectReason=temp[11]
            dr.active=temp[12]
            data.append(dr)
    cursor.close()
    conn.close()
    return data

def ListDeviceRequestById(id):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListDeviceRequestById'
    cursor.callproc(procedure, [id,])
    data = []
    for result in cursor.stored_results():
        for temp in result.fetchall():
            dr = DeviceRequest()
            dr.id=temp[0]
            dr.idEmployee=temp[1]
            dr.idITManager=temp[2]
            dr.idDevice=temp[3]
            dr.requestName=temp[4]
            dr.reason=temp[5]
            dr.type=temp[6]
            dr.noteRequest=temp[7]
            dr.requestDate=temp[8]
            dr.requestStatus=temp[9]
            dr.requestITRejectReason=temp[10]
            dr.requestManagerRejectReason=temp[11]
            dr.active=temp[12]
            data.append(dr)
    cursor.close()
    conn.close()
    return data

def list_all_DeviceRequest():
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    query = ('SELECT * FROM DeviceRequest WHERE active = 1')
    cursor.execute(query)
    data = []
    for t in cursor:
        dr = DeviceRequest()
        dr.id=t[0]
        dr.idEmployee=t[1]
        dr.idITManager=t[2]
        dr.idDevice=t[3]
        dr.requestName=t[4]
        dr.reason=t[5]
        dr.type=t[6]
        dr.noteRequest=t[7]
        dr.requestDate=t[8]
        dr.requestStatus=t[9]
        dr.requestITRejectReason=t[10]
        dr.requestManagerRejectReason=t[11]
        dr.active=t[12]
        data.append(dr)
    cursor.close()
    conn.close()
    return data

def list_DeviceRequestByStatus(requestStatus):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListDeviceRequestByStatus'
    cursor.callproc(procedure, [requestStatus,])
    data = []
    for result in cursor.stored_results():
        for temp in result.fetchall():
            dr = DeviceRequest()
            dr.id=temp[0]
            dr.idEmployee=temp[1]
            dr.idITManager=temp[2]
            dr.idDevice=temp[3]
            dr.requestName=temp[4]
            dr.reason=temp[5]
            dr.type=temp[6]
            dr.noteRequest=temp[7]
            dr.requestDate=temp[8]
            dr.requestStatus=temp[9]
            dr.requestITRejectReason=temp[10]
            dr.requestManagerRejectReason=temp[11]
            dr.active=temp[12]
            data.append(dr)
    cursor.close()
    conn.close()
    return data