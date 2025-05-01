# Enviando e-mail com Python
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
load_dotenv()

# Remetente
remetente = os.getenv('FROM_EMAIL', '')

# Destinatário
destinatario = input('Digite o email do destinatario: ')

# Assunto
assunto = input('Digite o assunto do email: ')

# Mensagem
mensagem = input('Digite a mensagem do email: ')

# Configuração do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = remetente
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Criação da mensagem
mime_multipart = MIMEMultipart()
mime_multipart['From'] = remetente
mime_multipart['To'] = destinatario
mime_multipart['Subject'] = assunto
mime_multipart.attach(MIMEText(mensagem, 'plain'))

# Enviando o email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!')
