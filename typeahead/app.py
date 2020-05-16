from flask import Flask, request
from flask_restful import Resource, Api
from config import CONFIG
import main

main.tokenize(CONFIG["filename"])
main.build_index(CONFIG["pq_size"])
main.preprocess()

app = Flask(__name__)
api = Api(app)

class Status(Resource):
    def get(self):
        return CONFIG

class Healthcheck(Resource):
    def get(self):
        return 'what is liveness?'

class Search(Resource):
    def get(self, prefix):
        return str(main.query(prefix))

class Reload(Resource):
    def post(self):
        main.tokenize(CONFIG["filename"])
        main.build_index(CONFIG["pq_size"])
        main.preprocess()

class Write(Resource):
    def post(self, prefix):
        pass
    
    def delete(self, prefix):
        pass

api.add_resource(Status, '/')
api.add_resource(Healthcheck, '/healthcheck')
api.add_resource(Search, '/search/<prefix>')
api.add_resource(Reload, '/admin/index/reload')
api.add_resource(Write, '/admin/index/<prefix>')

if __name__ == '__main__':
    app.run(port=CONFIG['port'])
