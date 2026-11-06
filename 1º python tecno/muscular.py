peso=float(input("Escribe tu peso en kg: "))
altura=float(input("Escribe tu altura en metros: "))
imc=peso/(altura)**2
if imc<=18.5:
    print (f"Tu índice de masa muscular es:{imc:.2f} y tienes un peso bajo.")
elif 18.5<imc<=25 :
    print (f"Tu índice de masa muscular es:{imc:.2f} y tienes un peso medio.")
elif 25<imc<=30 :
    print (f"Tu índice de masa muscular es:{imc:.2f} y tienes sobrepeso.")
elif 30<imc<=35 :
    print (f"Tu índice de masa muscular es:{imc:.2f} y tienes obesidad grado I.")
elif 35<imc<=40 :
    print (f"Tu índice de masa muscular es:{imc:.2f} y tienes obesidad grado II.")
else:
    print (f"Tu índice de masa muscular es:{imc:.2f} y tienes obesidad grado III.")