#correo
correo=input('Escribe tu correo ').strip()
nomUsuario=correo[:correo.index('@')]
nomDominio=correo[correo.index('@')+1:]
salida="Tu correo es: '{}'\nTu dominio es '{}'".format(nomUsuario,nomDominio)
print (salida)