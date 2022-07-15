from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import employee
from src.Models import employee_task

@app.route('/employee/information', methods=['GET'])
def employeeDetail():
   idEmployee = request.args.get('idEmployee')
   data = employee.employeeInfor(idEmployee)
   return jsonify(data.getInformation())

@app.route('/employee/update', methods=['PUT'])
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
   return jsonify(1)

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
   return {
      'message':'Cập nhật thành công'
   }

@app.route('/employee/listtask', methods=['GET'])
def employeeListTask():
   idEmployee = request.args.get('idEmployee')
   data = employee_task.listTask(idEmployee)
   return jsonify([t.getTaskEmployee() for t in data])

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
   idRequestType = request.json['idRequestType']
   idEmployee = request.json['idEmployee']
   idCensor = request.json['idCensor']
   startDayWFH = request.json['startDayWFH']
   endDayWFH = request.json['endDayWFH']
   reason = request.json['reason']

   response = employee.Request()
   response.addRequestWFH(idRequestType, idEmployee, idCensor, startDayWFH, endDayWFH, reason)
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
# }

@app.route('/addrequestOT', methods=['POST'])
def requestOTAddDetail():
   idEmployee = request.json['idEmployee']
   idRequestType = request.json['idRequestType']
   hourOT = request.json['hourOT']
   dayOT = request.json['dayOT']
   reason = request.json['reason']

   response = employee.Request()
   response.addRequestOT(idRequestType, idEmployee, hourOT, dayOT, reason)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"

# http://127.0.0.1:5001/addrequestOT

@app.route('/addrequestOFF', methods=['POST'])
def requestOFFAddDetail():
   idEmployee = request.json('idEmployee')
   idRequestType = request.json('idRequestType')
   startDayOFF = request.json('startDayOFF')
   numberDayOFF = request.json('numberDayOFF')
   noteDayOFF = request.json('noteDayOFF')
   reason = request.json('reason')
   response = employee.Request()
   response.addRequestOFF(idRequestType, idEmployee, startDayOFF, numberDayOFF, noteDayOFF, reason)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"

# http://127.0.0.1:5001/addrequestOFF

