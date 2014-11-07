import smtplib

class Config():
    def __init__(self):


        #Enter your spam gmail account username here:
        Gmail_account_username = ""

        #Enter your spam gmail account password here:
        Gmail_account_password = ""

        #If you would like a default spam message, enter it here:
        self.Default_spam_message = ""








        self.Google_server = smtplib.SMTP('smtp.googlemail.com',587)
        self.Google_server.starttls()
        self.Google_server.login(Gmail_account_username, Gmail_account_password)
        
