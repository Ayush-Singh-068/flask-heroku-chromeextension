from flask import Flask

from app.api.routes import api
from config.constants import HOST, PORT
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
