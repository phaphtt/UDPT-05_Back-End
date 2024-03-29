from xmlrpc.client import ResponseError
from src import app
from flask import jsonify, request, Response
from src.Models import requestModels

# http://127.0.0.1:5003/listrequest/censorship
@app.route('/listrequest/censorship', methods=['GET'])
def requestListRequest():
   idCensorship = request.args.get('idCensorship')
   pageIndex = request.args.get('pageIndex')
   pageSize = request.args.get('pageSize')
   typeRequest = request.args.get('typeRequest')
   requestStatus = request.args.get('requestStatus')
   data = requestModels.listRequestCensorship(idCensorship, pageIndex, pageSize, typeRequest, requestStatus)
   return jsonify([e.getRequest() for e in data])

@app.route('/request/detail', methods=['GET'])
def requestDetailById():
   idCensorship = request.args.get('idCensorship')
   pageIndex = request.args.get('pageIndex')
   pageSize = request.args.get('pageSize')
   typeRequest = request.args.get('typeRequest')
   requestStatus = request.args.get('requestStatus')
   idRequest = request.args.get('idRequest')
   data = requestModels.requestDetailById(idCensorship, pageIndex, pageSize, typeRequest, idRequest, requestStatus)
   return jsonify(data)


@app.route('/request/update/censorship', methods=['PUT'])
def requestUpdateByCensorship():
   idRequest = request.json['idRequest']
   requestStatus = request.json['requestStatus']
   requestRejectReason = request.json['requestRejectReason']
   r = requestModels.Request()
   r.updateRequestByCensorship(idRequest, requestStatus, requestRejectReason)
   return jsonify(1)
   


@app.route('/readrequest', methods=['GET'])
def requestReadDetail():
   idEmployee = request.args.get('idEmployee')
   idRequestType = request.args.get('idRequestType')
   data = requestModels.readRequest(idEmployee, idRequestType)
   return jsonify([e.getRequest() for e in data])
   
# http://127.0.0.1:5003/readrequest?idEmployee=3&idRequestType=1


@app.route('/addrequestOT', methods=['POST'])
def requestOTAddDetail():
   idEmployee = request.json['idEmployee']
   idCensor = request.json['idCensor']
   idRequestType = request.json['idRequestType']
   hourOT = request.json['hourOT']
   dayOT = request.json['dayOT']
   reason = request.json['reason']
   employeeFirstName = request.json['employeeFirstName']
   employeeLastName = request.json['employeeLastName']
   censorFirstName = request.json['censorFirstName']
   censorLastName = request.json['censorLastName']
   positionCensor = request.json['positionCensor']

   response = requestModels.Request()
   response.addRequestOT(idRequestType, idEmployee, idCensor, hourOT, dayOT, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"

@app.route('/addrequestOFF', methods=['POST'])
def requestOFFAddDetail():
   idEmployee = request.json['idEmployee']
   idCensor = request.json['idCensor']
   idRequestType = request.json['idRequestType']
   startDayOFF = request.json['startDayOFF']
   numberDayOFF = request.json['numberDayOFF']
   noteDayOFF = request.json['noteDayOFF']
   reason = request.json['reason']
   employeeFirstName = request.json['employeeFirstName'] 
   employeeLastName = request.json['employeeLastName']
   censorFirstName = request.json['censorFirstName']
   censorLastName = request.json['censorLastName']
   positionCensor = request.json['positionCensor']
   
   response = requestModels.Request()
   response.addRequestOFF(idRequestType, idEmployee, idCensor, startDayOFF, numberDayOFF, noteDayOFF, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"


# http://127.0.0.1:5003/readrequest?idEmployee=2&idRequestType=1

@app.route('/employee/addrequestWFH', methods=['POST'])
def requestWFHAddDetail():
   idRequestType = request.json['idRequestType']
   idEmployee = request.json['idEmployee']
   idCensor = request.json['idCensor']
   startDayWFH = request.json['startDayWFH']
   endDayWFH = request.json['endDayWFH']
   reason = request.json['reason']
   employeeFirstName = request.json['employeeFirstName']
   employeeLastName = request.json['employeeLastName']
   censorFirstName = request.json['censorFirstName']
   censorLastName = request.json['censorLastName']
   positionCensor = request.json['positionCensor']

   response = requestModels.Request()
   response.addRequestWFH(idRequestType, idEmployee, idCensor, startDayWFH, endDayWFH, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"

@app.route('/employee/addrequestCheckoutLate', methods=['POST'])
def requestCheckoutLateAddDetail():
   idRequestType = request.json['idRequestType']
   idEmployee = request.json['idEmployee']
   idCensor = request.json['idCensor']
   checkoutDate = request.json['checkoutDate']
   reason = request.json['reason']
   employeeFirstName = request.json['employeeFirstName']
   employeeLastName = request.json['employeeLastName']
   censorFirstName = request.json['censorFirstName']
   censorLastName = request.json['censorLastName']
   positionCensor = request.json['positionCensor']

   response = requestModels.Request()
   response.addRequestCheckoutLate(idRequestType, idEmployee, idCensor, checkoutDate, reason, employeeFirstName, employeeLastName, censorFirstName, censorLastName, positionCensor)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"


@app.route('/employee/checkin_history', methods=['GET'])
def checkinDetail():
   idEmployee = request.args.get('idEmployee')
   pageno = request.args.get('pageno')
   data = requestModels.employeeCheckinHistory(idEmployee, pageno)
   return jsonify([e.getCheckinHistory() for e in data])

# url: http://127.0.0.1:5003/employee/checkin_history?idEmployee=1

# @app.route('/employee/countcheckin', methods=['GET'])
# def countCheckin():
#    data = requestModels.countCheckin()
#    return jsonify([e.getRequest() for e in data])

@app.route('/employee/checkin', methods=['POST'])
def checkin():
   idEmployee = request.json['idEmployee']
   startTime = request.json['startTime']

   response = requestModels.CheckinCheckout()
   response.addCheckin(idEmployee,startTime)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"

# url: http://127.0.0.1:5003/employee/checkin

@app.route('/employee/checkout', methods=['POST'])
def checkout():
   idEmployee = request.json['idEmployee']

   response = requestModels.CheckinCheckout()
   response.addCheckout(idEmployee)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"
