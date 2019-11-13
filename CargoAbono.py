from tabulate import tabulate
import sys
import os
import time
#se necesita instalar tabulate desde la cmd
#en esta seccion importamos los modulos que seran necesarios para este script, el modulo sys sirve para la funcion salir, el modulo os para la funcionn de limpiar pantalla
#el modulo tabulate sirve para poder tabular datos de un diccionario y el modulo time para que tarde un poco en saltar de renglon
#se declaran listas, diccionarios y variables globales en los siguientes renglones
saldoBan=0
saldoCaj=0
saldoAlm=0
saldoCl=0
saldoDeu=0
saldoPro=0
saldoAcre=0
saldoMaq=0
saldoMob=0
saldoEq=0
saldoVen=0
saldoCos=0
y=0
index=0
cuentasList=['01 Caja','02 Bancos','03 Almacen','04 Clientes','05 Deudores Diversos','06 Maquinaria y Equipo','07 Mobiliario y Equipo','08 Equipo de transporte','09 Acreedores Diversos','10 Proveedores',"11 Costo de Venta"," 12 Venta"]
saldosList=[saldoCaj,saldoBan,saldoAlm,saldoCl,saldoDeu,saldoMaq,saldoMob,saldoEq,saldoAcre,saldoPro,saldoCos,saldoVen]
cuentas={'Cuentas':cuentasList,"saldos":saldosList}
cuentas2={'Cuentas':cuentasList}

#se elaboraron 4 funciones una para el menu, otra para el registro, otra mas para la impresion de los saldos de una cuenta en particular y una ultima con
#opcion para salir
def menu():
    os.system("cls")
    desicion=int(input("Elija una opcion, despues introduzca el numero y de ENTER \n 1.  Registrar un nuevo movimiento \n 2. Saldo de una cuenta especifica \n 3. Salir\n"))
    if desicion==1:
        os.system("cls")#comando para limpiar pantalla de la consola
        print("cargando")
        os.system("cls")
        regmov()
        
    if desicion==2:
        os.system("cls")
        print("cargando...")
        time.sleep(4)
        os.system("cls")
        mostrardatos()
        
    if desicion==3:
        os.system("cls")
        print("Cerrando el programa...")
        time.sleep(5)
        salir()
    if desicion!=(1,2,3):
        os.system("cls")
        print("Opcion no correcta dirigiendo al menu principal...")
        time.sleep(4)
        os.system("cls")
        print("Intente de nuevo")
        menu()
        



def regmov():#funcion para insertar registros
    print(tabulate(cuentas2, headers=["Cuentas"]))
    desicion2=int(input("Numero de la cuenta que desea afectar en el Cargo\n"))-1
    

    desicion3=int(input("Numero de la cuenta que afectara en el Abono\n"))-1


    
    desicion4=(input("Nombre de las cuentas por afectar \n""Cargo " +cuentas["Cuentas"][desicion2]+ "\n"+ "Abono "+cuentas["Cuentas"][desicion3]+" \n¿Es correcto?  "))
    print("Cargando...")
    time.sleep(4)
    os.system("cls")

    desicion4.lower()
    if desicion4=="si" and desicion2 != 8 and desicion2 != 9 and desicion2!=11 and desicion3 !=0 and desicion3!=1 and desicion3!=2 and desicion3!=3 and desicion3!=4 and desicion3!=5 and desicion3!=6 and desicion3!=7 and desicion3!=10:
        Monto=float(input("Monto por cargar/abonar \n"))
        cuentas["saldos"][desicion2]=cuentas["saldos"][desicion2]+Monto
        cuentas["saldos"][desicion3]=cuentas["saldos"][desicion3]+Monto
        desicion6=input("¿Desea agregar un registro mas?\n")
        desicion6.lower()
        if desicion6=="si":
            regmov()
        if desicion6=="no":
            print("Redirigiendo al menu...")
            menu()
    if desicion4=="si" and desicion3 != 8 and desicion3 != 9 and desicion3 != 11 and desicion2 !=0 and desicion2!=1 and desicion2!=2 and desicion2!=3 and desicion2!=4 and desicion2!=5 and desicion2!=6 and desicion2!=7 and desicion2!=10:
    
        Monto=float(input("Monto por cargar/abonar\n"))
        cuentas["saldos"][desicion2]=cuentas["saldos"][desicion2]-Monto
        cuentas["saldos"][desicion3]=cuentas["saldos"][desicion3]-Monto
        desicion6=input("¿Desea agregar un registro mas?\n")
        desicion6.lower()
        if desicion6=="si":
            regmov()
        if desicion6=="no":
            print("Redirigiendo al menu...")
            menu()

    if desicion4=="si" and desicion2 != 8 and desicion2 != 9 and desicion2!=11 and desicion3 !=8 and desicion3!=9 and desicion3!=11:

        
        Monto=float(input("Monto por cargar/abonar\n"))
        cuentas["saldos"][desicion2]=cuentas["saldos"][desicion2]+Monto
        cuentas["saldos"][desicion3]=cuentas["saldos"][desicion3]-Monto
        desicion6=input("¿Desea agregar un registro mas?\n")
        desicion6.lower()
        if desicion6=="si":
            regmov()
        if desicion6=="no":
            print("Redirigiendo al menu...")
            menu()
        
           
    
    if desicion4=="si" and  desicion2 !=0 and desicion2!=1 and desicion2!=2 and desicion2!=3 and desicion2!=4 and desicion2!=5 and desicion2!=6 and desicion2!=7 and desicion2!=10 and desicion3 !=0 and desicion3!=1 and desicion3!=2 and desicion3!=3 and desicion3!=4 and desicion3!=5 and desicion3!=6 and desicion3!=7 and desicion3!=10:
        Monto=float(input("Monto por cargar/abonar\n"))
        cuentas["saldos"][desicion2]=cuentas["saldos"][desicion2]-Monto
        cuentas["saldos"][desicion3]=cuentas["saldos"][desicion3]+Monto
        desicion6=input("¿Desea agregar un registro mas?\n")
        desicion6.lower()
        if desicion6=="si":
            regmov()
        if desicion6=="no":
            print("Redirigiendo al menu...")
        menu()
    if desicion4=="no":
        print("Dirigiendose al menu, los datos se desecharan, intente de nuevo ingresando a la opcion correspondiente ")
    if desicion4!=("si","no"):
        print("Datos introducidos no validos, regresando al menu")
        menu()


def mostrardatos():#funcion para impirmir datos
    print(tabulate(cuentas2,headers=["Cuentas"]))
    desicion8=int(input("Numero de la cuenta de la cual desea ver el saldo : \n"))-1
    cuenta=cuentas["Cuentas"][desicion8]
    saldo=float(cuentas["saldos"][desicion8])
    os.system("cls")
    print("Cargando...")
    os.system("cls")
    time.sleep(5)
    print("Cuenta: \n"+ cuenta +"\nSaldo: \n"+ str(saldo))
    

    desicion9=int(input("1 para volver al menu \n2 para salir del programa"))
    if desicion9==1:
        os.system("cls")
        print("Cargando...")
        time.sleep(3)
        menu()
    if desicion9==2:
        salir()
def salir():#funcion para salir del programa
    sys.exit()#comando para salir del sistema

print(" PIA INTRODUCCION A LA PROGRAMACION \n EQUIPO NUMERO # \n ADVERTENCIA: LEA BIEN LAS INSTRUCCIONES YA QUE UNA MALA MANIPULACION DEL PROGRAMA PUEDE HACER \n QUE ESTE SE CAEGA.")
time.sleep(15)
try:
    menu()#se llama a la funcion menu para que se pueda empezar a correr el codigo
except ValueError:
    print("Ha introducido un valor no valido, para guardar la integridad del programa este se cerrara")
    time.sleep(10)
    salir()