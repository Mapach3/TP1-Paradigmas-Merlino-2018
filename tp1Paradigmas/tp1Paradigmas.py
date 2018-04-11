# Una calculadora basica que trabaja con 2 numeros
import calcubasic   #Libreria con funciones basicas
import os           # os que tiene el metodo system para limpiar pantalla

def showNumbers(a,b):
    """ 
        Muestra los numeros con los que se trabaja
        Parametro a: primer numero
        Parametro b: segundo numero
        return: Ninguno
        
    """                                       
    print "Los numeros que ingreso son ",a,"y",b,"."

def limpiar():
    """ Limpia la pantalla 
        Sin parametros
        return: Ninguno
        
        
    """                                              
    os.system("cls")
    
def setNumbers():
    """ Crea 2 variables a las que nosotros ingresamos los numeros con los que 
        trabajaremos
        Sin parametros
        Return: num1: Primer numero.
                num2: Segundo numero.
    
    
    """                                           
    print "Ingrese 2 numeros:"
    num1=int(input("Primer numero: "))
    num2=int(input("Segundo numero: "))
    return num1,num2
    

def menu(a,b):
    """Menu principal de la calculadora, desde donde se utiliza.
       Parametro a: Primer numero.
       Parametro b: Segundo numero.
       Return: Ninguno, vuelve al main.
    
    
    """
    print showNumbers(a, b)
    print "Elija operacion a realizar"
    print "1-Suma, 2-Resta, 3-Producto, 4-Division, 5- Salir"
        
    opcion=input("Opcion: ")
        
    if opcion == 1:
        print "El resultado es: ", calcubasic.suma(a, b)
    elif opcion == 2:
        print "El resultado es: ", calcubasic.resta(a, b)
    elif opcion == 3:
        print "El resultado es: ", calcubasic.producto(a, b)
    elif opcion == 4:
        print "El resultado es: ", calcubasic.division(a, b)
    elif opcion == 5:
        print "Decidio salir"
    else: print"Opcion incorrecta" 
            
            
        
        

def main():
    """Funcion main del programa.
       Sin parametros.
       Return: Ninguno.
    
    """
    print "Bienvenido"
    a,b=setNumbers()
    n=0
    seguir = "s" 
    
    while (seguir != "n"):
        menu(a,b)
        n+=1
        cambio = raw_input("Desea cambiar los valores? S/N: ")
        if cambio == "s":
            a,b=setNumbers()
        else: None

        seguir=raw_input("Desea continuar? S/N: ")
        limpiar()
    
    print "Gracias por usar la calcu, que tenga un buen dia. Realizo:",n,"operacion/es."
        

    
    
   
  
    
    
    
   
        
        
        
        
    
    

main()
