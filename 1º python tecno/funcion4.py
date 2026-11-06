num1=float(input("Introduce un número: "))
num2=float(input("Introduce un número: "))
if num2!=0:
    def division(num1,num2):
        return num1/num2
    div=division(num1,num2)
    print(f"El resultado es {div}")
else:
    print("No se puede hacer una división con denominador cero.")