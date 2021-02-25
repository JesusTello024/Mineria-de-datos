#!/usr/bin/env python
# coding: utf-8

# # EJERCICIOS DE PYTHON

# #### Ejercicio 1. Realiza una variable con tu matricula y realiza una secuencia de imprimir con tu nombre y tu matricula concatenados.

# In[26]:


matricula=1798181
name="Jesus Omar Tello Esparza "
print(name+str(matricula))


# #### Ejercicio 2. Pidiendo el input del usuario pide dos números y crea una pequeña calculadora con los operadores básicos de suma, resta, multiplicación, división, y exponente.

# In[28]:


print("\nCALCULADORA BÁSICA")
Valor1= int(input("Inserta un número: "))
Valor2=int(input("Inserta un número: "))
print("Suma: ", Valor1+Valor2)
print("Resta: ", Valor1-Valor2)
print ("Multiplicación: ", Valor1*Valor2)
print("División: ", Valor1/Valor2)
print("Exponente: ", Valor1**Valor2)


# #### Ejercicio 3. Con loop while o for, realiza una lista de 10 numeros multiplos de 3, y después realiza una función de loop que sume todos los números dentro del arreglo.

# In[11]:


multiplo3=[]
validar= False

for i in range (1, 31):

    validar = i % 3 == 0
    
    if (validar):
        multiplo3.append(i)

print (multiplo3)


# #### Ahora, se procederá a crear una función de loop que sume los números

# In[12]:


suma=0
for i in range(len(multiplo3)):
    suma=suma+multiplo3[i]
print("La suma de los elementos es",suma)


# #### Ejercicio 4. Con una función de if else, revisar si un número es par o es impar. Con una función de if else, revisar si un número es primo o no.

# In[35]:


numero= int(input(" Inserte el número para verificar si es primo o no: "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador = contador + 1
    print("divisor:", n)
 
if contador > 0 :
  print("El número no es primo" )
else:
  print("El número es primo")

#https://unipython.com/ejemplo-numeros-primos/


# ####  Ejercicio 5. Utilizando diferentes clases en python, crea una calculadora con los operadores básicos de suma, resta, multiplicación, división, y exponente.

# In[41]:


print("Calculadora de Python")
print(" Suma \n Resta \n Multiplicación \n Divisón \n Exponente ")
op= input("¿Qué operación deseas realizar? : ")
x = float(input("Inserta un numero: "))
y = float(input("Inserte un numero: "))
def Suma(x,y):
    return(x+y)
def Resta(x,y):
    return(x-y)
def Multiplicacion(x,y):
    return(x*y)
def Division(x,y):
    return(x/y)
def Exponente(x,y):
    return(x**y)
r=0
if op=="Suma":
    r=Suma(x,y)
elif op=="Resta":
    r=Resta(x,y)
elif op=="Multiplicación":
    r=Multiplicacion(x,y)
elif op=="División":
    if y!=0:
        r=Division(x,y)
elif op=="Exponencial":
    r=Exponente(x,y)
else: 
    print("Ingrese una operación marcada anteriormente")
    

print("\n El resultado es: ", r)


# ####  Ejercicio 6. Tuplas

# #### Ejercicio 7. Listas

# #### Crear una lista con 40 elementos aleatorios enteros.
# 

# In[44]:


import random

RandomList = [random.randint(0,200) for _ in range(n)]
n=40
print(RandomList) 
#https://es.stackoverflow.com/questions/124063/crear-una-lista-de-numeros-aleatorios-en-python


# #### Con una funcion (def) crear dos listas nuevas a partir de la lista creada por números aleatorios, en la cual en una estén los elementos pares, y en la otra los elementos impares

# In[ ]:





# #### Ordenar los elementos de la lista par de mayor a menor, y los de la lista impar de menor a mayor.
# 

# In[ ]:





# #### Ejercicio 8. Diccionarios

# #### Crear un diccionario de 6 personas que conozcas con su primer nombre y su edad.

# In[70]:


dicc={'Jesus': 21, 'Felipe': 20, 'Evelin': 22, 'Angel': 19, 'Amauri': 18, 'Karla': 23}
dicc


# #### Crear una lista con los valores de la edad y reacomodar la lista de menor a mayor valor.
# 

# In[72]:


OrdenEdad=sorted(dicc.values())
print("Las edades de menor a mayor es:",OrdenEdad)


# #### Usando el diccionario y un loop, imprimir solo los nombres.

# In[74]:


print("\nNombres:")
for n in dicc:
    print (n)


# #### Añadir dos personas nuevas a tu diccionario, incluyendo edad.

# In[75]:


dicc['Rodrigo'] = '19'
dicc['Adrian'] = '26'
print("\nNuevo Diccionario:\n",dicc)


# #### Ejercicio 9. Sets

# #### Crea un set con 100 números aleatorios enteros del 1 al 25.
# 

# In[84]:


import random
con=0
set1=set()
while con < 100:
    set1.add((random.randint(0,25)))
    con=con+1
print("El set aleatorios es \n",set1)


# #### Comprueba la longitud de tu set.
# 

# In[86]:


longset = len(set1)
print("\nLa longitud del set es:\n",longset)


# #### Crea una lista de 5 números aleatorios del 1 al 10 y comprueba si cada valor aparece en el set inicial.
# 

# In[92]:


import random
lista=list(random.sample(range(1,11), 5))
lista

for i in range(len(lista)):
    
    if lista[i] in set1:
        a=lista[i]
        print(a, "si aparece en el set inicial")
    else:
        a=lista[i]
        print(a, "no aparece en el set inicial")

