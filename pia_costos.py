from tabulate import tabulate
from io import open
import sys
import time
import os
#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime
#eliminar fecha[-1]
#Día actual
today = date.today()
fecha1=[]
fecha2=[]
fecha3=[]
asunto=[]
entradalist=[]
entradalist.append(0)
salidalist=[]
salidalist.append(0)
existencialist=[]
unitariolist=[]
promediolist=[]
promediolist.append(0)
debelist=[]
debelist.append(0)
haberlist=[]
haberlist.append(0)
saldolist=[]
saldofinal=[]

print("Instrucciones, lea bien cada requerimento del programa, posteriormente introduzca los datos solictados y de ENTER \n \n ADVERTENCIA: COMO ES UNA VERSION DE PRUEBA, EL NO INTRODUCIR EL DATO CORRECTO \n PUEDE LLEVAR A UNA CAIDA DEL SISTEMA EN SU TOTALIDAD \n EN CASO DE OCURRIDO LO ANTERIOR, FAVOR DE REINICIAR EL PROGRAMA, GRACIAS")
print("Cargando...")

#time.sleep(30)
os.system("cls") 
tarjeta="--------------------------------------------TARJETA DE ALMACEN----------------------------------------------\n"
nombrearch=input("Nombre que desea darle al archivo por crear .txt: ")
direccion='C:\Programacion\ '+nombrearch+'.txt'
direccion.split()
archivo_texto=open(direccion,"w")
archivo_texto.write(tarjeta)
def salir():
    sys.exit()
def menu():
   
    os.system("cls")
    desicion=int(input("Elija una opcion del menu, teclee el numero de la opcion y posteriormente de ENTER: \n 1 -registro de inventarios \n 2 -balance general \n 3 -estado de resultados \n 4 -asientos de diario \n 5 -balanza de comprobacion \n 6 salir \n Opcion: "))
    if desicion==1:
        try:
            tarjetaalm()
        except ValueError:
            os.system("cls")
            print("LOS DATOS INGRESADOS NO SON VALIDOS, PARA EVITAR QUE LA TARJETA TENGA ERRORES SE CERRARA EL PROGRAMA, \n FAVOR DE INGRESAR DE NUEVO.")
            time.sleep(10)
            sys.exit()
    if desicion==2:
        os.system("cls")
        print("En mantenimiento...\n por favor elija otra opcion ")               
        time.sleep(4)
 
        menu()
    if desicion==3:
        os.system("cls")
        print("En mantenimiento...\n por favor elija otra opcion ")
        time.sleep(4)

        menu()
    if desicion==4:
        os.system("cls")
        print("En mantenimiento...\n por favor elija otra opcion ")
        time.sleep(4)
        menu()
    if desicion==5:
        os.system("cls")
        print("En mantenimiento...\n por favor elija otra opcion ")
        time.sleep(4)
        menu()
    if desicion==6:
        os.system("cls")
        print("Saliendo del programa...")
        time.sleep(5)
        salir()
    if desicion != (1,2,3,4,5,6):
        os.system("cls")
        print("Opcion incorrecta, redirigiendose al menu...")
        time.sleep(10)
        os.system("cls")
        menu()
def tarjetaalm():
    
    os.system("cls")
    print("---------------------TARJETA DE ALMACEN-----------------------")
    folio=input("Ingrese el folio:  ")
    articulo=input("Nombre del articulo: ")
    articulo2="Articulo : "+articulo+"  "
    folio2="Folio: "+folio+"     "
    archivo_texto.write(folio2)
    archivo_texto.write(articulo2)
    print("Fecha del dia de elaboracion de la tarjeta")
    print(today)
    archivo_texto.write("           Fecha  "+str(today)+"\n")
    print("Cargando...")
    time.sleep(4)
    os.system("cls")
    print("Saldos iniciales")
    print("Fecha del dia de la operacion")
    print(today)
    print("A continuacion se piden los saldos inciales: ")
    saldolist.append(float(input("Saldo Inicial de Mercancias: ")))
    unitariolist.append(float(input("Precio Unitario de la Mercancia Inicial: ")))
    existencialist.append(float(saldolist[0]))
    debelist.append(float(saldolist[0])*float(unitariolist[0]))
    saldofinal.append(float(debelist[-1]))

    asunto.append("Inicial")
    promediolist.append(float(saldofinal[-1])/float(existencialist[-1]))

         

    num_registros=int(input("Numero de registros por capturar:  "))


    horizontal=[today,asunto[-1],entradalist[-1],salidalist[-1],existencialist[-1],unitariolist[-1],promediolist[-1],debelist[-1],haberlist[-1],saldofinal[-1]]
    hola=tabulate(horizontal,headers=["Fecha","Asunto","Entrada","Salida","Existencia","Precio Unitario","Promedio","Debe","Haber","Saldo "])
    os.system("cls")
    print("Registrado con exito")
    print("Saldos iniciales")
    print(hola)
    archivo_texto.write(hola)
    if num_registros==0:
        print(tabulate(horizontal,headers=["Fecha","Asunto","Entrada","Salida","Existencia","Precio Unitario","Promedio","Debe","Haber","Saldo "]))
    print("Cargando...")
    time.sleep(10)
    acum=0
    while acum<num_registros:
    
        acum=acum+1
        os.system("cls")
        desicion=int(input("Es entrada o salida de mercancia(1 entrada, 2 salida):  "))
        if desicion==1:
            print("Movimiento No. ", acum)
            print("Fecha del dia de la operacion")
            
            print(today)
           
            asunto.append("Entrada")
            entradalist.append(float(input("Cantidad de mercancia entrante: ")))
            unitariolist.append(float(input("Precio unitario de la mercancia: ")))
            debelist.append(float(entradalist[-1])*float(unitariolist[-1]))
            existencialist.append(entradalist[-1]+existencialist[-1])
            saldofinal.append(float(saldofinal[-1])+float(debelist[-1]))
            promediolist.append(float(saldofinal[-1])/float(existencialist[-1]))
            horizontal=[today,asunto[-1],entradalist[-1],salidalist[0],existencialist[-1],unitariolist[-1],promediolist[-1],debelist[-1],haberlist[0],saldofinal[-1]]
            hola=tabulate(horizontal,headers=["     ","      ","       ","      ","          ","               ","        ","    ","     ","      "])
            archivo_texto.write(hola)
            print("Registrado con exito")
            print("Cargando...")
            time.sleep(4)
        

        if desicion==2:
            print("Movimiento No. ", acum)
            print("Fecha del dia de la operacion")
            print(today)
            asunto.append("Salida")
            salidalist.append(float(input("Cantidad de mercancia saliente: ")))
            unitariolist.append(float(promediolist[-1]))
            haberlist.append(float(salidalist[-1])*float(unitariolist[-1]))
            existencialist.append(float(existencialist[-1])-float(salidalist[-1]))
            saldofinal.append(float(saldofinal[-1])-float(haberlist[-1]))
            promediolist.append(float(saldofinal[-1])/float(existencialist[-1]))
            horizontal=[today,asunto[-1],entradalist[0],salidalist[-1],existencialist[-1],unitariolist[-1],promediolist[-1],debelist[0],haberlist[-1],saldofinal[-1]           ]
            hola=tabulate(horizontal,headers=["     ","      ","       ","      ","          ","               ","        ","    ","     ","      "])
            archivo_texto.write(hola)
            print("Registrado con exito")
            print("Cargando...")

            time.sleep(4)
    os.system("cls")
    print("La tarjeta de almacen ha sido guardada en la carpeta Programacion creada en su disco local C: en un archivo llamado " +nombrearch+".txt"+"\n el programa se cerrara automaticamente")
    time.sleep(10)
    
    archivo_texto.close()
    sys.exit()


menu()
