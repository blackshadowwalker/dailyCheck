# coding: UTF-8

import smtplib

from Config import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# if Email.send_mail(mailto_list, "hello", "hello world！"):
#     print("发送成功")
# else:
#     print("发送失败")

class Email:

    config = Config()

    def setConfig(self,config):
        self.config = config

    def send_mail(self, title, content=None, files=None):
        me = Header(self.config.nick_name, 'utf-8')
        me.append("<" + self.config.mail_user + "@" + self.config.mail_postfix + ">", 'ascii')
        #创建一个带附件的实例
        msg = MIMEMultipart()
        #msg = MIMEText(content, _subtype='plain', _charset='gb2312')
        msg['Subject'] = title
        msg['From'] = me
        msg['To'] = ";".join(self.config.mailto_list)
        try:

            text = MIMEText(content, 'plain', 'utf-8')
            msg.attach(text)

            if files!=None:
                for file in files:
                    #构造附件
                    att = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
                    att["Content-Type"] = 'application/octet-stream'
                    att["Content-Disposition"] = 'attachment; filename="'+file+'.txt"'
                    msg.attach(att)

            server = smtplib.SMTP()
            server.connect(self.config.mail_host)
            server.login(self.config.mail_user, self.config.mail_pass)
            server.sendmail(self.config.mail_from, self.config.mailto_list, msg.as_string())
            server.close()
            print('success send email ' + title)
            return True
        except Exception as e:
            print(e)
            return False