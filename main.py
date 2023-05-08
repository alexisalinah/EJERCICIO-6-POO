import csv
from ListaViajero import listaV 
if __name__=='__main__':
    archivo=open('Viajeros.csv')
    reader=csv.reader(archivo,delimiter=",")
    newl=listaV()
    for fila in reader:
        id=int(fila[0])
        dni=fila[1]
        nom=fila[2]
        ap=fila[3]
        millas=int(fila[4])
        newl.carga(id,dni,nom,ap,millas)
    archivo.close()
    newl.muestravmayor()
    m1=int(input("Ingrese las millasa sumar\n"))
    newl.acummillas(m1)
    m2=int(input("Ingrese la cantidad de millas a restar\n"))
    newl.restamillas(m2)

