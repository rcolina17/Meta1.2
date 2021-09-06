#acronimo
def main: 
    a = texto.split() 
    b = "" 
    for palabra in a:   
        b += palabra[0]    
    b = b.upper() 
    return b 

acronimo=input('Escribe el texto que quieres convertir acronimo: ')
print (main(acronimo))

"""def x(texto): 
    a = texto.split() 
    b = "" 
    for palabra in a:   
        b += palabra[0]    
    b = b.upper() 
    return b 

acronimo=input('Escribe el texto que quieres convertir acronimo: ')
print (x(acronimo))"""





