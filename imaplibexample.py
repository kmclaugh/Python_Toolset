import email, getpass, imaplib, os

class jarvismail:
    def __init__(self,messageID,From,To,Date,Subject,Body):
        self.ID = messageID
        self.F = From
        self.T = To
        self.D = Date
        self.S = Subject
        self.B = Body
    def __str__(self):
        return 'From: %s,\n\nTo: %s,\n\nDate: %s\n\nSubject: %s:\n\n%s' % (self.F,self.T,self.D,self.S,self.B)

##h = jarvismail('1','test@test','test@test','today','test','test test')
##print(h)
        

from email.parser import HeaderParser
username = 'ieatchipotle'
password = 'chrismas'
M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
M.login(username, password)
M.select()
typ, items = M.search(None, 'ALL')
idlist = items[0].split()

for num in idlist:
    resp, data = M.FETCH(num, '(RFC822)')
    try:
        email_body = data[0][1].decode() # getting the mail content
    except:
        email_body = data[0][1].decode('latin-1') # getting the mail content
    mail = email.message_from_string(email_body)
    for part in mail.walk():
        if part.get_content_maintype() == 'text':
            Body = part.get_payload()
            break
    Subject = mail['Subject']
    Date = mail['date']
    To = mail['Delivered-To']
    From = mail['From']
    messageID = mail['Message-ID']
    jmessage = jarvismail(messageID,From,To,Date,Subject,Body)
    print(jmessage)
    break
            
M.close()
M.logout()


