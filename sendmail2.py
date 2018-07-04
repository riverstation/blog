from flask import Flask,render_template,render_template_string
from flask_script import Manager
from flask_mail import Mail,Message
import os
from threading import Thread
app = Flask(__name__)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.163.com')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','liweiriver@163.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','liwei123')
mail = Mail(app)

manager = Manager(app)
def async_send_mail(msg):
    with app.app_context():

        mail.send(message=msg)
@app.route('/send_mail/')
def send_mail():
    msg = Message(subject='mail to ok:',recipients=['157723676@qq.com'],sender=app.config['MAIL_USERNAME'])
    msg.html = render_template_string('<h1>pleace touch this<a href="http://www.baidu.com">okokokok</a></h1>')
    mail.send(message=msg)
    thr = Thread(target=async_send_mail,args=(msg,))
    thr.start()
    return render_template_string('发送')


if __name__ == '__main__':
    manager.run()