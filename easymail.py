import time, smtplib
 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
 
class EasyMail(object):
        
        def __init__(self):
            pass

        @classmethod
        def login(cls, user, password):
            instantiate = cls()
            instantiate.set_server(user, password)
            return instantiate

        def set_server(self, user, password):
            self.smtp_user = user
            self.smtp_pass = password
            smtp = {'gmail': 'smtp.gmail.com',
                    'hotmail': 'smtp.live.com',
                    'outlook': 'smtp.live.com',
                    'yahoo': 'smtp.mail.yahoo.com',
                    }
            if 'yahoo' in user:
                self.smtp_server = smtp['yahoo']
            elif 'gmail' in user:
                self.smtp_server = smtp['gmail']
            elif 'hotmail' or 'outlook' in user:
                self.smtp_server = smtp['hotmail']


        def send(self, to, subject, text, path='default'):
            try:
                msg = MIMEMultipart()
                text = MIMEText(text, 'html')
                msg['Subject'] = subject
                msg['To'] = to
                msg['From'] = self.smtp_user
                msg.attach(text)
                if 'default' not in path:
                    fp = open(path, 'rb')
                    img = MIMEImage(fp.read())
                    fp.close()
                    img.add_header('Content-ID', path)
                    msg.attach(img)
                print "sujeto:%s origen: %s destino: %s servidor de smtp: %s"%(subject, to, self.smtp_user, self.smtp_server)
                print 'conectando a servidor'
                s = smtplib.SMTP_SSL(self.smtp_server)
                print 'logueando...'
                s.login(self.smtp_user, self.smtp_pass)
                print 'logeado: enviando mail...'
                s.sendmail(self.smtp_user, [to], msg.as_string())
                s.quit()
                print "Mail enviado"
                return True
            except Exception as e:
                print e

