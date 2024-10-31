import click


@click.group(short_help="karudata CLI.")
def karudata():
    """karudata CLI.
    """
    pass


@karudata.command()
@click.argument("name", default="karudata")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [karudata]
