#
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


fromaddr = 'kevin.mclaugh70@gmail.com'
toaddr = "kevin.mclaughlin70@gmail.com"

# Create a text/plain message
partt=MIMEText("Dear J")

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'This is the subject line'
msg.attach(partt)
print(msg)
 
##fname="adocument.pdf"
##partpdf=MIMEApplication(open(fname,"rb").read())
##partpdf.add_header('Content-Disposition', 'attachment', filename=fname)
##msg.attach(partpdf)
##print(msg)
##quit()
# send the message
import smtplib 

username='kevin.mclaughlin70@gmail.com'
password=input('1/2mv^2+1/2kx^2=E')

server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromaddr, [toaddr], msg.as_string())  
server.quit()  

