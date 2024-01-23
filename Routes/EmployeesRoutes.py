from flask import Blueprint, jsonify, request
from Config.config import Config
import requests

employees = Blueprint("employees", __name__)


@employees.route("/employees", methods=["GET"])
def index():
    url = Config.getConfigJson()["url-backend-inventory"] + "/employees"
    response = requests.get(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@employees.route("/employees/<id>", methods=["GET"])
def getEmployee(id):
    url = Config.getConfigJson()["url-backend-inventory"] + "/employees/" + id
    response = requests.get(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@employees.route("/employees", methods=["POST"])
def createEmployees():
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/employees"
    response = requests.post(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())


@employees.route("/employees/<id>", methods=["PUT"])
def updateEmployee(id):
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/employees/" + id
    response = requests.put(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())


@employees.route("/employees/<id>", methods=["DELETE"])
def deleteEmployee(id):
    url = Config.getConfigJson()["url-backend-inventory"] + "/employees/" + id
    response = requests.delete(url, headers=Config.getHeadersJson())
    return jsonify(response.json())
