from typeahead import app

from typeahead.build_index import BuildIndex

builder = BuildIndex(
    app.config["DIR_INPUT"],
    app.config["DIR_OUTPUT"],
    app.config["VERSION"],
    app.config["HEAP_SIZE"],
    app.config["PREFIX_SIZE"],
)


@app.before_first_request
def load():
    builder.read_index()


@app.route("/")
def status():
    return str(dict(app.config))  # cannot return config directly


@app.route("/healthcheck")
def healthcheck():
    return "status OK."


@app.route("/search/<prefix>")
def search(prefix):
    return str(builder.search(prefix))


@app.route("/admin/index/reload", methods=["POST"])
def reload():
    builder.reload()
    return "Index reloaded."


@app.route("/admin/index/<prefix>", methods=["POST", "DELETE"])
def update(prefix):
    builder.update(prefix, request.json[prefix])
    return "Index updated."


@app.route("/admin/index/<prefix>", methods=["DELETE"])
def delete(prefix):
    builder.delete(prefix, request.json[prefix])
    return "Index deleted."
