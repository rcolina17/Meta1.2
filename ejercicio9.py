#propina
pago = float(input("Cuanto a pagar? "))
propina = int(input ('La propina es 18%, 20%, 25%'))
print ('Solo pueden pagar 3 persons la cuenta')
personas = int(input('Cuantas personas pagaran la cuenta?'+'\n'))
if personas == 1:
    porcentaje = propina*.01
    total=(pago*porcentaje)+pago
    print ('Total a pagar: ',total)


elif personas == 2:
    porcentaje = propina*.01
    total=(pago*porcentaje)+pago
    print ('Total a pagar: ',total,)
    print ('Pagos de las personas')
    persona1= int(input('Cuanto porcentaje va a pagar la Persona 1: '+'\n'))
    x=persona1*.01
    porcentaje1 = total*x
    
    persona2= int(input('Persona 2: '))
    w=persona2*.01
    porcentaje2 = total*w
    print ('El pago es de: ',total ,'\nLa primera persona pago: ',porcentaje1, '\nLa segunda persona pago: ',porcentaje2)

elif personas == 3:
    porcentaje = propina*.01
    total=(pago*porcentaje)+pago
    print ('Total a pagar: ',total,)
    print ('Pagos de las personas')
    persona1= int(input('Persona 1: '))
    x=persona1*.01
    porcentaje1 = total*x
    
    persona2= int(input('Persona 2: '))
    w=persona2*.01
    porcentaje2 = total*w
    
    persona3= int(input('Persona 3: '))
    z=persona3*.01
    porcentaje2 = total*z
    print ('El pago es de: ',total ,'\nLa primera persona pago: ',porcentaje1, '\nLa segunda persona pago: ',porcentaje2,'\nLa tercera persona pago: ',porcentaje3)





