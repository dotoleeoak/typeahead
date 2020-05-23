from flask_restful import Resource


# TODO: many many things to implement...
# but I don't think it'll take much time

class Status(Resource):
    def get(self):
        # return app.config
        pass


class Healthcheck(Resource):
    def get(self):
        # return 'what is liveness?'
        pass


class Search(Resource):
    def get(self, prefix):
        # return builder.typeahead[prefix]
        pass


class Reload(Resource):
    def post(self):
        pass


class Write(Resource):
    def post(self, prefix):
        pass

    def delete(self, prefix):
        pass


# api.add_resource(Status, '/')
# api.add_resource(Healthcheck, '/healthcheck')
# api.add_resource(Search, '/search/<prefix>')
# api.add_resource(Reload, '/admin/index/reload')
# api.add_resource(Write, '/admin/index/<prefix>')

# if __name__ == '__main__':
#     app.run(port=CONFIG['port'])
