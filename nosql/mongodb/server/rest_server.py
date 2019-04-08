from flask import Flask, request
from neo4j.v1 import GraphDatabase, basic_auth
from pymongo import MongoClient
from flask_restful import Resource, Api
import json
from bson import json_util

driver = GraphDatabase.driver(
    "bolt://62.44.127.197:7687",
    auth=basic_auth("neo4j", "neo4j"))
session = driver.session()

client = MongoClient("mongodb://62.44.127.197:27017")
db = client.test

app = Flask(__name__)
api = Api(app)


class Sample(Resource):
    def get(self, sample_case_id=None):
        result = db.samples.find({'PATIENT_ID': sample_case_id}).limit(25)
        result_list = []
        for record in result:
            result_list.append(record)
        json_result = json_util.dumps(result_list)
        return json_result, 200  # Fetches first column that is Employee ID


class Samples(Resource):
    def get(self):
        result = session.read_transaction(self.print_samples)
        json_result = json.dumps(result)
        return json_result, 200  # Fetches first column that is Employee ID

    @classmethod
    def print_samples(cls, tx):
        result_list = []
        result = tx.run("MATCH (n:clinical) RETURN n LIMIT 25")
        for record in result:
            result_list.append(list(record['n'].values()))
        return result_list


class Tracks(Resource):
    def get(self):
        pass


class Employees_Name(Resource):
    def get(self, employee_id):
        pass


api.add_resource(Samples, '/samples')  # Route_1
api.add_resource(Sample, '/sample/<sample_case_id>')  # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3


if __name__ == '__main__':
    app.run(host='0.0.0.0')
