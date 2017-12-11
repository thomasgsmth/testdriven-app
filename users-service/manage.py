# users-service/manage.py
# use Flask CLI
# References:
#   http://flask.pocoo.org/docs/0.12/cli/
#   https://stackoverflow.com/questions/42754341/use-flasks-click-cli-with-the-app-factory-pattern

#from flask.cli import FlaskGroup
from flask_script import Manager
from project import app, db


#def shell_context():
#    return {'app': app}

#app.shell_context_processor(shell_context)

#cli = FlaskGroup(app)

#@cli.command
#def custom_comment():
#    pass

manager = Manager(app)


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()
    

if __name__ == '__main__':
    manager.run()
#    cli()
