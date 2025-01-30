from email.message import EmailMessage
import smtplib
import ssl

# Lendo a senha do arquivo
password = open('senha', 'r').read()
from_email = 'orbiweb17@gmail.com'
to_email = 'gustavojeronimo17@gmail.com'
subject = 'teste 2.0'
body = open('files/corpo.txt', 'r', encoding='utf-8').read()

# Montando a estrutura do Email
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)

# Criando o contexto de segurança
safe = ssl.create_default_context()

# Envio do Email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()  # Certifique-se de que toda a mensagem é enviada corretamente
    )
