#Ejercicio 1
frutas=["Melocotón","Pera","Sandía","Naranja","Melón"]
for nombre in frutas:
    print(nombre)

#Ejercicio 2
buscado=['1','2','3','4','5']
numbuscado=input("Introduce un número: ")
if numbuscado in buscado:
    print(f"El número {numbuscado} está en la lista.")
else:
    print(f"El número {numbuscado} no está en la lista.")

#Ejercicio 3
nombres=['Ana','Clara','Darío','Irene','Mercedes']
contador=0
for nombre in nombres:
    if len (nombre)>=4:
        contador+=1
print(f'Hay {contador} nombres que tienen 4 letras o más.')

#Ejercicio 4
invitados=[]
inv=input("Introduce el nombre de un invitado o fin para terminar: ")
while inv != "fin":
    invitados.append(inv)
    print (invitados)
    inv=input("Introduce el nombre de un invitado o fin para terminar: ")
print(f'Tu lista de invitados es: {invitados}')

#Ejercicio 5
edades=[]
for i in range(5):
    edad=int(input('Introduce tu edad: '))
    if 0<= edad <=120:
        edades.append(edad)
        print(edades)
    else:
        print('No es una edad válida.')
        print(edades)

#Ejercicio 6
par=[]
impar=[]
for i in range(10):
    numero=int(input('Introduce un número: '))
    if numero %2 ==0:
        par.append(numero)
        print(par)
        print(impar)
    else:
        impar.append(numero)
        print(par)
        print(impar)