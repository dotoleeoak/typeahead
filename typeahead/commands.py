import click
from typeahead import app


@app.cli.command("index")
@click.argument("input_path")
@click.argument("output_path")
@click.argument("version")
def index(input_path, output_path, version):
    app.config["DIR_INPUT"] = input_path
    app.config["DIR_OUTPUT"] = output_path
    app.config["VERSION"] = version
