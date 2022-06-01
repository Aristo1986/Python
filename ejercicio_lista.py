# Paso 1: Crea una lista vacía llamada beatles.
# Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
# Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
# Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
# Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.

beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in beatles:
    nombre1=input("Escriba a continuación Stu Sutcliffe para que se agregue a la lista:\n ")
    beatles.append(nombre1)
    print(beatles)
    nombre2=input("Escriba a continuación Pete Best para que se agregue a la lista:\n ")
    beatles.append(nombre2)
    print(beatles)
    break

del beatles[3]
del beatles[3]

beatles.insert(0,"Ringo Starr")

print(beatles)