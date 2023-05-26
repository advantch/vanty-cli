import rich
import typer

from cli._client import Client
from cli.config import config

app = typer.Typer(name="project", help="Manage project files", no_args_is_help=True)


@app.command(help="Downloads project files from advantch.com.")
def download():
    """
    Download project files from advantch.com.
    :return:
    """

    token_id = config.get("token_id")
    if token_id is None:
        rich.print("[red]Please run `vanty auth set` to set your token.[/red]")
        raise typer.Exit(code=1)

    rich.print("[green]Downloading project files...[/green]")
    Client().download()


@app.command(help="Print current configuration.")
def print_config():
    """
    Print current configuration.
    :return:
    """
    rich.print("[green]Current configuration:[/green]")
    rich.print(config)
