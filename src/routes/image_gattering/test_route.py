from flask import Blueprint, make_response
from flask_cors import cross_origin

test = Blueprint('test', __name__)

@test.route('/test', methods=['GET']) 
@cross_origin()
def sayHello():
    return make_response('Hi there',200)