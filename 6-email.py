from email.message import EmailMessage
import smtplib
import ssl

password = open ('senha', 'r').read()


from_email = 'orbiweb17@gmail.com'
to_email = 'gustavojeronimo17@gmail.com'
subject = 'teste'
body = '''Essa mensagem é um teste'''

#Estruturando a mensagem via email

message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)

safe = ssl.create_default_context()

#Envio de Email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string() # convertendo a mensagem para String
    )



