from flask import redirect,url_for, Blueprint,Flask,flash,render_template
from App.forms import Register,Login,AccountActivate
from App.models import User
from App.extensions import db
from App.email import send_mail
from flask_login import login_required,login_user,logout_user,current_user

user = Blueprint('user',__name__)


@user.route('/register/',methods=['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        u = User(username=form.username.data,password=form.userpass.data,email=form.email.data)

        db.session.add(u)
        db.session.commit()
        token = u.generate_token()
        # return token
        send_mail('activate email',form.email.data,'activate',usernam=form.username.data,token=token,urlFor='user.activate')
        flash('注册成功，请注意查收')
        return redirect(url_for('user.login'))
    return render_template('user/regist.html',form=form)
@user.route('/activate/<token>/')
def activate(token):
    if User.check_token(token):
        flash('激活成功，请登录')
        return redirect(url_for('user.login'))
    else:
        flash('激活失败，请重新登录')
        return redirect(url_for('user.register'))

@user.route('/accountactivation/',methods=['GET','POST'])
def accountactivation():
    form = AccountActivate()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data,email=form.email.data).first()
        if not u:
            flash('请输入正确的信息')
        elif not u.confirm:
            flash('该账户已经激活，请去登录')
        elif not u.check_password(form.userpass.data):
            flash('您输入的密码有误')
        else:
            token = u.generate_token()
            send_mail('activate email', form.email.data, 'activate', usernam=form.username.data, token=token,
                      urlFor='user.activate')
            flash('激活成功，请登录')
    render_template('user/accountactivate.html',form=form)


@user.route('/login/',methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        u = User.query.filter_by(username = form.username.data)
        if not u:
            flash('当前用户不存在')
        elif not u.confirm:
            flash('未激活')
        elif not u.check_password(form.userpass.data):
            flash('请输入正确的密码')
        else:
            pass
            logout_user(u)
            flash('登录成功')
            return redirect(url_for('main.index'))

    return render_template('user/login.html',form=form)
