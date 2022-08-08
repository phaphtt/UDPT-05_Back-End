from src.Config import connectDatabase

class Device:
    id = 0
    idDeviceType = 0
    deviceName = ''
    deviceQuota = ''
    deviceStatus = ''
    active = ''
    def getInformation(self):
        return{
            'id':self.id,
            'idDeviceType':self.idDeviceType,
            'deviceName':self.deviceName,
            'deviceQuota':self.deviceQuota,
            'deviceStatus':self.deviceStatus,
            'active':self.active
        }

def list_all_Device():
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    query = ('SELECT * FROM DeviceRequest.Device WHERE active = 1')
    cursor.execute(query)
    data = []
    for t in cursor:
        dr = Device()
        dr.id=t[0]
        dr.idDeviceType=t[1]
        dr.deviceName=t[2]
        dr.deviceQuota=t[3]
        dr.deviceStatus=t[4]
        dr.active=t[5]
        data.append(dr)
    cursor.close()
    conn.close()
    return data