import click
from typeahead import app
from typeahead.build_index import BuildIndex


@app.cli.command("index")
@click.argument("input_path")
@click.argument("output_path")
@click.argument("version")
def index(input_path, output_path, version):
    app.config["DIR_INPUT"] = input_path
    app.config["DIR_OUTPUT"] = output_path
    app.config["VERSION"] = version

    builder = BuildIndex(
        app.config["DIR_INPUT"],
        app.config["DIR_OUTPUT"],
        app.config["VERSION"],
        app.config["HEAP_SIZE"],
        app.config["PREFIX_SIZE"],
    )
