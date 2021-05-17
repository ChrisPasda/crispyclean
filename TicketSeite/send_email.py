from email.mime.text import MIMEText
import smtplib

def send_email(bam, numbers):
    from_email = "pasdachristopher@gmail.com"
    from_password ="I_lovemighty"
    to_email = "Christopher.Pasda@dkb-service.de"

    subject= "Buchung Notebooks"
    message = "Es wurden folgende Notebooks gebucht: %s Bam: %s " %(numbers, bam)
    print(message)
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
