import smtplib

class Mail:

    def __init__(self):
        self.port = 587
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "erwanformationia@gmail.com"
        self.password = "UT72M69aEpEU9Mw"

    def send(self, from_who, subject, content):
        
        service = smtplib.SMTP(self.smtp_server_domain_name, self.port)
        service.starttls()
        service.login(self.sender_mail, self.password)
        service.sendmail(self.sender_mail, from_who , f"Subject: {subject}\n{content}")
        service.quit()


if __name__ == '__main__':
    mail = Mail()
    mail.send('erwantanguyguiss@gmail.com', 'test', 'ceci estr zliksfd')





