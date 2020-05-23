import os
from flask import Flask
from flask_restful import Api
from typeahead.app import *
from typeahead.build_index import BuildIndex


app = Flask(__name__)
api = Api(app)

# Load config from the whole file?
if os.environ.get('TYPEAHEAD_SETTINGS'):
    app.config.from_envvar('TYPEAHEAD_SETTINGS')
else:
    path = app.root_path
    path = os.path.join(path, 'config.py')
    if os.path.isfile(path):
        app.config.from_pyfile(path)
    else:
        print("Please set a config file with typeahead.")
        exit(-1)

# TODO: Cannot use this instance in app.py
# Do we have to overwrite app method here(__init__.py)...?
builder = BuildIndex(**app.config)
builder.tokenize()
builder.build_index()
builder.read_index()

api.add_resource(Status, '/')
api.add_resource(Healthcheck, '/healthcheck')
api.add_resource(Search, '/search/<prefix>')
api.add_resource(Reload, '/admin/index/reload')
api.add_resource(Write, '/admin/index/<prefix>')
