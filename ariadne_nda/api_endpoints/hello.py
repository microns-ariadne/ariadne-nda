from flask_restful import Resource
from ariadne_nda.api_endpoints import api


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello brave world'}, 200

api.add_resource(HelloWorld, '/hello/', methods=['GET'])
