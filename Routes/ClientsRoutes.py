from flask import Blueprint, jsonify, request
from Config.config import Config
import requests

clients = Blueprint("clients", __name__)


@clients.route("/clients", methods=["GET"])
def index():
    url = Config.getConfigJson()["url-backend-inventory"] + "/clients"
    response = requests.get(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@clients.route("/clients", methods=["POST"])
def createClient():
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/clients"
    response = requests.post(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())


@clients.route("/clients/<id>", methods=["GET"])
def getClient(id):
    url = Config.getConfigJson()["url-backend-inventory"] + "/clients/" + id
    response = requests.get(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@clients.route("/clients/<id>", methods=["PUT"])
def updateClient(id):
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/clients/" + id
    response = requests.put(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())


@clients.route("/clients/<id>", methods=["DELETE"])
def deleteClient(id):
    url = Config.getConfigJson()["url-backend-inventory"] + "/clients/" + id
    response = requests.delete(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@clients.route("/sendMail", methods=["POST"])
def sendMail():
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/sendMail"
    response = requests.post(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())
