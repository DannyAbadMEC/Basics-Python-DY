from io import open #importamos desde la biblioteca open para abrir un archivo externo
archivo_texto = open("archivo.txt", "w") #recibira un nombre el archico y de que manera lo queremos ejecutar
                                         #el archo se crea
Mioracion = "Intento numero 2 para escribir \n dentro de un archivo de texto" #se escribe lo que se quiere mostrar

archivo_texto.write(Mioracion) #para incluir el contenido escrito en una variable

archivo_texto.close() #se cierra el archivo(abierto en memoria desde python)

print("_______________________________________________________________")


from io import open

archivo_texto = open("archivo.txt", "r") #se requiere abrir el archivo en modo lectura

Lectura = archivo_texto.read() #se crea una variable para guardar lo que se lee

archivo_texto.close() #se cierra
print(Lectura)    #Imprimir

print("_________________________________________________________________")

from io import open

archivo_texto = open("archivo.txt", "r")
lista_texto = archivo_texto.readlines() #lee informacion almacenada en un archivo y la almacena en una lista

archivo_texto.close()
print(lista_texto) #como es una lista se puede manipular
print("__________________________________________________________________")

from io import open

archivo_texto = open("archivo.txt", "a") #se agrega la funcion append para agregar algun texto
archivo_texto.write("\n Que ingeniosa manera de agregar algun texto") #se vizualisa en el archivo de texto
