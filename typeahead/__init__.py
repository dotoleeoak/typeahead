import os
from flask import Flask

app = Flask(__name__)

if os.environ.get("TYPEAHEAD_SETTINGS"):
    app.config.from_envvar("TYPEAHEAD_SETTINGS")
else:
    path = app.root_path
    path = os.path.join(path, "config")
    path = os.path.join(path, "config.py")
    if os.path.isfile(path):
        app.config.from_pyfile(path)
    else:
        print("Please set a config file with typeahead.")
        exit(-1)

# to set app.route
from typeahead.app import *
