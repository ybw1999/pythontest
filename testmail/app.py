from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)


#　下面是SMTP(发送邮箱)服务器配置
# 电子邮箱服务器的主机名或IP地址
app.config['MAIL_SERVER'] ='smtp.126.com'
# 电子邮箱服务器的端口
app.config['MAIL_PORT'] =25
# 使用ＴＬＳ启用传输层安全
app.config['MAIL_USE_TLS'] =True    # 这里启用的是TLS协议,不是SSL(加密)协议，所以是25号端口
# 自己的邮件账户用户名
app.config['MAIL_USERNAME'] ='ybw1999724@126.com'
# 邮件账户的密码,这个密码是指的授权码
app.config['MAIL_PASSWORD'] ='p0o9i8'

# 创建mail对象
mail =Mail(app)


@app.route('/')
def index():
    # 这里的sender是发信人,写上发信人的名字,例如zhangsan       # recipients是收信人,用一个列表去表示
    msg =Message('我是大标题',sender='ybw1999724@126.com',recipients=['2450263494@qq.com'])
    msg.body='你好'
    # 发送邮件的内容
    msg.html ='<b>啦啦啦</b>'
    # 发送邮件
    mail.send(msg)

    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
    app.run()
    num1 =10
    num2 =20
