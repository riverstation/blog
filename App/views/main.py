from flask import Blueprint,current_app,render_template
main = Blueprint('main',__name__)
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize

@main.route('/')
def index():
    hash_password = generate_password_hash('123456')
    print(check_password_hash(hash_password,'123456'))
    s = Seralize(current_app.config['SECRET_KEY'])
    print(s)
    token = s.dumps({'id':1})
    return token
    # return current_app.config['SECRET_KEY']
    # return 'index'
