secreto= ''
secreto= int(input("Introduce el número secreto: "))
intentos=0
while secreto != 14:
    print(f"El número {secreto} es incorrecto")
    if secreto!= 14:
        intentos+=1
        print(f'El número de intentos es: {intentos}')
    secreto= int(input("Introduce el número secreto: "))
print('Número correcto.')
print(f'Has necesitado {intentos} intentos.')



