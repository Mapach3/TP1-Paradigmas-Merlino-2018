# Libreria de operaciones matematicas basicas

def suma(a,b):
    """Realiza la suma entre dos operandos
       Parametro a: Primer operando
       Parametro b: Segundo operando
       Return: La suma de ambos operandos"""
    return a+b


def resta(a,b):
    """Realiza la diferencia entre dos operandos
       Parametro a: Primer operando
       Parametro b: Segundo operando
       Return: Diferencia entre los operandos"""             
    return a-b

def producto(a,b):
    """Realiza el producto entre dos operandos
       Parametro a: Primer operando
       Parametro b: Segundo operando
       Return: Producto de ambos operandos"""          
    
    return a*b

def division(a,b):
    """Realiza la division entre dos operandos. Si el divisor es 0 devuelve un mensaje de error.
       Parametro a: Primer operando
       Parametro b: Segundo operando
       Return: El cociente entre dos operandos en caso de que el divisor NO SEA 0"""
       
    if b == 0:
        print "Como vas a dividir por 0?!?!?"
    else:
        return float((float(a))/(b))  #transformar un parametro en float pq sino hace la division entera 



    
    