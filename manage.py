from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from src import app
from src.settings import db, DEBUG


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)



@manager.command
def runserver():
    app.run(debug=DEBUG)

@manager.command
def dbcreate():
    db.create_all()
    
if __name__ == '__main__':
    manager.run()