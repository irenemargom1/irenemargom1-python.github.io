#Ej 1
print('Bienvenido al sistema de cálculo de prismas.')
lg=float(input('Introduce la longitud del prisma en cm: '))
anch=float(input('Introduce la anchura del prisma en cm: '))
alt=float(input('Introduce la altura del prisma en cm: '))
def volumen(lg,anch,alt):
    return lg*anch*alt
vol=lg*anch*alt
print(f'El volumen del prisma es {vol}cm3')




#Ej 2 
print('Bienvenido al sistema de cálculo de velocidades.')
km=float(input('Escribe la distancia en Km: '))
tiempo=float(input('Escribe el tiempo empleado en horas: '))
def velocidad(km,tiempo):
    return km/tiempo
solucion= km/tiempo
print(f'La velocidad media es {solucion}')
if solucion<40:
    print('Muy lenta.')
elif 40<=solucion<80:
    print('Velocidad normal.')
else:
    print('¡Vas muy rápido!')



#Ej 3
print('Bienvenido el sistema de control de acceso del parque de atracciones.')
print("Ingrese los datos de los visitantes (escriba 'fin' como nombre para terminar).")
admitidos = []
while True:
    nombre = input("Nombre del visitante: ").strip()
    if nombre.lower() == 'fin':
        break
    if nombre!=ValueError:
        edad = int(input("Edad del visitante: "))
    else:
        print("Por favor ingrese una edad válida (número entero).")
        continue
    if edad >= 12:
        admitidos.append(nombre)
        print(f"{nombre} puede subir a la montaña rusa.")
    else:
        print(f"{nombre} no puede subir a la montaña rusa (edad mínima: 12 años).")
print(f"Lista de personas admitidas:")
if admitidos:
    for i, persona in enumerate(admitidos, 1):
        print(f"{i}. {persona}")
else:
    print("No hubo personas admitidas.")




#Ej 5
print('Bienvenido al sistema que permite registrar las nbotas de los alumnos.')
print('Introduce los nombres del alumnado (escribe fin como nombre para terminar la lista).')
alumn=[]
alum_a=[]
alum_s=[]
nota=[]
nom_alum=input('Introduce el nombre del alumnado: ').strip()
while nom_alum.lower!='fin':
    nota_alum=float(input('Introduce la nota del alumno: '))
    nom_alum=input('Introduce el nombre del alumnado: ').strip()
    alumn.append(nom_alum)
    nota.append(nota_alum)
    if nota_alum>=5:
        alum_a.append(nom_alum)
    else:
        alum_s.append(nom_alum)
    def media_clase(nota):
        return nota/len(nota)
    media_class= nota/len(nota)
    print('La lista de alumnos es:')
    for i, alumnos in enumerate (alumn,nota, 1): 
            print(f'{i}.{alumnos} {nota}')
    print(f'La media de la clase es {media_class}')
    print('La lista de alumnos aprobados es:')
    for i, alumnos_a in enumerate (alum_a, 1): 
            print(f'{i}.{alumnos_a}')
    print('La lista de alumnos suspensos es:')
    for i, alumnos_s in enumerate (alumn,nota, 1): 
            print(f'{i}.{alumnos_s}')




    