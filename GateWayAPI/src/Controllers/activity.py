from src import app
from flask import jsonify, request, Response
from src.Models import activity
import json

@app.route('/activity/getall', methods=['GET'])
def list_all_acitvity():
   data = activity.list_all_Activity()
   return jsonify([e.getActivity() for e in data])

@app.route('/activity/information', methods=['GET'])
def activityDetail():
   activityId = request.args.get('activityId')
   data = activity.ActivityInfor(activityId)
   return jsonify([e.getActivity() for e in data])

@app.route('/activity/search', methods=['GET'])
def activitySearch():
   activityName = request.args.get('activityName')
   data = activity.ActivitySearch(activityName)
   return jsonify([e.getActivity() for e in data])