import click
from core import createProject
from tokenManager import set_token, get_token

@click.group()
def cli():
    """CLI for mystical project."""
    pass

@click.command("create")
@click.argument("prompt")
@click.argument("output", default="./")
def command_create(prompt: str, output: str):
    """Create project with a prompt."""
    click.echo(f"🚀 Création du projet avec le prompt : {prompt}")
    click.echo(f"🚀 Création du projet avec l'output : {output}")
    createProject(prompt)

@click.command("setToken")
@click.argument("token", required=True)
def command_login(token: str):
    """Set a token to use openAI."""
    click.echo(f"🚀 Save openAI token : {token}")
    set_token(token)

@click.command("getToken")
def command_get_token():
    """Get the token to use openAI."""
    click.echo(f"🚀 Get openAI token")
    token = get_token()
    if token:
        click.echo(f"🚀 Token : {token}")
    else:
        click.echo(f"🚀 No token found")

@click.command("removeToken")
def command_remove_token():
    """Logout from openAI."""
    click.echo(f"🚀 logout from openAI")

cli.add_command(command_create)
cli.add_command(command_login)
cli.add_command(command_remove_token)
cli.add_command(command_get_token)

if __name__ == "__main__":
    cli()