from App.extensions import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize
from flask_login import UserMixin
from App.extensions import login_menager
class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(13),unique=True)
    password_hash = db.Column(db.String(128))
    age = db.Column(db.Integer,default=18)
    sex = db.Column(db.Boolean,default=True)
    email = db.Column(db.String(128))
    icon = db.Column(db.String(64),default='default.jpg')
    confirm = db.Column(db.Boolean,default=False)

    @property
    def password(self):
        raise ArithmeticError('属性不存在')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def generate_token(self):
        s = Seralize(current_app.config['SECRET_KEY'])
        return s.dumps({'id':self.id})
    @staticmethod
    def check_token(token):
        try:
            s = Seralize(current_app.config['SECRET_KEY'])
            Dict = s.loads(token)
            uid = Dict['id']
            u = User.query.get(uid)
            if not u:
                raise ValueError
        except:
            return False
        if not u.confirm:
            u.confirm = True
            db.session.add(u)

        return True



    def check_password(self,password):
        return check_password_hash(self.password_hash,password)



@login_menager.user_loader
def user_loader(uid):
    return