import time, smtplib
 
from email.mime.text import MIMEText
 
class EasyMail(object):
        
        def __init__(self):
            pass

        @classmethod
        def loggin(cls, user, password):
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

        def send(self, to, subject,text):
            try:
                msg = MIMEText(text)
                msg['Subject'] = subject
                msg['To'] = to
                msg['From'] = self.smtp_user
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
            except Exception:
                return False

def get_sended():
    try:
        mail_sended=''
        rea = open('./log.txt', 'rb')
        for line in rea:
            mail_sended += line
        rea.close()
        return mail_sended
    except:
        print 'no hay log'


mail_inst = EasyMail.loggin('ikerocio@gmail.com', '8fOtIhE4+@Gm')

logout = open('./log.txt', 'a')
namesfile = open('./nombres.txt', 'rb')

mail_sended = get_sended()
aux = 0
url = 'http://bodalaurayaitor.com/?invitation='
tipo = ''
emails = []
names = []
types = []
urls = []
for line in namesfile:
    if aux%3 == 0:
        url+= line.replace(',','+').replace(" ", "")
        urls.append(url)
        names.append(line)
    elif aux%3 == 1:
        tipo = line
        types.append(tipo)
    elif aux%3 == 2:
        if line.replace('\n', '') not in mail_sended:
            logout.write("%s"%line)
            mail_inst.send(line, 'BODA', 'entra aqui: '+url)
        url = 'http://bodalaurayaitor.com/?invitation='
        tipo = ''
        email = ''
    aux+=1
namesfile.close()
logout.close()
