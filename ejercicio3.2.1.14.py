# Cada capa inferior contiene un bloque más que la capa superior.
# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la 
# pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques
# y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.



bloques = int(input("Ingresa el número de bloques: "))

altura=0

while(bloques>altura):
    altura+=1
    bloques-=altura

print("La altura de la pirámide:", altura)


