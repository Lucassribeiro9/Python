import os
import time
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib

# Definindo a leitura das tarefas
def ler_atividades():
    with open('atividades.json', 'r', encoding='utf-8') as f:
        atividades = json.load(f)
    return [a for a in atividades if a['data'] == time.strftime('%d/%m/%Y')]

def ler_tarefas():
    with open('tarefas.json', 'r', encoding='utf-8') as f:
        tarefas = json.load(f)
    return tarefas

def gerar_relatorio():
    atividades = ler_atividades()
    tarefas = ler_tarefas()
    
    nome_arquivo = "relatorio_{}.pdf".format(time.strftime('%d-%m-%Y'))
    pdf_path = os.path.join(os.getcwd(), 'relatorios', nome_arquivo)

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(200, 750, 'Relatório de Atividades')
    c.drawString(200, 730, 'Data: {}'.format(time.strftime('%d/%m/%Y')))
    
    y = 700
    c.drawString(50, y, 'Atividades do dia:')
    y -= 20
    for atividade in atividades:
        c.drawString(30, y, f"- {atividade['nome']} - {atividade['descricao']} - {atividade['data']}")
        y -= 15

    y -= 20
    c.drawString(50, y, 'Tarefas:')
    y -= 20
    for tarefa in tarefas:
        c.drawString(30, y, f"- {tarefa['nome']} - {tarefa['descricao']} - {tarefa['status']}")
        y -= 15

    c.save()
    return pdf_path