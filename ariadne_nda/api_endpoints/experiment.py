from flask import request
from flask_restful import Resource
from ariadne_nda import mongo
from ariadne_nda.api_endpoints import api
from ariadne_nda import schema as _schema
from ariadne_nda.logging import log


class ListExperiment(Resource):
    def __init__(self, *args, **kwargs):
        self.experiment = mongo.db.experiment
        self.experiment.create_index('name', unique=True)
        super().__init__(*args, **kwargs)

    def get(self):
        schema = _schema.ExperimentSchema()
        exp_find = self.experiment.find({})
        return schema.dump(exp_find, many=True).data

    def post(self):
        schema = _schema.ExperimentSchema()
        exp_dict = request.get_json(force=True)
        exp_dict, errors = schema.load(exp_dict)
        if errors:
            log.debug(errors)
            return {'message': errors}, 400
        self.experiment.insert(exp_dict)
        exp_find = self.experiment.find_one(exp_dict)
        return schema.dump(exp_find).data, 201

api.add_resource(ListExperiment, '/experiment/', methods=['GET', 'POST'])
