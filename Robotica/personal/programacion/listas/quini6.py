'''
>>>crear una lista de 5 numero al azar entre el 0 y el 9
que esten ordenados y NO repetirlo.

'''
import random 
lista = []
numero = random.randint(0,9)
while len (lista)<5:
    if numero not in lista:
        lista.append (numero)
    numero = random.randint (0,9)
lista.sort() #metodo para ordenar lista 
print (lista)
