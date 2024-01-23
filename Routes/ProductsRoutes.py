from flask import Blueprint, jsonify, request
from Config.config import Config
import requests

products = Blueprint("products", __name__)


@products.route("/products", methods=["GET"])
def index():
    url = Config.getConfigJson()["url-backend-inventory"] + "/products"
    response = requests.get(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@products.route("/products", methods=["POST"])
def createProduct():
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/products"
    response = requests.post(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())


@products.route("/products/<id>", methods=["GET"])
def getProduct(id):
    url = Config.getConfigJson()["url-backend-inventory"] + "/products/" + id
    response = requests.get(url, headers=Config.getHeadersJson())
    return jsonify(response.json())


@products.route("/products/<id>", methods=["PUT"])
def updateProduct(id):
    data = request.get_json()
    url = Config.getConfigJson()["url-backend-inventory"] + "/products/" + id
    response = requests.put(url, headers=Config.getHeadersJson(), json=data)
    return jsonify(response.json())


@products.route("/products/<id>", methods=["DELETE"])
def deleteProduct(id):
    url = Config.getConfigJson()["url-backend-inventory"] + "/products/" + id
    response = requests.delete(url, headers=Config.getHeadersJson())
    return jsonify(response.json())
