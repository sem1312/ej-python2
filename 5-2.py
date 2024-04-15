frutas = ["banana", "manzana", "pera", "naranja"]

fruta = input("Que fruta queres buscar? ")
n = 0

while(n < len(frutas)):
  if(fruta == frutas[n]):
    print("La fruta esta en la lista")
    break
  elif(n != len(frutas)-1):
    n += 1
  else:
    print("La fruta no esta en la lista")
    break
