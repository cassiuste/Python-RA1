# Lista con los cuadrados de los números impares del 0 al 10
impares_cuadrados = [x**2 for x in range(11) if x % 2 != 0]

# Conjunto de vocales únicas en una frase
frase = "Esto es un ejemplo"
vocales = {c.lower() for c in frase if c.lower() in 'aeiou'}

# Diccionario que mapea números pares a su cubo si el cubo > 20
cubos = {x: x**3 for x in range(6) if x % 2 == 0 and x**3 > 20}

print(impares_cuadrados)
print(vocales)
print(cubos)