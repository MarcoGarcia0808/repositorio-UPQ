numero1= float(input("ingresa el número 1: "))
numero2= float(input("ingresa el número 2: "))
numero3= float(input("ingresa el número 3: "))

if numero1 > numero2 and numero1 > numero3:
    print("el mayor es el primer número")
    
elif numero2 > numero3:
    print("el mayor es el segundo número") 
    
else: print("el tercer número es el mayor")       