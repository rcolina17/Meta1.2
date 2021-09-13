#Biografia
from datetime import datetime

nombre=input('Cual es tu nombre '+'\n')
if nombre.isalpha():
    print ('Nombre: ',nombre)
else:
    print('Solo se permiten letras')

fechaN=input('Cual es tu fecha de nacimiento? Dia/Mes/Año'+'\n')
fechaN2=datetime.strptime(fechaN,'%d/%m/%Y')
print ('Tu fecha de nacimiento es: ',fechaN)




