lista = ["1","2","3"]

for i in lista:
  print(i)

print("_______________________________________________________________")

email = False
for i in "danylo.delangel@gmgmail.com":
  if(i=="@"):
    email = True
if email == True:
  print("Email es correcto")
else:
  print("El emial no es coerrecto")

print("_______________________________________________________________")

email = False
miEmail = input("Introduce tu email")
for i in miEmail:
  if (i == "@"):
    email = True
if email:
  print("email es correcto")

else:
  print("el email no es correcto")

print("_______________________________________________________________")

contador = 0
miEmail = input("Introduce tu email")
for i in miEmail:
  if (i == "@" or i=="."):
    contador = contador + 1
if contador == 2:
  print("email es correcto")

else:
  print("el email no es correcto")  # para verificar si en el correo alla @ y .

print("_______________________________________________________________")
