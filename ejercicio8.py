def A():
    texto = input("\nIngresa una palabra en polindromo: ") 
    w = texto.lower() 
    x = list(w) 
    return x

def B(lista): 
    np = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for caracter in np: 
        if caracter in lista: 
            lista.remove(caracter) 
            return B(lista)
    return lista 

def C(lista2):
    y = lista2[::-1] 
    if y == lista2: 
        return "La palabra que pusiste es un palindromo" 
    else: 
        return "La palabra que pusiste no es un palindromo" 

def main(): 
    print("\nRevision") 
    org = A()
    org = B(org) 
    palindromo = C(org)
    print(palindromo)

main()