# users-service/manage.py
# use Flask CLI
# References:
#   http://flask.pocoo.org/docs/0.12/cli/
#   https://stackoverflow.com/questions/42754341/use-flasks-click-cli-with-the-app-factory-pattern

from flask.cli import FlaskGroup
from project import app


def shell_context():
    return {'app': app}

app.shell_context_processor(shell_context)

cli = FlaskGroup(app)

@cli.command
def custom_comment():
    pass

if __name__ == '__main__':
    cli()
