from flask import Flask,render_template,current_app,render_template_string
from flask_script import Manager
from flask_mail import Mail,Message
import os
from .extensions import mail
from threading import Thread
app = Flask(__name__)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.163.com')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','liweiriver@163.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','liwei123')
mail = Mail(app)

manager = Manager(app)
def async_send_mail(app,msg):
    with app.app_context():

        mail.send(message=msg)

def send_mail(subject,to,tem,**kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])
    msg.html = render_template('email/'+tem+'.html',**kwargs)
    # msg.html = render_template_string('<h1>pleace touch this<a href="http://www.baidu.com">okokokok</a></h1>')
    mail.send(message=msg)
    thr = Thread(target=async_send_mail,args=(msg,))
    thr.start()



if __name__ == '__main__':
    manager.run()