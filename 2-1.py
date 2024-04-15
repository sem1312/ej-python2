sum = 0

n = int(input("ingrese un numero entero para sumar al total, ingrese un numero negativo para terminar: "))
while n >= 0:
  sum = sum + n
  n = int(input("ingrese otro numero: "))

print(sum)
