from flask import request, jsonify, Blueprint
from Config.config import Config
from utils.RespHelper import RespHelper
from waitress import serve
from flask_cors import CORS
from Routes import ProductsRoutes, InventoryRoutes, ClientsRoutes, EmployeesRoutes

from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity, jwt_required, JWTManager
import re
import datetime
import requests

app = Config.getApp()
CORS(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
app.register_blueprint(ProductsRoutes.products)
app.register_blueprint(ClientsRoutes.clients)
app.register_blueprint(InventoryRoutes.inventory)
app.register_blueprint(EmployeesRoutes.employees)


@app.before_request
def before_request_callback():
    endPoint = limpiarUrl(request.path)
    print(endPoint)
    excludedRoutes = ["/login"]
    if excludedRoutes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"] is not None:
            print(usuario)
            tienePermiso = validarPermiso(
                endPoint, request.method, usuario["rol"]["_id"])
            if not tienePermiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401


def limpiarUrl(url):
    partes = url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url


def validarPermiso(endPoint, metodo, idRol):
    url = Config.getConfigJson()["url-backend-security"] + \
        "/permisos-roles/validar-permiso/rol/" + str(idRol)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers)
    try:
        print(response)
        data = response.json()
        print(data)
        if ("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso


@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = Config.getConfigJson()['url-backend-security'] + "/usuario/validar"
    response = requests.post(url, json=data, headers=headers)
    if (response.status_code == 200):
        user = response.json()
        print(user)
        expires = datetime.timedelta(seconds=60*60*24)
        access_token = create_access_token(
            identity=user, expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
        return jsonify({"msg": "Usuario o contraseña incorrectos"}), 401


@app.route("/")
def home():
    return RespHelper.jsonResp("api Gateway Flask funcionando", [], 200), 200


@app.errorhandler(404)
def notFound(error):
    return RespHelper.jsonResp('Ruta no encontrada', [], 404), 404


@app.errorhandler(400)
def routeError(error):
    return RespHelper.jsonResp('Peticion incorrecta', [], 400), 400


@app.errorhandler(405)
def incompleteRoute(error):
    return RespHelper.jsonResp('Faltan elementos en la ruta solicitada', [], 405), 405


if __name__ == "__main__":
    # se usa esta forma de correr el servidor mientras se desarrolla ya que este se recarga automaticamente al guardar cambios el otro no
    app.run(port=Config.getConfigJson()["port"], debug=True)
    # print(
    #     f'Servidor iniciado en la ruta {Config.getConfigJson()["url-backend"]}:{Config.getConfigJson()["port"]}')
    # serve(app, host=Config.getConfigJson()[
    #       "url-backend"], port=Config.getConfigJson()["port"], debug=True)
