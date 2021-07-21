import math
print("programa para calculo de raiz")

p = int(input("\ningrese un numero "))

intentos = 0

while p<0:
  print("No se puede, es negativo")
  if intentos == 2:
    print("Muchos intentos")
    break;
  p = int(input("ingrese un numero"))
  if p<0:
    intentos = intentos + 1
if intentos<2:
  solucion = math.sqrt(p)
  print("la raiz cuadrada de " + str(p) + " es " + str(solucion))
