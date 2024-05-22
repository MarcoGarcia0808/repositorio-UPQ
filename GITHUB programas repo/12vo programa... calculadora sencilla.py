a = float(input("ingresa el primer número: "))
b = float(input("ingresa el segundo número: "))
operación = input("ingresa la operación que deseas realizar (+, -, *, /): ")

if operación == '+':
   resultado = a + b
   
elif operación == '-':
   resultado = a - b 

elif operación == '*':
   resultado = a * b 
  
  elif operación == '/':
   resultado = a / b  
  
if b != 0:
   resultado = a * b
  
  