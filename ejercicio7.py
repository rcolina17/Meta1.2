#adivina el numero
import random
maquina=random.randrange(1,50)
# print(maquina)
jugador=int(input('Dame un numero del 1 al 50: '))
while jugador !=maquina:
    if jugador<maquina: 
        jugador=int(input ('Dame un numero mas grande '))
    elif jugador>maquina: 
        jugador= int(input ('Dame un numero mas pequeno '))
else: print('Adivinaste el numero')




    
