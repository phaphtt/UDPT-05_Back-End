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
    def updateTaskByEmployee(self, idTask, status):
        conn = connectDatabase.connect()
        cursor = conn.cursor()
        procedure = 'UpdateStatusTaskByEmployee'
        cursor.callproc(procedure, [idTask, status,])
        cursor.close()
        conn.close()
        return

def listTask(idEmployee, pageIndex, pageSize, status):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListTaskEmployeeById'
    cursor.callproc(procedure, [idEmployee, pageIndex, pageSize, status,])
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

def taskDetailById(idEmployee, pageIndex, pageSize, status, idTask):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'TaskEmployeeDetailById'
    cursor.callproc(procedure, [idEmployee, pageIndex, pageSize, status, idTask,])
    listTask =[]
    task_detail = EmployeeTask()
    data = {'listTask':[], 'task_detail':{}}
    i = 0
    for result in cursor.stored_results():
        if(i == 0):
            for temp in result.fetchall():
                task = EmployeeTask()
                task.id = temp[0]
                task.idTask = temp[1]
                task.taskName = temp[2]
                task.projectName = temp[3]
                task.deadline = temp[4]
                task.status = temp[5]
                listTask.append(task)
        else:
            for temp in result.fetchall():
                task_detail.id = temp[0]
                task_detail.idTask = temp[1]
                task_detail.taskName = temp[2]
                task_detail.projectName = temp[3]
                task_detail.deadline = temp[4]
                task_detail.status = temp[5]
        i = i + 1
    cursor.close()
    conn.close()

    data["listTask"] = [t.getTaskEmployee() for t in listTask]
    data["task_detail"] = task_detail.getTaskEmployee()
    return data

def listTaskByIdDepartment(idDepartment, pageIndex, pageSize, status):
    conn = connectDatabase.connect()
    cursor = conn.cursor()
    procedure = 'ListTaskByIdDepartment'
    cursor.callproc(procedure, [idDepartment, pageIndex, pageSize, status,])
    data = []
    for result in cursor.stored_results():
        for temp in result.fetchall():
            task = EmployeeTask()
            task.idTask = temp[0]
            task.taskName = temp[1]
            task.projectName = temp[2]
            task.deadline = temp[3]
            task.status = temp[4]
            data.append(task)
    cursor.close()
    conn.close()
    return data