from flask_restful import Resource
from ariadne_nda.api_endpoints import api


class Experiment(Resource):
    def get(self):
        return {'message': 'experiments'}, 200


class Sample(Resource):
    def get(self):
        return {'message': 'samples'}, 200


class Dataset(Resource):
    def get(self):
        return {'message': 'datasets'}, 200


class Channel(Resource):
    def get(self):
        return {'message': 'channels'}, 200


class ChannelMetadata(Resource):
    def get(self):
        return {'message': 'channel_metadata'}, 200


class EntityFeature(Resource):
    def get(self):
        return {'message': 'entity_feature'}, 200


class Data(Resource):
    def get(self):
        return {'message': 'data'}, 200


class Mask(Resource):
    def get(self):
        return {'message': 'mask'}, 200


api.add_resource(Experiment, '/anatomy/experiments', methods=['GET'])
api.add_resource(Sample, '/anatomy/samples/', methods=['GET'])
api.add_resource(Dataset, '/anatomy/datasets/', methods=['GET'])
api.add_resource(Channel, '/anatomy/channels/', methods=['GET'])
api.add_resource(ChannelMetadata, '/anatomy/channel_metadata/',
                 methods=['GET'])
api.add_resource(EntityFeature, '/anatomy/entity_feature/', methods=['GET'])
api.add_resource(Data, '/anatomy/data/', methods=['GET'])
api.add_resource(Mask, '/anatomy/mask/', methods=['GET'])
