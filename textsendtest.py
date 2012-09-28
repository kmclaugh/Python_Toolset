def textsender(number,message):

    import smtplib

    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( 'kevin.mclaughlin70@gmail.com', '1/2mv^2+1/2kx^2=E' )

    server.sendmail( 'kevin', '{0}@mms.att.net'.format(number), '{0}'.format(message) )


message = 'Hope youre having a good day!'
test = textsender(2145023694,message)
