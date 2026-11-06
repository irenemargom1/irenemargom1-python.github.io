#Ejercicio 1
frutas=["Melocotón","Pera","Sandía","Naranja","Melón"]
for nombre in frutas:
    print(nombre)

#Ejercicio 2
colores=["Negro","Rojo","Morado","Gris","Verde"]
print(colores[0])
print(colores[-1])


#Ejercicio 3 y 4
alumnos=[]
for i in range(3):
    nom=input("Introduce un alumno: ")
    alumnos.append(nom)
print(alumnos)

#Ejercicio 5
nom=input("Introduce un alumno para eliminarlo de la lista: ")
alumnos.remove(nom)
print(alumnos)

#Ejercicio 6
nombres=['Ana','Clara','Darío','Irene','Mercedes']
contador=0
for nombre in nombres:
    if len (nombre)>=5:
        contador+=1
print(f'Hay {contador} nombres que tienen 5 letras o más.')

#Ejercicio 7
numeros=[1,2,3]
def suma(numeros):
    return sum(numeros)
solucion= sum(numeros)
print (solucion)