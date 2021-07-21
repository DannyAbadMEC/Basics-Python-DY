Lista = ["Lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
print(Lista) # Esta es una lista normal

Lista = ["Lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
print(Lista[2]) #Aqui estamos eligiendo algo de la lista

Lista = ["Lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
print(Lista[-2]) #Con simbolo negativo se accede a la lista desde el ultimo elemento

Lista = ["Lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
print(Lista[0 : 3]) #Aqui se indica de donde a donde se quiere imprimir

Lista = ["Lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo", 23, 43, 23, [1,2,3],True]
print(Lista) #Dentro de una lista se puede almacenar todo tipo de variables

Lista = ["Lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
print(len(Lista)) #La funcion len sirve para contar los elementos dentro de una lista

Lista = ["a", "b", "c", "d", "e", "f", "g"]
Lista.append("z")
print(Lista) #Esta funcion agrega un valor al fianal de nuestra lista

Lista = ["a", "b", "c", "d", "e", "f", "g"]
Lista.insert(3, "h")
print(Lista) #Agrega un elemento a la lista indicando la posicion en este caso la h

Lista = ["a", "b", "c", "d", "e", "f", "g"]
Lista.extend(["h", "i", "j"]) #Añade los valores puestos en extend
print(Lista)

Lista1 = ["a", "b", "c"]
Lista2 = ["d", "e", "f"]

Lista3 = Lista1 + Lista2
print(Lista3)  # suma los valores y junta la lista

Lista = ["a", "b", "c", "d", 344]
print("d" in Lista) # para preguntar si un valor esta en la  lista

Lista1 = ["a", "b", "c", 1 , 2 , 3]
print(Lista1.index(1)) #Para saber que posicion ocupa un dato determinado en la lista
