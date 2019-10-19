Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista=[9,3.7,1,"ejemplo","cadena",9.9]
>>> print(lista[4]*lista[0])
cadenacadenacadenacadenacadenacadenacadenacadenacadena
>>> print(lista[0]+lista[1]+lista[2]+lista[5])
23.6
>>> print(lista[5]*lista[2])
9.9
>>> print(lista[0]/lista[5])
0.9090909090909091
>>> input(lista[4]("ingrese el nuevo valor de 4"))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    input(lista[4]("ingrese el nuevo valor de 4"))
TypeError: 'str' object is not callable
>>> 4=(input(lista[4]("ingrese el nuevo valor de 4"))
   print([4])
   
SyntaxError: invalid syntax
>>> 
>>> print(lista[4])
cadena
>>> lista[4]=(input("Ingrese el nuevo valor "))
Ingrese el nuevo valor hola
>>> print([4])
[4]
>>> print(lista[4])
hola
>>> print(lista[4])
hola
>>> 
