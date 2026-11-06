#Ejercicio 1
temperatura=[]
for i in range(3):
    temp= float(input("Introduce una temperatura: "))
    if -50<=temp<=60:
        temperatura.append(temp)
        def operacion(temperatura):
            return sum(temperatura) /len(temperatura)
        media= sum(temperatura) /len(temperatura)
if -50<=temp<=60:
    print(f'Temperaturas válidas introducidas:{temperatura}')
    print("Primera temperatura válida:", temperatura[0])
    print("Última temperatura válida:", temperatura[-1])
    print(f'La media de las temperaturas válidas es: {media:.2f}')
else:
    print("No se introdujeron temperaturas válidas.")

#Ejercicio 2
alumnos=[]
notas=[]
grupo=[]
for i in range(5):
    alum=input('Introduce tu nombre: ').strip()
    nota=float(input('Introduce tu nota:'))
    if nota>=5:
        notas.append(nota)
        alumnos.append(alum)
    grupo.append(nota)
    def operaciones(grupo):
        return sum(grupo)/len(grupo)
    media1= sum(grupo)/len(grupo)
if nota>=5:
    print(f'Han aprobado: {alumnos}')
    print(f'La media de las notas del grupo es: {media1}')
else:
    print('No han aprobado ninguno.')

#Ejercicio 3
admitidos = []
print("Bienvenido al sistema de control de acceso de la montaña rusa.")
print("Ingrese los datos de los visitantes (escriba 'fin' como nombre para terminar).")
while True:
    nombre = input("Nombre del visitante: ").strip()
    if nombre.lower() == 'fin':
        break
    try:
        edad = int(input("Edad del visitante: "))
    except ValueError:
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

#Ejercicio 4
productos=[]
productos_malos=[]
print('Bienvenido al sistema de comprobación de la caducidad de productos.')
print('Para finalizar con el proceso de comprobación ingrese: "fin".')
while True:
    product=input('Introduce el nombre de un producto: ')
    if product.lower() == 'fin':
        break
    else:
        caducidad=input('¿Está caducado? ').strip().lower()
    if caducidad== 'si':
        productos_malos.append(product)
        print('Retire este producto.')
    elif caducidad == 'no':
        productos.append(product)
    else:
        print('Por favor responda "si" o "no".')
        continue
if productos:
    print('La lista de alimentos que no están caducados es:')
    for i, alimentos in enumerate (productos, 1):
        print(f'{i}.{alimentos}')
    print('La lista de alimentos que tienes que hacer un retiro inmediato de ellos es:')
    for i, alimentos_malos in enumerate (productos_malos, 1): 
        print(f'{i}.{alimentos_malos}')
else:
    print('No hay ningún producto en buen estado, haz un retiro inmediato de ellos:')
    for i, alimentos_malos in enumerate (productos_malos, 1): 
        print(f'{i}.{alimentos_malos}')