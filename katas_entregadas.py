#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#de cada letra en la cadena. Los espacios no deben ser considerados

def contar_frecuencias(palabra):
    diccionario = {}
    for letra in palabra:
        if letra != " ": #con esto no cuenta los espacios
            if letra in diccionario:
                diccionario[letra] += 1
            else:
                diccionario[letra] = 1
    return diccionario

Posiciones = contar_frecuencias ("Hoy es Domingo")

print(Posiciones)

#CON LIST COMPREHENSION
def contar_letras(texto):
    texto = texto.replace(" ", "")  # Quitamos espacios
    letras = set(texto)  # Letras únicas
    return {letra: texto.count(letra) for letra in letras}


# In[ ]:


 # 2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

Lista = [2, 4, 6, 8]

resultado = map(lambda x: x * 2, Lista) #usamos funcion lambda ya que la usaremos una vez y es la forma mas rapida de usar el MAP y la funcion en sí

print (list(resultado))


# In[ ]:


# 3 Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo

lista_de_palabras = ["naranja", "pera", "uva", "durazno"]
palabra_objetivo = "durazno"

resultado = []

for palabra in lista_de_palabras:
    if palabra_objetivo in palabra: #si la palabra objetivo está en palabra (en cada vuelta que da el bucle, es decir, cada una de las 4 vueltas, colocarla en la lista resultad)
     resultado.append(palabra)                   

print(resultado) #primero hago un codigo funcionar para ver lo que quiero plasmar en la funcion



# In[ ]:


# 3 Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo (SEGUIMIENTO DEL BLOQUE ANTERIOR)

def filtrar_palabras(lista_palabras, palabra_objetivo): 
    lista = []
    for palabra in lista_palabras:
         if palabra_objetivo in palabra:
            lista.append(palabra)
    return lista
#esta funcion realiza la busqueda de una palabra objetivo en una lista, para usarla debo realizar la lista y la palabra objetivo, funcion con dos argumentos
listado = ["pera", "manzana", "durazno"]
objetivo = "pera"

resultado = filtrar_palabras (listado, objetivo)

print (resultado)


# In[76]:


# 4 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map

def operaciones_listas(variable1, variable2):
    operacion = map(lambda x, y: x - y, variable1, variable2) #colocamos que la variable x se reste con la variable y, al poner dos listas se restan por posicion de ambas listas, es decir -pos1 lista 1 - posion 2 lista 2
    return operacion

lista_1 = [8, 3, 10, 7 ]
lista_2 = [5, 3, 7, 2]

resultado = operaciones_listas(lista_1, lista_2)

print(list(resultado))




# In[ ]:


# 5 Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y 
# determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". 
# La función debe devolver una tupla que contenga la media y el estado.

def estado_notas(notas, notas_aprobado=5):
    media = sum(notas) / len(notas) #la funcion realizará la operación de sacar la media, se usa len para que nos devuelva la cantidad de elementos dentro de la lista y se divide entre la sumatoria de la lista
    if media >= notas_aprobado:#cabe aclarar que pudiera poner if>=5 y quitar un parametro de la funcion (dejar solo notas) y serviría también, pero de esta forma puedo cambiar el valor del 2do parametro
        #cuando llame la funcion y hacerla mas flexible por si un dia quiero cambiar la nota del aprobado por ejemplo, que ahora pasen con media de 4, cambio el numero abajo y listo
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)

estado=estado_notas([8,6,7],5)

print("la nota media es de", estado)


# In[75]:


# 6 Escribe una función que calcule el factorial de un número de manera recursiva.

#primero lo escribo de forma normal para entenderlo, me piden el factorial de un numero
n = 5
resultado = 1

for i in range(n, 0, -1):  # Empieza en 5, termina en 1, se mulplica 1x5, luego el resultado por 4 y asi hasta el 1 
    resultado = resultado * i


#Ahora haré la funcion con la idea mas clara
def factorial(n):
    if n == 1 or n == 0:     # Caso base: cuando n es 1 o 0, devolvemos 1 (regla del factorial)
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva (cuando n sea mas de 1 la funcion se llama a si misma, es decir, da los resultados)

#Como tiene el return dos veces, en dos condiciones, es como una especie de bucle, que se seguirá usando hasta llegar al IF 
# que marca claramente que una vez sea 0 o 1 el return dará directamente un 1, esto hace que sea recursiva esta funcion

final=factorial(4) #da 24, es decir 4x1=4x3=12x2=24x1=24 y termina

print (final)


# In[ ]:


# 7 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

#primero voy a hacer unas pruebas con las tuplas para entender lo que quiero
prueba=[("Hola", "Mundo"), ("Python", "Genial")]
prueba[0]="adios" #modifico el primer elemento que es la lista, por eso cambia
print(prueba) #Me piden algo parecido a esto

prueba3=[("Hola", "Mundo"), ("Python", "Genial")]
print(prueba3)

prueba2=[("Hola", "Mundo"), ("Python", "Genial")]
prueba2[0][0]="adios" #modifico el 2do elemento que es la tupla, debe dar error
print(prueba2)



# In[ ]:


# 7 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
lista_tuplas = [("Hola", "Mundo"), ("Python", "Genial")]

lista_strings = []

for tupla in lista_tuplas:
    string = " ".join(tupla)  # Une los elementos de la tupla con espacio
    lista_strings.append(string)

print(lista_strings)
#sin la funcion (para verlo mejor antes de hacerlo)

#ESTO ES LO QUE PIDE EL EJERCICIO
def tuplas_a_strings(lista_tuplas):
    return map(lambda tupla: " ".join(tupla), lista_tuplas)

lista_1 = [("Hola", "Mundo"), ("Python", "Genial")]

resultado=tuplas_a_strings(lista_1)

print(list(resultado))

#en este ejercicio el join se ejecuta en una sola lista y lo que me hace el for (el buble que hice antes para entender lo que debo hacer), 
# que tengo que poner el append, esto lo hace por detras el lambda y me genera el solo la lista nueva,
# por eso se usa una sola lista, en vez de hacer una lista vacia y que me lo aplique a parte, el map opera solo (guardo esta explicación para mi ya que me costó el ejercicio)


# In[ ]:


# 8 Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, 
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
except ValueError:
    print("Error: Debes ingresar valores numéricos.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print("División exitosa. Resultado:", resultado)

#para inputs que tengan valores de texto es mejor usar Try en input ya que como el float no puede convertir letra en decimales 
#lanzará inmediatamente un error antes de llegar a cualquier bloque siguiente, por lo que aqui usaremos el except value error para
#que omita el error y siga el codigo


# In[ ]:


#EJERCICIO 8 NUEVAMENTE, lo agrego de esta forma también para mi ya que se puede de ambas formas, me gusta mas con el bucle ya que así
#el usuario trabaja hasta que sea correcto

while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: Debes ingresar valores numéricos.")
        continue
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        continue
    else:
        print("División exitosa. Resultado:", resultado)
        break  # Salir del bucle si todo fue bien


# In[84]:


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def lista_numeros(lista_mascotas):
    prohibidas=["mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"]
    mascotas_prohibidas = filter(lambda x: x not in prohibidas, lista_mascotas)
    return mascotas_prohibidas

animales=["ave","oso", "pelicano"]

resultado = lista_numeros(animales)

print(list(resultado))


# In[ ]:


# 10 Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
# excepción personalizada y maneja el error adecuadamente.
def estado_notas(numeros):
    if len(numeros) == 0:
        raise ValueError("La lista está vacía, no se puede calcular la media.")
    #colocamos este tipo de error para luego indicarlo en el except y lanzar la indicacion que queremos dar
    media = sum(numeros) / len(numeros)
    return media

lista2 = []  # Puedes probar también con lista2 = [] para ver el error

try:
    resultado = estado_notas(lista2)
except ValueError as a:#lo asignamos con otro nombre para que de la descripcion del tipo de error que pusimos arriba para que se sepa que pasa
    print("Error:", a)#mensaje que damos al usuario
else:
    print("La media es:", resultado)# si no se cumple el if, da el resultado


# In[105]:


# 11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try:
    edad = int(input("Ingresa tu edad: "))
    if edad >= 1 and edad <=110:
        print ("tienes",edad, "años")
    else:
        print ("Coloca un numero entre 1 y 100")
except ValueError:
    print ("No se permite colocar texto")


# In[114]:


#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def lista(longitud_lista):
    return map(lambda x: len(x), longitud_lista)

palabras = ["Hola", "Chao"]
resultado=lista(palabras)

print(list(resultado))


# In[ ]:


#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
# Las letras no pueden estar repetidas .Usa la función map()

def eliminar_repetidas(texto):
    resultado = []
    for letra in texto:
        if letra not in resultado:
            resultado.append(letra)
    return resultado

#Hacemos primero este FOR para que mantenga el orden de la lista

def convertir_letras(texto):
    unicas = eliminar_repetidas(texto)
    return map(lambda x: (x.upper(), x.lower()), unicas)

#Ahora definimos la funcion del MAP, dentro metemos la funcion del FOR de eliminar repetidas, con eso se mantiene tanto el orden como la devolucion de cada letra mayuscula y minuscula

tupla =("Claudio")

resultado = convertir_letras (tupla)

print (list(resultado))


# In[ ]:


#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtrar_lista(lista, letra_inicial):
    return filter(lambda x: x.startswith(letra_inicial), lista) #aqui estamos colocando que el filtro del 2do parametro se aplique al primer parametro (lista)

Lista=["Hola", "Chao"]
Iniciales=("H")

resultado=filtrar_lista(Lista, Iniciales)

print(list(resultado))


# In[125]:


#15. Crea una función lambda que sume 3 a cada número de una lista dada

def sumar_3(numeros):
    return map(lambda x: x+3, numeros)

lista_numeros=[5,6,8]

resultado=sumar_3(lista_numeros)

print(list(resultado))


# In[129]:


#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def filtrar_texto(lista):
    return filter(lambda x: len(x)>5, lista)

lista_letras=["hola", "claudio"]

resultado=filtrar_texto(lista_letras)

print(list(resultado))


# In[ ]:


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

def unir_digitos(lista):
    # Convertir cada número a string
    strings = map(str, lista)
    # Unirlos todos
    unido = "".join(strings)
    # Convertir el resultado a entero
    return int(unido)
#primero quise hacerlo sin el reduce para aclararme, me lo guardo para mi para tenerlo como ejemplo en ocasiones futuras
#AHORA EL EJECICIO
from functools import reduce

def unir_digitos(lista):
    return reduce(lambda x, y: x * 10 + y, lista)

resultado = unir_digitos([5, 2, 3]) #la tupla me lo une ya que multiplica 5*10=50+2=52*10=520+3=523
print(resultado)



# In[137]:


#19. Crea una función lambda que filtre los números impares de una lista dada.

def filtro_impares(lista):
    return filter(lambda x: x % 2 != 0, lista)

numeros=[5,2,4,7]

resultado=filtro_impares(numeros)

print(list(resultado))


# In[2]:


# 20 Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(lista):
    return filter(lambda x: isinstance(x, int), lista)#insinstance es una funcion para que nos traiga solo numeros entero si la lista los posee, nos devuelve true a los numeros enteros

lista=["hola",5,"chao",2]

resultado=filtrar_enteros(lista)

print(list(resultado))


# In[8]:


#21 Crea una función que calcule el cubo de un número dado mediante una función lambda

def cubo(numero):
    return map(lambda x: x**3, numero)

lista_numeros=[2,3,4]

resultado=cubo(lista_numeros)

print(list(resultado))


# In[11]:


#22 Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

def producto_total(numeros):
    return reduce(lambda x,y: x*y, numeros)

resultado=producto_total([5,5,5])

print(resultado)


# In[14]:


# 23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

def concatenar(lista):
    return reduce(lambda x, y: x + y, lista)

resultado=concatenar(["Hola","soy","Claudio"])
print(resultado)


# In[15]:


#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia(lista):
    return reduce(lambda x, y: x - y, lista)

resultado=diferencia([20,5,2])
print(resultado)


# In[19]:


#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar(longitud):
    return len(longitud)

palabra = ("Hola")
resultado=contar(palabra)

print(resultado)


# In[8]:


#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter 
# para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad en numeros: "))
calificacion = int(input("Escribe la calificación en numeros: "))

estudiante = {
    "nombre": nombre,
    "edad": edad,
    "calificacion": calificacion
}

estudiantes = [
    estudiante,
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 21, "calificacion": 88},
    {"nombre": "Sofía", "edad": 19, "calificacion": 92}
]

estudiantes_destacados = filter(lambda x: x["calificacion"] >= 90, estudiantes)


print(list(estudiantes_destacados))


# In[ ]:


nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad en numeros: "))
calificacion = int(input("Escribe la calificación en numeros: "))

estudiante = {
    "nombre": nombre,
    "edad": edad,
    "calificacion": calificacion
}

estudiantes = [
    estudiante,
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 21, "calificacion": 88},
    {"nombre": "Sofía", "edad": 19, "calificacion": 92}
]

estudiantes_destacados = list(filter(lambda x: x["calificacion"] >= 90, estudiantes))

print("Estudiantes con calificación mayor o igual a 90:")
for e in estudiantes_destacados:
    print(e)

#Estas son las dos formas de hacer el ejercicio, yo lo hice de la primera forma, IA me recomendó hacerlo asi ya que de esta forma muestra el resultado de forma mas ordenada
#como objeto - valor de cada uno, haciendo que se vea mejor, la funcion trabaja sobre lista de cada calificacion dejando los mayores a 90.
#Se coloca una lista de diccionarios para que se pueda usar filter, ya que el filtro compara sobre algo para filtrar, si no hay con que comparar daría error


# In[16]:


resto = lambda x, y: x % y
print(resto(9, 2))  


# In[21]:


# 27. Crea una función que calcule el promedio de una lista de números.

def promedio (lista):
    media = sum(lista) / len(lista)
    return media

lista_numeros=[5,6,7]

resultado=promedio(lista_numeros)

print(resultado)


# In[ ]:


#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def duplicados(lista):
    vistos = []
    for elemento in lista: #trabajamos sobre los elementos del PARAMETRO de la funcion
        if elemento in vistos: #Si el elemento esta en vistos (lista donde iran agregandose los elementos dependiendo de nuestras condiciones)
            return elemento  # Primer duplicado encontrado, lo coloca, si no lo encuentra usa el Else y va poniendo los numeros, cuando lo encuentra se ejecuta el IF y se usa el return
        #para parar el bucle y solo devolver el primer numero duplicado, sin el return el bucle seguiría
        else:
            vistos.append(elemento) #coloca el elemento en la lista si no hay duplicados, por eso el else
    return None  # Si no hay duplicados, devuelve none, lo colocamos en el bloque del for ya que es lo que devolverá si no se cumplen condiciones del for, en vez de devolver la lista vacia

Lista = [5,6,7,5,4,2,7]

resultado=duplicados(Lista)
print(resultado)


# In[ ]:


def enmascarar(texto):
    # Convertimos a string por si el valor que recibimos es un número
    # Así podemos trabajar con él como si fuera una lista de caracteres:
    # - usar len() para contar
    # - usar slicing (texto[-4:]) para acceder a partes del texto
    texto = str(texto)

    # Si el texto tiene 4 o menos caracteres, no lo enmascaramos
    if len(texto) <= 4:
        return texto
    else:
        # Calculamos cuántos caracteres debemos ocultar (todos menos los últimos 4)
        cantidad_enmascarada = len(texto) - 4

        # Creamos una cadena con "#" repetida esa cantidad de veces
        parte_oculta = "#" * cantidad_enmascarada

        # Obtenemos los últimos 4 caracteres del texto original
        parte_visible = texto[-4:]

        # Devolvemos la parte oculta + la parte visible
        return parte_oculta + parte_visible


# Ejemplos de uso
print(enmascarar("123456789"))  # Resultado: "#####6789"
print(enmascarar("hola"))       # Resultado: "hola"
print(enmascarar(987654321))    # Resultado: "#####4321"



# In[28]:


def son_anagramas(palabra1, palabra2):
    # Convertimos todo a minúsculas por si hay mayúsculas mezcladas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Si al ordenar las letras las palabras quedan iguales → son anagramas
    if sorted(palabra1) == sorted(palabra2): #el sorted nos ordena las letras alfabeticamente pongamos lo que pongamos, por lo que si son iguales devuelve true, sino false
        return True
    else:
        return False

print(son_anagramas("amor", "roma"))     
print(son_anagramas("perro", "gato")) 


# In[ ]:


#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje 
# indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre(): #lo colocamos sin parametros ya que las variables se piden dentro de la funcion al tener Input
    # Pedimos la lista de nombres al usuario (separados por coma)
    entrada = input("Introduce una lista de nombres separados por comas: ")
    nombres = entrada.split(",")  # Convertimos a lista separando por comas

    # Limpiamos los espacios en blanco
    nombres = [nombre.strip() for nombre in nombres] #strip quita los espacios de todas las variables

    # Pedimos el nombre que vamos a buscar
    nombre_a_buscar = input("Introduce el nombre a buscar: ").strip()

    # Buscamos el nombre
    if nombre_a_buscar in nombres:
        print(f"{nombre_a_buscar} fue encontrado en la lista.")
    else:
        # Si no está, lanzamos una excepción
        raise ValueError(f"{nombre_a_buscar} no fue encontrado en la lista.") #Usando el F-String se ve mas limpio

buscar_nombre()


# In[8]:


def buscar_nombre_en_lista(lista, nombre_a_buscar):
    if nombre_a_buscar in lista:
        print(f"{nombre_a_buscar} fue encontrado.")
    else:
        raise ValueError((nombre_a_buscar)," no fue encontrado.")


lista = ["Ana", "Pedro", "Lucía"]
Resultado = buscar_nombre_en_lista(lista, "Pedro")
print(Resultado)



#Esta es una version sin input que había hecho yo para aclararme de mas o menos como sería


# In[ ]:


#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, 
# de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

empleados = [
    {"nombre": "Ana Gómez", "puesto": "Analista"},
    {"nombre": "Luis Pérez", "puesto": "Contador"},
    {"nombre": "Sofía Ruiz", "puesto": "Gerente"}
]

buscar_nombre = "Ana Gómez"

for elemento in empleados:
    if elemento ["nombre"].lower() == buscar_nombre.lower():
        print (elemento["puesto"])

#Hago primero el ejercicio sin la función para ver como plasmarlo


# In[ ]:


#ESTO ES LO QUE PIDE EL EJERCICIO

def buscar_puesto(nombre_buscado, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"].lower() == nombre_buscado.lower():
            return empleado["puesto"]
    return "El empleado no está en la lista"

empleados = [
    {"nombre": "Ana Gómez", "puesto": "Analista"},
    {"nombre": "Luis Pérez", "puesto": "Contador"},
    {"nombre": "Sofía Ruiz", "puesto": "Gerente"}
]

# Probando con un nombre que sí existe
print(buscar_puesto("ana gómez", empleados))   

# Probando con uno que no existe
print(buscar_puesto("Carlos Reyes", empleados))  


# In[38]:


#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

def suma(lista1, lista2):
    return (map(lambda x, y: x + y, lista1, lista2))

Numeros1=[5,6,7]
Numeros2=[5,6,7]

resultado=suma(Numeros1, Numeros2)
print(list(resultado))


# In[ ]:


#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método
#info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
#mismas.
#Caso de uso:
#1. Crear un árbol.
#2. Hacer crecer el tronco del árbol una unidad.
#3. Añadir una nueva rama al árbol.
#4. Hacer crecer todas las ramas del árbol una unidad.
#5. Añadir dos nuevas ramas al árbol.
#6. Retirar la rama situada en la posición 2.
#7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        # El tronco empieza con longitud 1
        self.tronco = 1
        # La lista de ramas comienza vacía
        self.ramas = []

    def crecer_tronco(self):
        # Aumenta la longitud del tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # Añade una nueva rama con longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumenta en 1 la longitud de cada rama usando list comprehension
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # Verificamos que la posición sea válida
        if posicion >= 0 and posicion < len(self.ramas):
            self.ramas.pop(posicion) #con el pop quitamos la posicion que eligamos luego al llamar el metodo mas abajo (al colocar posición elegimos luego que quitamos, no como los anteriores
            #que todo está definido)
        else:
            print("Posición no válida")

    def info_arbol(self):
        # Muestra información actual del árbol
        print(f"Tronco: {self.tronco}")
        print(f"Número de ramas: {len(self.ramas)}")
        print(f"Longitudes de ramas: {self.ramas}")


Arbolito=Arbol() #Creamos el arbol con la clase que nos va a traer un tronco y una lista de ramas vacía donde agregaremos los demas metodos
Arbolito.crecer_tronco()
Arbolito.crecer_tronco()#hacemos crecer los troncos
Arbolito.nueva_rama()
Arbolito.nueva_rama()
Arbolito.nueva_rama() #creamos las ramas
Arbolito.crecer_ramas() #hacemos crecer las ramas
Arbolito.info_arbol() #traemos la info antes de eliminar una de las ramas
Arbolito.quitar_rama(2) #Aqui colocamos la posicion que queremos quitar ya que en el metodo no colocamos una posición fija, sino que al agregar el parametro posición nosotros colocamos el valor
Arbolito.info_arbol() #volvemos a traer la info de las ramas


# In[61]:


# Kata 35 – Clase UsuarioBanco
# Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como:
# - retirar dinero
# - transferir dinero desde otro usuario
# - agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True o False.
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo a "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo de "Alicia".

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente): #como nos pide usuarios diferentes, esta vez colocamos los parametros para elegirlos en los self y poder cambiarlos cuando los llamemos
        self.usuario = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente


    def retirar_dinero(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo-=cantidad
            print(f"Ha retirado {cantidad}, su saldo actual es de {self.saldo}")
        else:
            print("Saldo insuficiente para la operación")

    def transferir_dinero(self, otro_usuario, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad #Aqui estamos diciendo que si el saldo es mayor o igual a la cantidad elegida entonces se resta el saldo del usuario DE LA CLASE
            otro_usuario.saldo += cantidad #El usuario que colocamos como parametro se le suma la cantidad de la transferencia
            print(f"{self.usuario} ha transferido {cantidad} a {otro_usuario.usuario}") 
        else:
            print(f"{self.usuario} no tiene suficiente saldo para transferir")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"{self.usuario} ha recibido {cantidad}, su saldo es de {self.saldo}")


Alicia = UsuarioBanco("Alicia", 100, True)
Bob = UsuarioBanco("Bob", 50, True)

Bob.agregar_dinero(20)
Bob.transferir_dinero(Alicia, 80)
Alicia.retirar_dinero(50)



# In[ ]:


# Kata 36 – Función procesar_texto
# Crea una función llamada `procesar_texto` que procese un texto según la opción especificada:
# Las opciones disponibles son:
# - contar_palabras → cuenta cuántas veces aparece cada palabra
# - reemplazar_palabras → reemplaza una palabra por otra
# - eliminar_palabra → elimina una palabra del texto
# Código a seguir:
# 1. Crear una función `contar_palabras` que reciba un texto y devuelva un diccionario con la frecuencia de cada palabra.
# 2. Crear una función `reemplazar_palabras` que reciba un texto, una palabra_original y una palabra_nueva y devuelva el texto con la palabra reemplazada.
# 3. Crear una función `eliminar_palabra` que reciba un texto y una palabra, y devuelva el texto sin esa palabra.
# 4. Crear una función `procesar_texto` que reciba:
#    - el texto
#    - una opción entre "contar", "reemplazar", "eliminar"
#    - argumentos adicionales según la opción
# Caso de uso esperado:
# - procesar_texto("hola mundo mundo", "contar") → {'hola': 1, 'mundo': 2}
# - procesar_texto("hola mundo", "reemplazar", "mundo", "amigo") → "hola amigo"
# - procesar_texto("hola mundo mundo", "eliminar", "mundo") → "hola"

#Funcion 1
def contar_palabras(texto):
    diccionario = {}
    palabras = texto.split()  # divide el texto en palabras

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1 #lo hacemos de esta forma para agregar el valor a cada celda, en diccionarios no se usa el Append (lo recuerdo para mi)
        else:
            diccionario[palabra] = 1
    return diccionario

resultado= contar_palabras("hola mundo mundo")
print(resultado)

#Funcion 2
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    nuevo_texto = texto.replace(palabra_original, palabra_nueva)#replace para reemplazar la palabra que queramos del texto
    return nuevo_texto

resultado = reemplazar_palabras("hola mundo", "mundo", "amigo")
print(resultado)  

#Funcion 3

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()  # Separamos el texto en una lista de palabras

    # Creamos una nueva lista solo con las palabras que NO son la que queremos eliminar
    resultado = [palabra for palabra in palabras if palabra != palabra_a_eliminar] # Guarda palabra (como hacer la lista vacia en un for normal y colocar el .append, el append solo se usa en listas) 
    #por cada palabra en palabras si palabra es diferente de la que quiero eliminar

    return " ".join(resultado)  # Volvemos a unir la lista en un solo string separado por espacios

resultado = eliminar_palabra ("Hola mundo", "mundo")
print (resultado)

# Funcion 4- la final que elige que funcion de las otras 3 se ejecutará
def procesar_texto(texto, opcion, *args): #usamos args ya que al tener 3 funciones estas pueden tener varios parametros, por lo que la funcion principal indicamos eso con el args y luego modificamos dentro
    # Si la opción es "contar", solo necesitamos el texto
    if opcion == "contar":
        return contar_palabras(texto)

    # Si la opción es "reemplazar", esperamos 2 palabras adicionales
    elif opcion == "reemplazar":
        if len(args) == 2:
            palabra_original = args[0]#Les damos la posición a cada variable dentro de la tupla para que luego pueda cambiarse
            palabra_nueva = args[1]
            return reemplazar_palabras(texto, palabra_original, palabra_nueva)
        else:
            return "Faltan parámetros para reemplazar"

    # Si la opción es "eliminar", esperamos 1 palabra adicional
    elif opcion == "eliminar":
        if len(args) == 1:
            palabra_a_eliminar = args[0]
            return eliminar_palabra(texto, palabra_a_eliminar)
        else:
            return "Falta la palabra a eliminar"

    else:
        return "Opción no válida"

print(procesar_texto("hola mundo mundo", "contar"))


print(procesar_texto("hola mundo", "reemplazar", "mundo", "amigo"))


print(procesar_texto("hola mundo mundo", "eliminar", "mundo"))



# In[16]:


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

try:
    hora=int(input("Ingresa la hora en número sin los dos puntos (por ejemplo: 15 equivale a las 15:00 de la tarde)"))
    if hora >=6 and hora<= 12:
        print (f"Son las {hora} de la mañana")
    elif hora >=13 and hora<= 18:
        print (f"Son las {hora} de la tarde")
    elif hora >=19 and hora<= 24:
        print (f"Son las {hora} de la noche")
    elif hora >=1 and hora<= 5:
        print (f"Son las {hora} de la madrugada")
    else:
        print ("Introduce un valor válido")
except ValueError:
    print ("No se permite colocar texto")

#Se hace un programa donde indicamos colocar la hora en numer


# In[17]:


#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
#- 0 - 69 insuficiente
#- 70 - 79 bien
#- 80 - 89 muy bien
#- 90 - 100 excelente

try:
    nota=int(input("Ingresa la nota en número"))
    if nota >=0 and nota<= 69:
        print (f"Insuficiente")
    elif nota >=70 and nota<= 79:
        print (f"Bien")
    elif nota >=80 and nota<= 89:
        print (f"Muy bien")
    elif nota >=90 and nota<= 100:
        print (f"Excelente")
    else:
        print ("Introduce un valor válido")
except ValueError:
    print ("No se permite colocar texto")


# In[ ]:


#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) 
# y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calculo(figura, *args):#utilizo args ya que no se cuantos parametros pueden llegarse a usar en los condicionales
    if figura == "rectangulo":
        if len(args) == 2:
            largo = args[0]
            ancho = args[1]
            return largo * ancho #utilizo los return para que devuelvan las formulas dependiendo de la figura que elijan
        else:
            return "El rectángulo necesita 2 datos (largo y ancho)"

    elif figura == "triangulo":
        if len(args) == 2:
            base = args[0]
            altura = args[1]
            return (base * altura) / 2
        else:
            return "El triángulo necesita 2 datos (base y altura)"

    elif figura == "circulo":
        if len(args) == 1:
            radio = args[0]
            pi = 3.14
            return pi * (radio ** 2)
        else:
            return "El círculo necesita solo 1 dato (radio)" #utilizo los Else para indicar el dato que necesita cada formula por si lo colocan mal

    else:
        return "Figura no válida"

print(calculo("rectangulo", 5, 3))
print(calculo("triangulo", 4, 6))   
print(calculo("circulo", 2))   
print(calculo("cuadrado", 2))    


# In[ ]:


# Kata 41 – Descuento en tienda online
#
# En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales
# para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.
#
# El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta "sí" o "no").
# 3. Si el usuario responde que "sí", solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (mayor a cero).
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o no.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones.

try:
    # 1. Solicitamos el precio original
    precio = float(input("Introduce el precio original del artículo (€): "))

    # 2. Preguntamos si tiene cupón
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí / no): ").lower()

    # 3. Si tiene cupón, pedimos el valor del cupón
    if tiene_cupon == "sí":
        descuento = float(input("Introduce el valor del cupón (€): "))

        # 4. Validamos que el descuento sea positivo
        if descuento > 0:
            precio_final = precio - descuento
            print(f"Se ha aplicado un descuento de {descuento}€. Precio final: {precio_final}€")
        else:
            print("El valor del cupón no es válido. No se aplicará ningún descuento.")
            print(f"Precio final: {precio}€")

    # 5. Si no tiene cupón
    elif tiene_cupon == "no":
        print(f"No se ha aplicado ningún descuento. Precio final: {precio}€")

    # 6. Entrada no válida
    else:
        print("Respuesta no válida. Por favor escribe 'sí' o 'no'.")

except ValueError:
    print("Por favor, introduce solo números donde se te pide.")

