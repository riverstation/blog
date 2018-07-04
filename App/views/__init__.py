from .main import main
from .user import user

defalut_blueprint = [
    (main,''),
    (user,''),

]
#
def blueprint_register(app):
    for blueprint,url_prefix in defalut_blueprint:
        app.register_blueprint(blueprint,url_prefix=url_prefix)
    # app.regist_blueprint('main')
    # app.regist_blueprint('user')

