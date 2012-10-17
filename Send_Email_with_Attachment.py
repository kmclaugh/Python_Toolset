##copied from:
##http://jackal777.wordpress.com/2011/07/19/sending-emails-via-gmail-with-python3/

import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def send_mail(to, subject, text, attach):

    gmail_user = 'antonshipley@gmail.com'
    gmail_pwd = 'F=kqq/r2'
    
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject




    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()

##test
##attachment = '/Users/kevin/Library/Jarvis/BalanceUpdater/RachaelGoogleDocsUdater.csv'
##sendto = 'kevin.mclaughlin70@gmail.com'
##send_mail(sendto,'test','test of python send',attachment)
