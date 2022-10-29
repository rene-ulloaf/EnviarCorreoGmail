###Recibir e-mail Gmail

def autoriza(popHost, miuser, mipass):

    import poplib
    try:
        pop = poplib.POP3_SSL(popHost, 995)
        
    except:
        raise RuntimeError("no se establecio la coneccion"
                           "a %r problema al conectar al host " % popHost)
    try:
        pop.user(miuser)
        pop.pass_(mipass)
        numeromensajes = len(pop.list()[1])
        if (numeromensajes == 0):
            print "No hay mensajes :( "
        else:
            for i in range(numeromensajes):
                for j in pop.retr(i+1)[1]:
                    print j
        
        pop.quit()
    except:
        raise RuntimeError("no se verifico a identidad "
                           "usuario %r o pass incorrecto"  %  miuser)
        pop.quit()
        
autoriza("pop.gmail.com", "micuenta@gmail.com", "mipassworddegmail")


###Enviar e-mail Gmail

import smtplib
from email.mime.text import MIMEText
mensajito = raw_input('su mensajito : ')
tema = raw_input('tema : ')
destino = raw_input('destino : ')
mensaje = MIMEText(mensajito)
mensaje['Subject'] = tema
smtpserver = 'smtp.gmail.com'
smtpuser = 'sucuentagmail@gmail.com'  # su usuario de gmail
smtppassword = "supassdegmail" # su password de gmail
SENDER = "sucuentagmail@gmail.com" # su usuario de gmail
RECIPIENTS = destino
session = smtplib.SMTP(smtpserver, 587)
session.ehlo()
session.starttls()
session.ehlo()
session.login(smtpuser, smtppassword)
session.sendmail(SENDER, RECIPIENTS, mensaje.as_string())
session.quit()