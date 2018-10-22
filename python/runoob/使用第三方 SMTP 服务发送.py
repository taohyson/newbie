import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='541885431@qq.com'
my_pass = 'aogeyydlzwkbbcga'
my_user='zhujw@mapbar.com'
def mail():
    ret=True
    try:
        msg=MIMEText('test','plain','utf-8')
        msg['From']=formataddr(["FromRunoob",my_sender])
        msg['To']=formataddr(["FK",my_user])
        msg['Subject']="test"
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender,[my_user,],msg.as_string())
        server.quit()
    except Exception:
        ret=False
    return ret
 
ret=mail()
if ret:
    print("successed")
else:
    print("failed")