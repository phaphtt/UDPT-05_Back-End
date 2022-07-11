from src.Config import connectDatabase

def employeeInfor():
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    query = ('SELECT * FROM Employee')
    cursor.execute(query)
    data = []
    for t in cursor:
        data.append(t)
    cursor.close()
    conn.close()
    return data