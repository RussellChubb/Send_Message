'''
import smtplib
from email.message import EmailMessage
from emailToSMSConfig import senderEmail, gatewayAddress, appKey

msg = EmailMessage()
msg.set_content("wsup wit it")

msg['From'] = 'russell.d.chubb@gmail.com'
msg['To'] = '0212989942@mtxt.co.nz' #'642102832101@mtxt.co.nz'
msg['Subject'] = 'Sending this via code lol'

server = smtplib.SMTP("smtp.gmail.com")
server.starttls()
server.login("russell.d.chubb@gmail.com", "envd nbzt kkqo ukty")

server.send_message(msg)
server.quit()
'''

import smtplib

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("russell.d.chubb@gmail.com", "envd nbzt kkqo ukty")
smtpObj.sendmail("russell.d.chubb@gmail.com", "russell.d.chubb@gmail.com", "Subject: rahh \n sup")
smtpObj.quit()