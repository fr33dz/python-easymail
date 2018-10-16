import time, smtplib
 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
class EasyMail(object):
        
        def __init__(self):
            pass

        @classmethod
        def login(cls, smtp_server='smtp.gmail.com', user, password):
            instantiate = cls()
            self.smtp_user = user
            self.smtp_pass = password
            self.smtp_server = smtp_server
            return instantiate
           
        def send(self, to, subject, text):
            try:
                msg = MIMEMultipart()
                text = MIMEText(text, 'html')
                msg['Subject'] = subject
                msg['To'] = to
                msg['From'] = self.smtp_user
                msg.attach(text)

                print "subjet:%s from: %s to: %s smtp server : %s"%(subject, to, self.smtp_user, self.smtp_server)
                print 'connection to server'
                s = smtplib.SMTP_SSL(self.smtp_server)
                print 'authentification...'
                s.login(self.smtp_user, self.smtp_pass)
                print 'connection established : sending mail...'
                s.sendmail(self.smtp_user, [to], msg.as_string())
                s.quit()
                print "message sent"
                return True
            except Exception as e:
                print e

