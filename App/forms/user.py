from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from werkzeug.security import generate_password_hash,check_password_hash
from App.models import User
class Register(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(message='用户名不嫩为空'),Length(min=2,max=12,message='用户名长度为6-12')],render_kw={
        'placeholder':'请输入用户名','maxlength':12
    })
    userpass = PasswordField('密码',validators=[DataRequired(message='密码不能为空'),Length(min=6,max=12,message='密码长度为6-16位'),EqualTo('userpass',message='两次不一致')],render_kw={'placeholder':'输入确认密码','maxlength':16})
    confirm = PasswordField('确认密码',validators=[DataRequired(message='确认密码不能为空'),Length(min=6,max=16,message='密码长度为6-12'),EqualTo('userpass',message='两次输入的密码不一致')],render_kw={'placeholder':'输入确认密码','maxlength':16})

    email = StringField('激活邮箱',validators=[Email(message='请输入正常的地址'),DataRequired(message='游戏不能为空')],render_kw={"placeholder":"请输入"})
    submit = SubmitField('注册')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户已注册')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已存在')

class AccountActivate(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(message='用户名不嫩为空'), Length(min=2, max=12, message='用户名长度为6-12')],
                           render_kw={
                               'placeholder': '请输入用户名', 'maxlength': 12
                           })
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=12, message='密码长度为6-16位'),
                                         EqualTo('userpass', message='两次不一致')],
                             render_kw={'placeholder': '输入确认密码', 'maxlength': 16})
    email = StringField('激活邮箱', validators=[Email(message='请输入正常的地址'), DataRequired(message='游戏不能为空')],
                        render_kw={"placeholder": "请输入"})
    submit = SubmitField('激活')

class Login(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(message='用户名不嫩为空'), Length(min=2, max=12, message='用户名长度为6-12')],
                           render_kw={
                               'placeholder': '请输入用户名', 'maxlength': 12
                           })
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=12, message='密码长度为6-16位'),
                                         EqualTo('userpass', message='两次不一致')],
                             render_kw={'placeholder': '输入确认密码', 'maxlength': 16})
    # email = StringField('激活邮箱', validators=[Email(message='请输入正常的地址'), DataRequired(message='游戏不能为空')],
    submit = SubmitField('登录')