import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'zhujw@mapbar.com'
receivers = ['541885431@qq.com']

message = MIMEText('Python send a test mail...', 'plain', 'utf-8')
message['Subject'] = Header('Python SMTP mail test', 'utf-8')
message['From'] = Header("test", 'utf-8')
message['To'] =  Header("test", 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "Success"
except smtplib.SMTPException:
    print "Error"