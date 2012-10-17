#demostrates how to capture exceptions with a traceback
import sys, traceback

def textsender(number,message):

    import smtplib

    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( 'antonshipley@gmail.com', 'F=kqq/r2' )

    server.sendmail( 'kevin', '{0}@mms.att.net'.format(number), '{0}'.format(message) )



def test():
    textsender(8173126800)
    return('good')

try:
    t = test()
    print(t)
except Exception as inst:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_inst = traceback.format_exception(exc_type, exc_value, exc_traceback)
    if inst.args == (8,'nodename nor servname provided, or not known'):
        print('no internet')
    else:
        tbstring = ''
        for line in exc_inst:
            tbstring = tbstring + line
        print(tbstring)

