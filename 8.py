nombres = []

while True:
    nombre = input("Ingresa un nombre (o 'fin' para terminar): ")

    if nombre == 'fin':
        break

    nombres.append(nombre)

nombres_ordenados = sorted(nombres)
print("Nombres en orden alfabético:")
for nombre in nombres_ordenados:
    print(nombre)

cantidad_a_e = sum(1 for nombre in nombres if nombre[0].lower() in ['a', 'e'])
print(f"Nombres que empiezan con 'A' o 'E': {cantidad_a_e}")

nombre_especifico = input("Ingresa un nombre para verificar si está en la lista: ")
if nombre_especifico in nombres:
    print(f"{nombre_especifico} está en la lista.")
else:
    print(f"{nombre_especifico} no está en la lista.")
