n = int(input())
minutos = 60
horas =  3600
if n >= horas:
    calculo0 = n // horas
    calculo1 = (n % horas) // minutos
    calculo2 = (n % horas) % minutos
    print(f"{calculo0}:{calculo1}:{calculo2}")
elif n < 3600 and n >=60:
    calculo_h = 0
    calculo = n // 60
    calculo1 = n % 60
    print(f"{calculo_h}:{calculo}:{calculo1}")
else:
   calculo_h = 0
   calculo_m = 0
   calculo1 = n
   print(f"{calculo_h}:{calculo_m}:{calculo1}") 