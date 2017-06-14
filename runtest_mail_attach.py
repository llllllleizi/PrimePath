from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
import sys

#=====================定义发送邮件====================
def send_mail (file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    smtpserver = "smtp.163.com"
    user = "imsy44@163.com"
    password = "shiyu18362963921"
    sender = "imsy44@163.com"
    receiver = "18303974@qq.com"
    subject = "自动化测试报告_施宇"
    # smtpserver = 'smtp.163.com'
    # user = 'imsy44@163.com'
    # password = 'shiyu19941116'
    # sender = 'imsy44@163.com'
    # receiver = '494780866@qq.com'
    # subject = '自动化测试报告_施宇'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(subject, 'utf-8')                      
    msgRoot['From'] = sender
    msgRoot['To'] = receiver

    msgRoot.attach(MIMEText('最新测试报告已到，请查收!', 'plain', 'utf-8'))

    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="new_report.html"'
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print ('email has send out !')


#=====查找测试报告目录，找到最新生产的测试报告文件========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print ('文件相对路径：' + file_new)
    return file_new


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    test_dir = 'test_case'
    test_report = 'report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = test_report + '/shiyu-' + now + '-result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,              
                        title='测试报告_施宇',               
                        description='用例执行状况：') 
    runner.run(discover)   
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)   # 发送测试报告
