from src.Config import connectDatabase

class Activity:
    def __init__(self):
        id = 0
        idActivityType = 0
        activityName = ''
        activityDeadline = ''
        activityDescription = ''
        active = ''
    def getActivity(self):
        return{
            'id':self.id,
            'idActivityType':self.idActivityType,
            'activityName':self.activityName,
            'activityDeadline':self.activityDeadline,
            'activityDescription':self.activityDescription,
            'active':self.active
        }
def list_all_Activity():
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    query = ('SELECT * FROM CompanyActivity.Activity')
    cursor.execute(query)
    data = []
    for t in cursor:
        emp = Activity()
        emp.id = t[0]
        emp.idActivityType = t[1]
        emp.activityName = t[2]
        emp.activityDeadline = t[3]
        emp.activityDescription = t[4]
        emp.active = t[5]
        data.append(emp)
    cursor.close()
    conn.close()
    return data

def ActivityInfor(activityId):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'GetInfoActivityById'
    cursor.callproc(procedure, [activityId,])
    data = []
    for result in cursor.stored_results():
        emp = Activity()
        temp = result.fetchall()[0]
        emp.id = temp[0]
        emp.idActivityType = temp[1]
        emp.activityName = temp[2]
        emp.activityDeadline = temp[3]
        emp.activityDescription = temp[4]
        emp.active = temp[5]
        data.append(emp)
    cursor.close()
    conn.close()
    return data

def ActivitySearch(activityName):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'SearchActivity'
    cursor.callproc(procedure, [activityName,])
    data = []
    for result in cursor.stored_results():
        for t in result.fetchall():
            emp = Activity()
            emp.id = t[0]
            emp.idActivityType = t[1]
            emp.activityName = t[2]
            emp.activityDeadline = t[3]
            emp.activityDescription = t[4]
            emp.active = t[5]
            data.append(emp)
       
    cursor.close()
    conn.close()
    return data