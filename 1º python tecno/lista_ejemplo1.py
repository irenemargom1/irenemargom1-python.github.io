nombres=["Irene","Clara","Mercedes","Daniel","Ana"]
print(nombres)
print(nombres[0]) #Primer elemento
print(nombres[-1]) #Último elemento
nombres[4]="Mar" #Cambiar nombre
print(nombres)
nombres.append("Sofía") #Añadir elemento
print(nombres)
nombres.remove("Daniel") #Quitar elemento
print(nombres)
for nombre in nombres:
    print(nombre)
print(len(nombres)) #Muestra cuantos elementos hay
nombrebuscado=input("Introduce un nombre: ")
if nombrebuscado in nombres:
    print("El nombre está en la lista.")
else:
    print("El nombre no está en la lista.")
