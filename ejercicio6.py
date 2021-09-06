#pierda papel o tijeras
from random import randint

opciones=['piedra','papel','tijeras']
maquina=opciones[randint(0,2)]
jugador=input('Escribe piedra papel o tijeras: ').lower()
print('La maquina escogio: '+maquina)

if jugador == maquina:print('Empate')
elif jugador=='piedra' and maquina=='papel':print ('Gano la maquina')
elif jugador=='piedra' and maquina=='tijeras':print ('Gano el jugador')
elif jugador=='papel' and maquina=='piedra':print ('Gano el jugador')
elif jugador=='papel' and maquina=='tijeras':print ('Gano la maquina')
elif jugador=='tijeras' and maquina=='piedra':print ('Gano la maquina')
elif jugador=='tijeras' and maquina=='papel':print ('Gano el jugador')


