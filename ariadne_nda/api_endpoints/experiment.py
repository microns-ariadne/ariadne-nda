from flask_restful import Resource
from ariadne_nda import mongo
from ariadne_nda.api_endpoints import api
from ariadne_nda import schema as _schema


class ListExperiment(Resource):
    def get(self):
        schema = _schema.ExperimentSchema()
        experiment = mongo.db.experiment.find({})
        return schema.dump(experiment, many=True).data

api.add_resource(ListExperiment, '/experiment/', methods=['GET'])
