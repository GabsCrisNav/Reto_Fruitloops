from flask import Flask
from flask_restful import Api
from config import configuration
from routes.image_gattering.test_route import test
from extensions import crs

app = Flask(__name__)

app.config.from_object(configuration['development'])
crs.init_app(app)
app.register_blueprint(test)

if __name__ == '__main__':
    app.run()