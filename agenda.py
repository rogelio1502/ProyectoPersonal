claves=list()
nombres=list()
telefonos=list()
edades=list()
contactos=list()


def AgregarContacto():
    while True:
        clave=input("Clave del contacto")
        if clave in claves:
            
            while clave in claves:
                clave=input("La clave ya esta ocupada\n escoja una nueva")
        claves.append(clave)
        nombre=input("Nombre del contacto:\n")
        nombres.append(nombre)
        telefono=input("Telefono Celular:\n")
        if telefono.isdigit() == False:
            print(telefono)
            while telefono.isdigit() == False:
                telefono=input("El telefono celular que ingreso tiene un caracter no valido\nTelefono Celular:")
        telefonos.append(telefono)
        edad=input("Edad")
        if edad.isdigit() == False:
            while edad.isdigit()==False:
                edad=input("El valor ingresado no es valido \nEdad\n: ")
        edades.append(edad)
        
        if claves[-1]==clave and nombres[-1]==nombre and telefonos[-1]==telefono and edades[-1]==edad:
            
            print("Done")
            contactos.append(clave+" "+nombre+" "+telefono+" "+edad)
            break
            
        else:
            print("ALgo ha salido mal, intente de nuevo")
            break
    Menu()
        
def BuscarContacto():
    if len(contactos)>0:
        claveAbuscar=input("Clave ")
        
        while not claveAbuscar in claves:
            ids=input("No existe tal contacto...\n intente de nuevo, o teclee 'exit' para salir")
            if ids=='exit':
                Menu()
        ids=claves.index(claveAbuscar)
        print(f'Clave:\n{claves[ids]} Nombre:\n{nombres[ids]} Telefono:\n {telefonos[ids]} Edad:\n{edades[ids]}')
        Menu()
    elif len(contactos)==0:
        print("Lista de contactos vacia, favor de agregar un contacto")
        Menu()
def EliminarContacto():
    if len(contactos)>0:
        e=0
        for i in contactos:
            print(f'Clave:{claves[e]} Nombre:{nombres[e]} Telefono:{telefonos[e]} Edad:{edades[e]}')
            e=e+1
        ids1=(input("Clave del que desea borrar"))
        while not ids1 in claves:
            ids1=input("No existe tal contacto...\n intente de nuevo, o teclee 'exit' para salir")
            if ids1=='exit':
                Menu()
        
        claveAborrar=claves.index(ids1)
        contactos.pop(claveAborrar)
        claves.pop(claveAborrar)
        nombres.pop(claveAborrar)
        telefonos.pop(claveAborrar)
        edades.pop(claveAborrar)

        
        print("DONE")
        Menu()
    
    
    elif len(contactos)==0:
        print("Lista de contactos vacia, favor de agregar un contacto")
        Menu()
    
def ModificarContacto():
    if len(contactos)>0:
        e=0
        for i in contactos:
            print(f'Clave:{claves[e]} Nombre:{nombres[e]} Telefono:{telefonos[e]} Edad:{edades[e]}')
            e=e+1
        indexAmodificar=input('Clave del Contacto que desea modificar')
        
        while not indexAmodificar in claves:
            indexAmodificar=input("No existe tal contacto...\n intente de nuevo, o teclee 'exit' para salir")
            if indexAmodificar=='exit':
                Menu()
        ids2=claves.index(indexAmodificar)
        print(f'Clave:{claves[ids2]} Nombre:{nombres[ids2]} Telefono:{telefonos[ids2]} Edad:{edades[ids2]}')
        eleccion=int(input('1 modificar nombre, 2 modificar telefono, 3 modificar edad'))
        if eleccion == 1 :
            nombres[ids2]=input("Nuevo nombre:\n")
            contactos[ids2]=(claves[ids2]+" "+nombres[ids2]+" "+telefonos[ids2]+" "+edades[ids2])
            print("DONE")
        elif eleccion == 2 :
            telefonoChange=input("Nuevo Telefono:\n")
            if telefonoChange.isdigit() == False:
                print(telefonoChange)
                while telefonoChange.isdigit() == False:
                    telefonoChange=input("El telefono celular que ingreso tiene un caracter no valido\nTelefono Celular:")
            telefonos[ids2]=telefonoChange
            contactos[ids2]=(claves[ids2]+" "+nombres[ids2]+" "+telefonos[ids2]+" "+edades[ids2])
            print("DONE")
        elif eleccion == 3 :
            edadChange=input("Nueva Edad:\n")
            if edadChange.isdigit() == False:
                while edadChange.isdigit()==False:
                    edadChange=input("El valor ingresado no es valido \nEdad\n: ")
            edades[ids2]=edadChange
            contactos[ids2]=(claves[ids2]+" "+nombres[ids2]+" "+telefonos[ids2]+" "+edades[ids2])
            print("DONE")
        else:
            print("opcion no existe, se reedigira al menu")
            Menu()
        
        Menu()
    elif len(contactos)==0:
        print("Lista Vacia, favor de agregar un Contacto")
        Menu()
    
def ListarContactos():
    if len(contactos)>0:
        e=0
        for i in contactos:
            print(f'Clave:{claves[e]} Nombre:{nombres[e]} Telefono:{telefonos[e]} Edad:{edades[e]}')
            e=e+1
        Menu()
    elif len(contactos)==0:
        print("Lista de Contactos vacia, favor de agregar un contacto")
        Menu()
    
def salir():
    sys.exit()
    
    
def Menu():
    
    eleccion=(input('''Elija La opcion que desee:
\n1.-Agregar Contacto\n2.-Buscar Contacto Por Clave\n3.-Eliminar Contacto\n4.-Modificar Contacto\n5.-Listar Contactos\n6.-Salir'''))
    while eleccion.isdigit()==False:
        print("No existe tal opcion")
        Menu()
    eleccion=int(eleccion)
    if eleccion==1:
        AgregarContacto()
    elif eleccion==2:
        BuscarContacto()
    elif eleccion==3:
        EliminarContacto()
    elif eleccion==4:
        ModificarContacto()
    elif eleccion==5:
        ListarContactos()
        
    elif eleccion==6:
        salir()
        
    else:
        print("opcion no existe")
        Menu()
    
    

Menu()