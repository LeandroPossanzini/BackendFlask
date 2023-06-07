from db import conectar
from models import Contacto, Pertenece


def seleccionarContactos(id_usuario, campo, orden):
    try:
        session = conectar()
        if campo == "ID" and orden =="ASC":
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id).all()
        elif campo == "ID" and orden == "DESC":
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id.desc()).all() 
        elif campo == "NOMBRE" and orden == "ASC":
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre).all()  
        elif campo == "NOMBRE" and orden == "DESC":
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre.desc()).all()       
    except Exception as e:
        print(e)
    finally:
        session.close()

    return contactos


def seleccionarContacto(id):
    try:
        session = conectar()
        contacto = session.query(Contacto).filter(Contacto.id == id).all()
    
    except Exception as e:
        print(e)
    finally:
        session.close()
    
    return contacto

def busquedaContacto(id, valor):
    try:
        session = conectar()
        contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id).filter((Contacto.nombre.ilike('%'+valor+'%')) | (Contacto.apellidos.ilike('%'+valor+'%')) | (Contacto.direccion.ilike('%'+valor+'%')) | (Contacto.email.ilike('%'+valor+'%'))).order_by(Contacto.nombre).all()
    except Exception as e:
        print(e)
    finally:
        session.close()
    
    return contactos

def insertarContacto(id_usuario,nombre,apellido,direccion,email,telefono):
    try:
        contacto = Contacto(
            nombre = nombre,
            apellidos = apellido,
            direccion = direccion,
            email = email,
            telefono = telefono
        )
        session = conectar()
        session.add(contacto) 
        session.commit()
        # este refres sirve para refrescar la bd y poder seguir trabajando
        # como este contacto lo acabo de creer lo tengo que refrescar
        session.refresh(contacto)
        id_contacto = contacto.id
        # como los id se generan automaticamente para poder matchear las dos
        #tablas uso el id del contacto que estoy queriendo crear
        pertence = Pertenece(
            id_usuario = id_usuario,
            id_contacto = id_contacto
        )
        session.add(pertence)
        session.commit()
    
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
    
    return True

def actualizarConctacto(id,nombre,apellido,direccion,email,telefono):
    try:
        session = conectar()
        contacto = session.query(Contacto).get(id) 
        contacto.nombre = nombre
        contacto.apellidos = apellido
        contacto.direccion = direccion
        contacto.email = email
        contacto.telefono = telefono

        session.add(contacto)
        session.commit()
    
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
    
    return True

def eliminarContacto(id_usuario, id_contacto):
    try:
        session = conectar()
        session.query(Pertenece).filter(Pertenece.id_contacto == id_contacto).filter(Pertenece.id_usuario == id_usuario).delete()
        conctacto = session.query(Contacto).get(id_contacto)
        session.delete(conctacto)
        session.commit()
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
    
    return True