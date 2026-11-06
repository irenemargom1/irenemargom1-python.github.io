contrasena = ''
contrasena=input("Introduce la contraseña: ")
contador=3
while contrasena != 'mercedes' and contador>0:
    print ("Acceso denegado") 
    if contrasena!='mercedes':
        contador-=1
        print(f'Te quedan {contador} intentos.')
    contrasena=input("Introduce la contraseña: ")
else:
    if contador <=0:
        print("Acceso denegado.")
    else:
        print ("¡Acceso concedido!")