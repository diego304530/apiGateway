from flask import Blueprint, jsonify, request
from Config.config import Config
import requests

inventory = Blueprint("inventory", __name__)


@inventory.route("/inventory", methods=["GET"])
def index():
    url = Config.getConfigJson()["url-backend-inventory"] + "/inventory"
    response = requests.get(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@inventory.route("/inventory", methods=["POST"])
def createInventory():
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/inventory"
    response = requests.post(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())


@inventory.route("/inventory/<id>", methods=["GET"])
def getInventory(id):
    url = Config.getConfigJson()["url-backend-inventory"] + "/inventory/" + id
    response = requests.get(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@inventory.route("/inventory/<id>", methods=["PUT"])
def updateInventory(id):
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/inventory/" + id
    response = requests.put(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())


@inventory.route("/inventory/<id>", methods=["DELETE"])
def deleteInventory(id):
    url = Config.getConfigJson()["url-backend-inventory"] + "/inventory/" + id
    response = requests.delete(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@inventory.route("/inventory/<id>/product/<idProduct>", methods=["PUT"])
def setProductToInventory(id, idProduct):
    url = Config.getConfigJson()["url-backend-inventory"] + \
        "/inventory/" + id + "/product/" + idProduct
    response = requests.put(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@inventory.route("/inventory/<id>/employee/<idEmployee>", methods=["PUT"])
def setEmployeeToInventory(id, idEmployee):
    url = Config.getConfigJson()["url-backend-inventory"] + \
        "/inventory/" + id + "/employee/" + idEmployee
    response = requests.put(url, headers=Config.getHeadersJson())
    return jsonify(response.json())
