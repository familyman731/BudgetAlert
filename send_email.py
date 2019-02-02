import smtplib
import BudgetAlert_config # in Python37-32\lib\site-packages

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(BudgetAlert_config.EMAIL_ADDRESS, BudgetAlert_config.PASSWORD)
        message = f'Subject: {subject}\n\n{msg}'
        server.sendmail(BudgetAlert_config.EMAIL_ADDRESS, BudgetAlert_config.RECIPIENTS, message)
        server.quit()
        print("Email successfully sent!")
    except:
        print("Email failed to send...")