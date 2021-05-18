import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMail(bam, number):
   fromaddr = "pasdachristopher@gmail.com"
   toaddr = "pasda.berlin@googlemail.com"

# instance of MIMEMultipart
   msg = MIMEMultipart()

# storing the senders email address
   msg['From'] = fromaddr

# storing the receivers email address
   msg['To'] = toaddr

# storing the subject
   msg['Subject'] = "Buchung von Notebooks"

# string to store the body of the mail
   body = "Es wurden folgende Notebooks gebucht: %s Bam: %s " %(number, bam)

# attach the body with the msg instance
   msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
   filename = "test1.docx"
   attachment = open("C:\\Users\\Chris\\github\\crispyclean\\TRY\\TicketSeite\\test1.docx", "rb")

# instance of MIMEBase and named as p
   p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
   p.set_payload((attachment).read())

# encode into base64
   encoders.encode_base64(p)

   p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
   msg.attach(p)

# creates SMTP session
   s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
   s.starttls()

# Authentication
   s.login(fromaddr, "PASSWORD")

# Converts the Multipart msg into a string
   text = msg.as_string()

# sending the mail
   s.sendmail(fromaddr, toaddr, text)

# terminating the session
   s.quit()

