import smtplib


class SendMail():
    def __init__(self):

        pass

    def send(mail_id):
       gmail_user = 'onor.register@gmail.com'
       gmail_pwd = 'Sprite123$'
       FROM = gmail_user
       recipient = mail_id
       TO = recipient if type(recipient) is list else [recipient]
       SUBJECT = 'User Registration'
       TEXT = 'succesfully registered as a user in our app'
       message = """From: %s\nTo: %s\nSubject: %s\n\n%s
       """% (FROM, ", ".join(TO), SUBJECT, TEXT)
       try:
           server = smtplib.SMTP("smtp.gmail.com", 587)
           server.ehlo()
           server.starttls()
           server.login(gmail_user, gmail_pwd)
           server.sendmail(FROM, TO, message)
           server.close()
           return ("success")
       except Exception as ex:
           return (ex)
