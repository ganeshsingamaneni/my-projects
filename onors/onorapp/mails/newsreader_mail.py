import smtplib
from django.http import JsonResponse,HttpResponse
import email.mime.application
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class news_email():
    def __init__(self):
        pass
    def send():
       fromaddress = "onor.register@gmail.com"
       toaddress = "manyamraghuram@gmail.com"
       password = "Sprite123$"
       message = MIMEMultipart()
       message['From'] = fromaddress
       message['To'] = toaddress
       message['Subject'] = "SUBJECT OF THE EMAIL"
       body = "TEXT YOU WANT TO SEND"
       message.attach(MIMEText(body, 'plain'))
       filename = "Newsreader.csv"
       attachment = open("/home/ganesh/dev3/onor/onors/onorapp/files/newsreader.csv", "rb")
       part = MIMEBase('application', 'octet-stream')
       part.set_payload((attachment).read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
       message.attach(part)
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.starttls()
       server.login(fromaddress, password)
       text = message.as_string()
       server.sendmail(fromaddress, toaddress, text)
       server.quit()
       return HttpResponse('success')
