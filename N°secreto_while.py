secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |    
+==================================+
""")

numero=int(input("¿Cuál es el número secreto?"))

while (numero!=secret_number):
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero=int(input("¿Cuál es el número secreto?"))

print("Elegiste el número: ",numero," y es CORRECTO")
print("¡Bien hecho, muggle! Eres libre ahora")