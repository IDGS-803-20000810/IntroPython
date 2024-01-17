print("Suma de dos numeros")

num1 = int(input("Inserte valor de n1"))
num2 = int(input("Inserte valor de n2"))

if num1 > num2 :
    print("El {} es mayor que el {}".format(num1,num1))
else:
    print("El {} es mayor que el {}".format(num2,num1))

print("--------------dame una edad---------------")
edad = int(input("ingresa tu edad"))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("tienes 18")
else:
    print("Eres menor de edad")
    
