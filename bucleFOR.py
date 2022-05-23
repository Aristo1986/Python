for i in range(100):
     #do_something()
     pass

# Cualquier variable después de la palabra reservada "for" es la variable de control del bucle; cuenta los giros del
# bucle y lo hace automáticamente.
# La palabra reservada "in" introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan
# a la variable de control.
# La función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de
# la variable de control

for i in range(10):
    print("El valor de i es actualmente", i)

#======================================================================================================================

#La invocación de la función range() puede estar equipada con dos argumentos, no solo uno:
for i in range(2, 8):
    print("El valor de i es actualmente", i)

# En este caso, el primer argumento determina el valor inicial (primero) de la variable de control.

# El último argumento muestra el primer valor que no se asignará a la variable de control.

# Nota: la función range() solo acepta enteros como argumentos y genera secuencias de enteros.

#======================================================================================================================

# La función range() también puede aceptar tres argumentos

# El tercer argumento es un incremento: es un valor agregado para controlar la variable en cada
# giro del bucle

for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)


