from flask import Flask,url_for,render_template,render_template_string
from flask_script import Manager
from App import create_app
from flask_migrate import MigrateCommand

app = create_app('default')
manager = Manager(app)
manager.add_command('db',MigrateCommand)



@app.route('/')
def index():
    render_template('App/templates/common/base.html')

if __name__ == '__main__':
    manager.run()


