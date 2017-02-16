from flask_restful import Resource
from ariadne_nda.api_endpoints import api


class Animal(Resource):
    def get(self):
        return {'message': 'animals'}, 200


class AnimalInfo(Resource):
    def get(self):
        return {'message': 'animal_info'}, 200


class Session(Resource):
    def get(self):
        return {'message': 'sessions'}, 200


class SessionInfo(Resource):
    def get(self):
        return {'message': 'session_info'}, 200


class Run(Resource):
    def get(self):
        return {'message': 'runs'}, 200


class RunInfo(Resource):
    def get(self):
        return {'message': 'run_info'}, 200


class Cell(Resource):
    def get(self):
        return {'message': 'cells'}, 200


class CellInfo(Resource):
    def get(self):
        return {'message': 'cell_info'}, 200


class Trial(Resource):
    def get(self):
        return {'message': 'trials'}, 200


class TrialInfo(Resource):
    def get(self):
        return {'message': 'trial_info'}, 200


class RawEyeTracking(Resource):
    def get(self):
        return {'message': 'raw_eye_tracking'}, 200


class FunctionalTimeCourse(Resource):
    def get(self):
        return {'message': 'functional_time_course'}, 200


class GlobalCell(Resource):
    def get(self):
        return {'message': 'global_cells'}, 200


class CellCollection(Resource):
    def get(self):
        return {'message': 'cell_collections'}, 200


class CellCollectionInfo(Resource):
    def get(self):
        return {'message': 'cell_collection_info'}, 200


class PerCellMetrics(Resource):
    def get(self):
        return {'message': 'per_cell_metrics'}, 200


class PerCellMetric(Resource):
    def get(self):
        return {'message': 'per_cell_metric'}, 200


class PerCellMetricInfo(Resource):
    def get(self):
        return {'message': 'per_cell_metric_info'}, 200


api.add_resource(Animal, '/physiology/animals', methods=['GET'])
api.add_resource(AnimalInfo, '/physiology/animal_info', methods=['GET'])
api.add_resource(Session, '/physiology/sessions', methods=['GET'])
api.add_resource(SessionInfo, '/physiology/session_info', methods=['GET'])
api.add_resource(Run, '/physiology/runs', methods=['GET'])
api.add_resource(RunInfo, '/physiology/run_info', methods=['GET'])
api.add_resource(Cell, '/physiology/cells', methods=['GET'])
api.add_resource(CellInfo, '/physiology/cell_info', methods=['GET'])
api.add_resource(Trial, '/physiology/trials', methods=['GET'])
api.add_resource(TrialInfo, '/physiology/trial_info', methods=['GET'])
api.add_resource(RawEyeTracking, '/physiology/raw_eye_tracking',
                 methods=['GET'])
api.add_resource(FunctionalTimeCourse, '/physiology/functional_time_course',
                 methods=['GET'])
api.add_resource(GlobalCell, '/physiology/global_cells', methods=['GET'])
api.add_resource(CellCollection, '/physiology/cell_collections',
                 methods=['GET'])
api.add_resource(CellCollectionInfo, '/physiology/cell_collection_info',
                 methods=['GET'])
api.add_resource(PerCellMetrics, '/physiology/per_cell_metrics',
                 methods=['GET'])
api.add_resource(PerCellMetricInfo, '/physiology/per_cell_metric_info',
                 methods=['GET'])
api.add_resource(PerCellMetric, '/physiology/per_cell_metric', methods=['GET'])
