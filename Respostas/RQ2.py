import time

hora_atual = time.time()
segundos1 =  int(hora_atual%60)
minuto1 = int(hora_atual//60)

horas = minuto1//60

dias = horas//24

print(f'Segundos: {segundos1}; Minutos: {minuto1%60}; Horas: {horas%24}; Dias: {dias};')