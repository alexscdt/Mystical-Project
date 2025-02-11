import click
from core import createProject

@click.group()
def cli():
    """CLI for mystical project."""
    pass

@click.command("create")
@click.argument("prompt")
def create(prompt):
    """Create project with a prompt."""
    click.echo(f"🚀 Création du projet avec le prompt : {prompt}")
    createProject(prompt)

@click.command("login")
@click.argument("token")
def login(token):
    """Set a token to use openAI."""
    click.echo(f"🚀 login with openAI token : {token}")

cli.add_command(create)
cli.add_command(login)

if __name__ == "__main__":
    cli()