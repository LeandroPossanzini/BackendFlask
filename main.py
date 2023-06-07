from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from routes.userRoutes import user_api
from routes.contactRoutes import contact_api
app = Flask(__name__)
CORS(app)
app.register_blueprint(user_api)
app.register_blueprint(contact_api)

if(__name__) == "__main__":
    app.run(host='172.26.7.49', port = 80, debug =True)