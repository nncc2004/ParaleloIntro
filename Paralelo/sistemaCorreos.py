#importaciones para acceder a BBDD y programar las tareas
import os
import sys
import django
import schedule
import time
from datetime import datetime

#importaciones para el envió de email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sys.path.append('Paralelo/')  # Adjust the path to your Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Paralelo.settings')
django.setup()

from BBDD.models  import *
from django.contrib.auth.models import User


print("iniciado el sistema de correos")
def envioCorreos():
    dato = User.objects.all()
    fechaActual = str(datetime.now().date()).split("-")
    anioActual = int(fechaActual[0])
    mesActual =  int(fechaActual[1])
    diaActual = int(fechaActual[2])
    DosDias = []
    UnMes = []
    for usuario in dato:
        ultimoLogin = str(usuario.last_login).split(" ")[0].split("-")
        #print("User:",usuario, "Email:", usuario.email, "Last login: ", ultimoLogin)
        anio = int(ultimoLogin[0])
        mes = int(ultimoLogin[1])
        dia = int(ultimoLogin[2])
        if anio == anioActual and mes == mesActual and dia+2 == diaActual:
            DosDias.append([usuario.username, usuario.email])
        elif anio == anioActual and dia == diaActual and mes+1 == mesActual:
            UnMes.append([usuario.username, usuario.email])
            
    print(DosDias)
    print(UnMes)

    for usuariosDosDias in DosDias:
        sender_email = "nncc2004@gmail.com"
        receiver_email = usuariosDosDias[1]
        subject = "Prueba Email"
        body = "Hola " + usuariosDosDias[0] + ". Han pasado dos días desde tu última sesión de estudio!! Conéctate y sigue aprendiendo!"

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "nncc2004@gmail.com"
        smtp_password = "fhkg tpdu zjvh qlxg"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS for security
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email enviado")

    for usuarioUnMes in UnMes:
        sender_email = "nncc2004@gmail.com"
        receiver_email = usuarioUnMes[1]
        subject = "Prueba Email"
        body = "Hola " + usuarioUnMes[0] + ". Han pasado dos días desde tu última sesión de estudio!! Conéctate y sigue aprendiendo!"

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "nncc2004@gmail.com"
        smtp_password = "fhkg tpdu zjvh qlxg"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS for security
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email enviado")
    print("----------------------------------------------------------------------------------------------")
    

schedule.every(10).seconds.do(envioCorreos)

while True:
    schedule.run_pending()
    time.sleep(1)