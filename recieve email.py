import poplib
from email import parser

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('antonshipley')
pop_conn.pass_('F=kqq/r2')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
##messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
##messages = [parser.Parser().parsestr(mssg) for mssg in messages]
counter = 0
for message in messages:
    for m in message[1]:
        print(m.decode())
        
##        if counter == 35 or counter == 43:
##            print(m.decode())
        counter = counter +1
pop_conn.quit()
