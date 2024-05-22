monto_compra= float(input("ingresa el monto de la compra"))
if monto_compra>=100:
     
   descuento= monto_compra*(float(input("ingresa el porcentaje de descuento"))/100)
   monto_compra-=descuento
   print("se aplica el descuento de", descuento, "pesos")
else:
    print("no se aplica descuento")