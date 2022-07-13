from src.Config import connectDatabase

class EmployeeTask:
    def __init__(self):
        self.id = 0
        self.idTask = 0
        self.taskName = ''
        self.projectName = ''
        self.deadline = ''
        self.status = ''
    def getTaskEmployee(self):
        return{
            'id': self.id,
            'idTask': self.idTask,
            'taskName': self.taskName,
            'projectName': self.projectName,
            'deadline': self.deadline,
            'status': self.status
        }

def listTask(idEmployee):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListTaskEmployeeById'
    cursor.callproc(procedure, [idEmployee,])
    data = []
    for result in cursor.stored_results():
        for temp in result.fetchall():
            task = EmployeeTask()
            task.id = temp[0]
            task.idTask = temp[1]
            task.taskName = temp[2]
            task.projectName = temp[3]
            task.deadline = temp[4]
            task.status = temp[5]
            data.append(task)
    cursor.close()
    conn.close()
    return data