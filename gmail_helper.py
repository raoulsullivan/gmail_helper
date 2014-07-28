class simple_gmail_mailer():
    def __init__(self,gmailUsername, gmailPassword, fromAddress='reporting@fundingoptions.com',toAddresses=[]):
        if (not gmailUsername) or (not gmailPassword):
            raise ValueError('Must have a username and password')
        self.fromAddress = fromAddress
        self.toAddresses = toAddresses
        self.gmailUsername = gmailUsername
        self.gmailPassword = gmailPassword

    def send_mail(self,subject,message,toAddresses=[]):
        """Actually sends an email"""
        toAddresses = toAddresses or self.toAddresses
        if len(toAddresses) == 0:
            raise ValueError('No addresses provided to send to')

        msg = ("From: {0}\r\nTo: {1}\r\nSubject: {2}\r\n\r\n{3}\r\n".format(self.fromAddress, ", ".join(toAddresses), subject,message))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(0)
        server.ehlo()
        server.starttls()
        server.login(gmail_username, gmail_password)
        server.sendmail(self.fromAddress, toAddresses , msg)
        server.quit()
        return(True)
