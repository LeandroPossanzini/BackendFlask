from flask import Flask, jsonify, request, Blueprint
import  controllers.userControler as usercontroler


user_api = Blueprint('user_api', __name__)

@user_api.route("/usuario", methods= ['GET'])
def getUsuario():
    parametros = request.args
    email = parametros['email']
    password = parametros['password']
    result = usercontroler.seleccionarUsuario(email, password)
    return jsonify({'result': result})