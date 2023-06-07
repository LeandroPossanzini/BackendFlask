from flask import Flask, jsonify, request, Blueprint
import controllers.contacControler as contactController

contact_api = Blueprint('contact_api', __name__)


@contact_api.route("/contactos", methods= ['GET'])
def getContactos():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    campo = parametros['campo']
    orden = parametros['orden']
    contactos  = contactController.seleccionarContactos(id_usuario,campo,orden)

    return jsonify( contactos)

@contact_api.route("/contacto", methods=['GET'])
def getConctacto():
    parametros = request.args
    id_contacto = parametros['id']
    contacto = contactController.seleccionarContacto(id_contacto)

    return jsonify(contacto)

@contact_api.route("/contactoStr", methods =['GET'])
def getContactoStr():
    parametros = request.args
    id_contacto = parametros['id_contacto']
    valor = parametros['valor']
    contacto = contactController.busquedaContacto(id_contacto,valor)

    return jsonify(contacto)

@contact_api.route("/contacto", methods = ["POST"])
def insertContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    nombre = parametros["nombre"]
    direccion = parametros["direccion"]
    apellido = parametros["apellido"]
    email = parametros["email"]
    telefono = parametros["telefono"]

    contacto = contactController.insertarContacto(id_usuario, nombre, apellido,direccion, email, telefono)

    return jsonify({'result':contacto})
 
@contact_api.route("/contacto", methods = ["PUT"])
def updateContacto():
    parametros = request.args
    id = parametros["id"]
    nombre = parametros["nombre"]
    direccion = parametros["direccion"]
    apellido = parametros["apellido"]
    email = parametros["email"]
    telefono = parametros["telefono"]

    contacto = contactController.actualizarConctacto(id, nombre, direccion, apellido, email, telefono)

    return jsonify({"Result": contacto})

@contact_api.route("/contacto", methods = ["DELETE"])
def deleteContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    id_contacto = parametros['id_contacto']
    borrado = contactController.eliminarContacto(id_usuario, id_contacto)

    return jsonify({"Resutl": borrado})