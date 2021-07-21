x = 1
while x<=10:
  print("Conteo" + str (x))
  x = x + 1

print("Aqui termina")
print("________________________________________________________________")

años = int(input("introduce tus años"))

while años<0:
  print("Tus años son negativos trata de nuevo")
  años = int(input("introduce tus años"))
print("eso fue todo")
print("años del participante" + str(años))
print("_________________________________________________________________")

años = int(input("introduce tus años"))

while años<0 or años>100:
  print("años incorrectos")
  años = int(input("introduce tus años"))
print("eso fue todo")
print("años del participante" + str(años))
