for i in range(5):
  print("hello") #el range va del 0 al 4 en esta ocacion e imprimira 5 veces "hello"
print("_______________________________________________________________")

for i in range(5):
  print(f"el valo de la variable es {i}") #La funcion "f" nos ayuda a concatenar strings y varible
print("_______________________________________________________________")

for i in range(5, 10):
  print(f"el valo de la variable es {i}")
print("_______________________________________________________________")

for i in range(5, 20, 3):
  print(f"el valo de la variable es {i}") #El ultimo valor es el valo de cuanto en cuanto ira el conteo
print("_______________________________________________________________")

valido = False
email = input("Intriuce el email: ")

for i in range(len(email)):
  if email[i]=="@":
    valido = True  #Range evalua el email escrito y len contabilza los datos

if valido:
  print("Email correcto")
else:
  print("Email incorrecto")
