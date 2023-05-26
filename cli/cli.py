import typer

from cli.project import app as project
from cli.dev import app as dev
from cli.ops import app as ops
from cli.auth import app as auth



app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="markdown",
    help="""
    Vanty is the fastest way to launch new SaaS & AI products.

    Visit https://www.advantch.com/ for documentation and more information

    """,
)
app.add_typer(auth)
app.add_typer(dev)
app.add_typer(ops)
app.add_typer(project)
