from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import employee
from src.Models import employee_task

@app.route('/employee/information', methods=['GET'])
def employeeDetail():
<<<<<<< Updated upstream
   employeeId = request.args.get('employeeId')
   data = employee.employeeInfor(employeeId)
   return jsonify([e.getInformation() for e in data])

@app.route('/employee/update', methods=['POST'])
def employeeUpdate():
   id = request.json['id']
   firstname = request.json['firstname']
   lastname = request.json['lastname']
   idDepartment = request.json['idDepartment']
   position = request.json['position']
   dayOfBirth = request.json['dayOfBirth']
   gender = request.json['gender']
   email = request.json['email']
   phoneNumber = request.json['phoneNumber']
   address = request.json['address']
   maritalStatus = request.json['maritalStatus']
   Emp = employee.Employee()
   Emp.updateInformation(id, firstname, lastname, idDepartment, position, dayOfBirth, gender, email, phoneNumber, address, maritalStatus)
=======
   data = employee.employeeInfor()
   return jsonify([e.getEmployee() for e in data])

@app.route('/employee/checkin_history', methods=['GET'])
def checkinDetail():
   idEmployee = request.args.get('idEmployee')
   data = employee.employeeCheckinHistory(idEmployee)
   return jsonify([e.getCheckinHistory() for e in data])

# url: http://127.0.0.1:5001/employee/checkin_history?idEmployee=1

@app.route('/employee/checkin', methods=['POST'])
def checkin():
   idEmployee = request.json['idEmployee']
   startTime = request.json['startTime']
   date = request.json['date']

   response = employee.CheckinCheckout()
   response.addCheckin(idEmployee,startTime,date)
   return {
      'message':'Thêm thành công'
   }

# url: http://127.0.0.1:5001/employee/checkin

@app.route('/employee/checkout', methods=['POST'])
def checkout():
   idEmployee = request.json['idEmployee']
   endTime = request.json['endTime']
   date = request.json['date']

   response = employee.CheckinCheckout()
   response.addCheckout(idEmployee,endTime,date)
>>>>>>> Stashed changes
   return {
      'message':'Cập nhật thành công'
   }

<<<<<<< Updated upstream
@app.route('/employee/listtask', methods=['GET'])
def employeeListTask():
   idEmployee = request.args.get('idEmployee')
   data = employee_task.listTask(idEmployee)
   return jsonify([t.getTaskEmployee() for t in data])
=======
# url: http://127.0.0.1:5001/employee/checkout

@app.route('/readrequest', methods=['GET'])
def requestReadDetail():
   idEmployee = request.args.get('idEmployee')
   idRequestType = request.args.get('idRequestType')
   data = employee.readRequest(idEmployee, idRequestType)
   return jsonify([e.getRequest() for e in data])

# http://127.0.0.1:5001/readrequest?idEmployee=2&idRequestType=1


@app.route('/employee/addrequestWFH', methods=['POST'])
def requestWFHAddDetail():
   idEmployee = request.json['idEmployee']
   idRequestType = request.json['idRequestType']
   idCensor = request.json['idCensor']
   startDayWFH = request.json['startDayWFH']
   endDayWFH = request.json['endDayWFH']
   reason = request.json['reason']

   response = employee.Request()
   response.addRequestWFH(idEmployee, idRequestType,idCensor, startDayWFH, endDayWFH, reason)
   return {
      'message':'Thêm thành công'
   }

# url: http://127.0.0.1:5001/employee/addrequestWFH
# body: {
#    "idEmployee" : 2,
#     "idRequestType": 2,
#     "idCensor": 3,
#     "startDayWFH": "'2022-07-14'",
#     "endDayWFH": "'2022-07-24'",
#     "reason":"'cuoi vo'"
# }
>>>>>>> Stashed changes
