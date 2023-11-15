'''
from django.db import models
from background_task import background
i = 0
@background(schedule=1) #tiempo en segundos
def enviarCorreos():
    print("correo", i)
    i +=1
    '''