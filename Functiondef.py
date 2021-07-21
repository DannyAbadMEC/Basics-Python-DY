def Tabla_de_multiplicar(n):

  for i in range(1,11):
    print(n,'*' , i , '=',i*n)

Tabla_de_multiplicar(5)
print("______________________________________________________________")

def cadena():
  return 'curso de python'
print(cadena()) # la variable return, retorna y llama a la cadena junto con lo que quieres retornar
print("______________________________________________________________")

u = 5
def funcion():
  print(u)
funcion()
print("_______________________________________________________________")

def dato():
  h = 2
  print(h)  #La funcion trabaja con diferentes valores, recomendable de no poner el mismo dato como valor a la variable
dato()

h = 4
dato()
print(h)
print("________________________________________________________________")

def suma (a,b):
  return a+b
respuesta =suma(4,5) #Fue aplicado una suma para mejor entendimiento
print(respuesta)
print("________________________________________________________________")

ejemplo = [3,4,5, 4, 4, 5, 5, 12,23,32]  #separar numeros pares e impares de una lista
def separar_lista(lista):
  lista.sort()
  pares = []
  impares = []
  for i in lista:
    if i %  2 == 0:
      pares.append(i)
    else:
      impares.append(i)
  return pares ,impares
pares, impares = separar_lista (ejemplo)

print("Numeros pares: ", pares )
print("Numeros impares: ", impares )
