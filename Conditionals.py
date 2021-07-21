numero = int(input("Write a number: "))

if numero>0:
  print("The number is positive")
elif numero == 0:
  print("the number is cero")
else:
  print("the number is negative")

print("thnak you for you participatio")
print("___________________________________________________________")
#concionales anidados y combinados

g = int(input("\nwrite you age: "))

if g>0:
  print("edad correcta")
  if g>=18:
    print("mayor de edad")
  else:
    print("menor de edad")
else:
  print("edad incorrecta")
print("____________________________________________________________")

age = int(input("\nDigite su edad: "))

if age > 0 and age <100:
  print("edad correcta")
  if age >= 18:
    print("es mayor de edad")
else:
  print("edad icorrecta")
