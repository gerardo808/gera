

a=float(input("Ingrese calificacion matematicas"))
b=float(input("Ingrese calificacion quimica"))
c=float(input("Ingrese calificacion programacion"))
d=float(input("Ingrese calificacion base de datos"))
e=float(input("Ingrese calificacion ingles"))
print("Su calificacion es", (a+b+c+d+e)/5)
f=((a+b+c+d+e)/5)

if(f<7):
    print("Reprobado")
if(f>=7.0 and f<=8):
    print("Suficiente")
if(f>=8.1 and f<=9):
    print("notable")
if(f>=9.1 and f<=10):
    print("Exelente")
if(f>10):
    print("Fuera de rango")

    


