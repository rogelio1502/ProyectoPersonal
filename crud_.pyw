import os,sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from sqlite3 import IntegrityError
from sqlite3 import OperationalError
#listas y variables globales ventana sell
con=0
productos=list()
c=0
cn=0
total=0
_id_venta=0
_id_cliente=0
#listas y variables globales add
codigos=list()
continuar=False
#listas y variables globales mod
_codigos=list()


class MainWindow:
    
    #Le pasamos el componente raiz al constructor
    def __init__(self,root):
        
        self.root=root
        #titulo
        self.root.title("Gestion de Productos v1.0.1")
        self.root.geometry('1500x631')
        #barra menu root
        self.barra_Menu=Menu(self.root)
        self.root.config(menu=self.barra_Menu)
        #inicio opcion
        self.inicioMenu = Menu(self.barra_Menu, tearoff=0)
        self.inicioMenu.add_command(label="AGREGAR PRODUCTO",command=self.segunda)
        self.barra_Menu.add_cascade(label="INICIO",menu=self.inicioMenu)
        #frame
        self.frame1=Frame(self.root).grid(row=1,column=1,padx=300,pady=10)
        #boton add producto
        
        self.btn_add=Button(self.frame1,text="Añadir Producto",command= self.segunda,fg="White",bg="black",height=5,width=15).grid(row=1,column=2,padx=10,pady=10)
        #boton ver productos
        self.btn_ver=Button(self.frame1,text="Listar Productos",command=self.verProductos,fg="White",bg="black",height=5,width=15).grid(row=2,column=2,padx=10,pady=10)
        #boton modificar producto
        self.btn_mod=Button(self.frame1,text="Modificar Producto", command=self.modificar,fg="White",bg="black",height=5,width=15).grid(row=3,column=2,padx=10,pady=10)
        #boton venta
        self.btn_venta=Button(self.frame1,text="Venta",command=self.venta,fg="White",bg="black",height=5,width=15).grid(row=4,column=2,padx=10,pady=10)
        #boton salir 
        self.btn_exit=Button(self.frame1,text="Salir",command=self.salir,fg="White",bg="black",height=5,width=15).grid(row=5,column=2,padx=10,pady=10)
    #funcion para salir del programa
    def salir(self):
        pregunta=messagebox.askyesno('SALIR','¿DESEA SALIR?')
        if pregunta:

            sys.exit()
    #funcion que abre la ventana para agregar productos
    def segunda(self):
        self.root.iconify()
        class SecondWindow:
            def __init__(self,root):
                self.root=root
                self.root.title("Agregar Producto -Gestion de Productos v.1.0.1")
                self.root.geometry('1500x629')
                self.numero=StringVar()
                self.nombre=StringVar()
                self.precio=StringVar()
                self.cantidad=StringVar()
                #barra menu crud_2
                self.barra_Menu=Menu(self.root)
                self.root.config(menu=self.barra_Menu)
                #inicio opcion
                self.inicioMenu = Menu(self.barra_Menu, tearoff=0)
                self.inicioMenu.add_command(label="Limpiar",command=self.clear)
                self.barra_Menu.add_cascade(label="Opciones",menu=self.inicioMenu)
                #frame
        
                self.frame_SV_1=Frame(self.root)
                self.frame_SV_1.pack()
                #id
                self.numeroProdLabel=Label(self.frame_SV_1,text="Codigo ").grid(row=1,column=1,padx=10,pady=10)
                self.numeroProdEntry=Entry(self.frame_SV_1,textvariable=self.numero).grid(row=2,column=1,padx=10,pady=10)
                #nombre
                self.nombreProdLabel=Label(self.frame_SV_1,text="Nombre ").grid(row=3,column=1,padx=10,pady=10)
                self.nombreProdEntry=Entry(self.frame_SV_1,textvariable=self.nombre).grid(row=4,column=1,padx=10,pady=10)
                #precio
                self.precioLabel=Label(self.frame_SV_1,text="Precio ").grid(row=5,column=1,padx=10,pady=10)
                self.precioEntry=Entry(self.frame_SV_1,textvariable=self.precio).grid(row=6,column=1,padx=10,pady=10)
                #cantidad
                self.cantidadLabel=Label(self.frame_SV_1,text="Cantidad").grid(row=7,column=1,padx=10,pady=10)
                self.cantidadEntry=Entry(self.frame_SV_1,textvariable=self.cantidad).grid(row=8,column=1,padx=10,pady=10)
                #boton añadir
                self.añadir=Button(self.frame_SV_1,text="Add",fg="White",bg="black",command=lambda:self.añadir_producto\
                (self.numero.get(),self.nombre.get(),self.precio.get(),self.cantidad.get())).grid(row=9,column=1,padx=10,pady=10)
                #boton salir
                self.salir=Button(self.frame_SV_1,fg="White",bg="black",text="Volver",command=self.salir).grid(row=10,column=1,padx=10,pady=10)

            def salir(self):
                pregunta=messagebox.askyesno('SALIR','¿DESEA SALIR AL MENU PRINCIPAL?')
                if pregunta:
                    self.root.destroy()
                    os.execl(sys.executable, sys.executable, *sys.argv)
            def añadir_producto(self,codigo,nombre,precio,cantidad):
                global continuar


                if len(codigo)>0 and len(nombre)>0 and len(precio) >0 and len(cantidad)>0:

                    if codigo.isdigit():
                        conexion=sqlite3.connect('Gestion_Productos_0.db')
                        try:
                            cursor=conexion.cursor()
                            cursor.execute("SELECT * FROM PRODUCTOS")

                            rows= cursor.fetchall()
                            conexion.close()
                            for i in range(len(rows)):
                                codigos.append(str(rows[i][0]))
                        except sqlite3.OperationalError:
                            continuar=True
                   
                        if codigo not in codigos or continuar==True:
                            if precio.isdigit():
                                if cantidad.isdigit():

                                    conexion=sqlite3.connect("Gestion_Productos_0.db")
                                    cursor=conexion.cursor()
                                    try:
                                        cursor.execute(''' CREATE TABLE PRODUCTOS (
                                        CODIGO INT PRIMARY KEY, NOMBRE_PRODUCTO VARCHAR(50), PRECIO INT,CANTIDAD INT
                                        )''')
                                        
                          
                                    
                                    except sqlite3.OperationalError:
                                        messagebox.showinfo("Operational ","Conectando con la base de datos.")
                                        messagebox.showinfo("Info","Se establecio conexion con la base de datos.")
                                    else:
                                        messagebox.showinfo("Info","Base de datos creada con exito.")
                        
                                    try:
                                        cursor.execute(''' INSERT INTO PRODUCTOS VALUES (?,?,?,?) ''',(codigo,nombre,precio,cantidad))
                                        conexion.commit()
                                        conexion.close()
                                    except sqlite3.IntegrityError:
                                        messagebox.showerror("Error","Ya existe un producto\ncon el codigo introducido")
                                    else:
                                        messagebox.showinfo("Info","DONE.")
                                        self.clear()

                                        
                                else :
                                    messagebox.showerror("Error","El campo 'Cantidad' solo\nacepta valores numericos")
                            else :
                                messagebox.showerror("Error","El campo 'Precio' solo\nacepta valores numericos")
                        else:
                            messagebox.showerror("Error","Ya existe un producto\ncon el codigo introducido")
                    else :
                        messagebox.showerror("Error","El campo 'Codigo' solo\nacepta valores numericos")
                else :
                    messagebox.showerror("Error","Campos incompletos,\nfavor de verificar")
            
            def clear(self):
                self.numero.set("")
                self.nombre.set("")
                self.precio.set("")
                self.cantidad.set("")
        s2=Toplevel()

        SecondWindow(s2)
    #funcion que abre la ventana para ver el stock
    def verProductos(self):
        self.root.iconify()
        class ThirdWindow:
            def __init__(self,root):
                root.title("Lista de Productos -Gestion de Productos v.1.0.1")
                root.geometry('1000x629')
                self.buscado=StringVar()
                self.root=root
                #buscar
                self.buscar=Entry(self.root,textvariable=self.buscado).pack()
                self.btn_buscar=Button(self.root,text="Search",fg="White",bg="black",command=self.filling_search).pack()
                #arbol
                self.tree=ttk.Treeview(self.root)
                self.tree["columns"]=("one","two","three")
                self.tree.column("#0",stretch=NO)
                self.tree.column("one",stretch=NO)
                self.tree.column("two",stretch=NO)
                self.tree.column("three",stretch=NO)
                self.tree.pack()
                self.tree.heading("#0",text="ID",anchor=W)
                self.tree.heading("one", text="Name",anchor=W)
                self.tree.heading("two", text="Price",anchor=W)
                self.tree.heading("three", text="Quantity",anchor=W)
                self.filling()
        
                #botones
                self.btn=Button(self.root,text="Imprime",fg="White",bg="black",command=self.imprimirProducto).pack()
                self.btn=Button(self.root,text="Refresh",fg="White",bg="black",command=self.filling).pack()
                self.btn=Button(self.root,text="Volver",fg="White",bg="Red",command=self.salir).pack()
            def salir(self):
                pregunta=messagebox.askyesno('SALIR','¿DESEA SALIR AL MENU PRINCIPAL?')
                if pregunta:
                    self.root.destroy()
                    os.execl(sys.executable, sys.executable, *sys.argv)
            def filling_search(self):
                records = self.tree.get_children()
                for element in records:
                    self.tree.delete(element)
        
                conexion=sqlite3.connect('Gestion_Productos_0.db')
                cursor=conexion.cursor()
                cursor.execute(f"SELECT * FROM PRODUCTOS WHERE NOMBRE_PRODUCTO LIKE '%{self.buscado.get()}%' OR CODIGO='{self.buscado.get()}'")

                rows= cursor.fetchall()

                for i in range(len(rows)):
                    self.tree.insert("","end",text=rows[i][0],values=(rows[i][1],rows[i][2],rows[i][3]))
        
            def filling(self):
                records = self.tree.get_children()
                for element in records:
                    self.tree.delete(element)
                try:
                    conexion=sqlite3.connect('Gestion_Productos_0.db')
                    cursor=conexion.cursor()
                    cursor.execute("SELECT * FROM PRODUCTOS")

                    rows= cursor.fetchall()

                    for i in range(len(rows)):
                        self.tree.insert("","end",text=rows[i][0],values=(rows[i][1],rows[i][2],rows[i][3]))
                except:
                    messagebox.showerror("Error","No se tiene registro alguno\nen la base de datos")
        
            def imprimirProducto(self):
                try:
                    self.tree.item(self.tree.selection())['text']
                except IndexError as e:
                    print('Please select a record')
                    return
                name = self.tree.item(self.tree.selection())['values'][0]
                print(name)
                self.filling()
        t3=Toplevel()
        ThirdWindow(t3)
    #funcion que abre la ventana para agregar ventas
    def venta(self): 
        self.root.iconify()
        
        class SellWindow:
            def __init__(self,root):
                #importamos variables globales
                global _id_cliente,_id_venta
                #vstringvar
                self.pagoSV=StringVar()
                self.totalSV=StringVar()
                self.cod_articulo=StringVar()
                self.estatusvar=StringVar()
                self.idventa=StringVar()
                self.idcliente=StringVar()
                #se apropia del root en la variable propia self
                #configuracion de la pagina
                self.root=root
                self.root.title("Venta - Gestion de Productos")
                self.root.geometry('1500x631')
                #se determina numero de cliente y numero de venta
        
                try:
                    conexion=sqlite3.connect("Gestion_Productos_0.db")
                    cursor=conexion.cursor()
                    cursor.execute("SELECT ID_VENTA FROM VENTAS")
                    ventas=cursor.fetchall()
            
                    _id_venta=(ventas[-1][0]+1)
        
        
        
                except:
                    _id_venta=1

                try:
    
                    cursor.execute("SELECT ID_CLIENTE FROM CLIENTE_COMPRA")
                    clientes=cursor.fetchall()
                    conexion.close()
                    _id_cliente=(clientes[-1][0]+1)            
        
            
                except:
            
                    _id_cliente=1
                self.idcliente.set(_id_cliente)
                self.idventa.set(_id_venta)
                #componentes
                #id cliente
                self.textventa=Label(self.root,text="VENTA NO.").grid(row=3,column=1,padx=10,pady=10)
                self.venta=Label(self.root,textvariable=self.idventa).grid(row=3,column=2,padx=10,pady=10)
                #id venta
                self.textventa=Label(self.root,text="CLIENTE NO.").grid(row=4,column=1,padx=10,pady=10)
                self.cliente=Label(self.root,textvariable=self.idcliente).grid(row=4,column=2,padx=10,pady=10)
                #articulo
                self.articulo=Label(self.root,text="Codigo del producto").grid(row=0,column=1,padx=10,pady=10)
                self.articuloEntry=Entry(self.root,textvariable=self.cod_articulo).grid(row=0,column=2,padx=10,pady=10)
                #estatus
                self.estatus=Label(self.root,textvariable=self.estatusvar,fg="Blue").grid(row=1,column=1,padx=4,pady=10)
                #grabar
                self.btn_grabar=Button(self.root,text="Grabar",fg="White",bg="black",command=self.grabar).grid(row=1,column=3,padx=10,pady=10)
        
                #demo
                #self.btn_demo=Button(self.root,text="Demo",command=self.demo).grid(row=2,column=3,padx=10,pady=10)
                #view
                #lista donde se van poniendo los productos que marcamos (terminado)
                self.tree=ttk.Treeview(self.root)
                self.tree["columns"]=("one","two")
                self.tree.column("#0",stretch=NO)
                self.tree.column("one",stretch=NO)
                self.tree.column("two",stretch=NO)
                self.tree.grid(row=0,column=3)
                self.tree.heading("#0",text="ID",anchor=W)
                self.tree.heading("one", text="Name",anchor=W)
                self.tree.heading("two", text="Price",anchor=W)
                #scroll
                self.scroll=Scrollbar(self.root, command=self.tree.yview)
                self.scroll.grid(row=0,column=4,sticky="nsew")
                self.tree.config(yscrollcommand=self.scroll.set)
                #total
                self.totalLabel=Label(self.root,text="TOTAL").grid(row=1,column=6,padx=10,pady=10)
                self.totalEntry=Entry(self.root,textvariable=self.totalSV,font=("Verdana",15),state="readonly").grid(row=1,column=7,padx=10,pady=10)
                
                #pago
                self.pagolLabel=Label(self.root,text="RECIBO").grid(row=2,column=6,padx=10,pady=10)
                self.pagoEntry=Entry(self.root,textvariable=self.pagoSV,font=("Verdana",15),justify=LEFT).grid(row=2,column=7,padx=10,pady=10)
                #menu principal
                self.btn_menu=Button(self.root,text="VOLVER",command=self.salir).grid(row=7,column=3,padx=10,pady=10)

                self.root.bind('<Return>',self.Buscar)
                self.totalSV.set("0")
            def salir(self):
                pregunta=messagebox.askyesno('SALIR','¿DESEA SALIR AL MENU PRINCIPAL?\nSE PERDERAN LOS DATOS CAPTURADOS')
                if pregunta:
                    self.root.destroy()
                    os.execl(sys.executable, sys.executable, *sys.argv)


            def funcion(self):
        
        
                conexion=sqlite3.connect("Gestion_Productos_0.db")
                cursor=conexion.cursor()
                cursor.execute(f"SELECT CANTIDAD FROM PRODUCTOS WHERE CODIGO={self.cod_articulo.get()}")            
                q=cursor.fetchall()
                _q=(q[-1][0])
                conexion.close()
                if _q>0:
                    global c
        
                    del(self.estatus)
                    self.estatus=Label(self.root,textvariable=self.estatusvar,fg="Blue").grid(row=1,column=1,padx=4,pady=10)

                    self.estatusvar.set(">>")

                    conexion=sqlite3.connect("Gestion_Productos_0.db")
                    cursor=conexion.cursor()
                    cursor.execute(f"SELECT CODIGO,NOMBRE_PRODUCTO,PRECIO FROM PRODUCTOS WHERE CODIGO={self.cod_articulo.get()}")            
                    rows=cursor.fetchall()
                    conexion.close()           
                    for i in range(len(rows)):
                        c=c+1
                        self.item=self.tree.insert("","end",text=rows[i][0],values=(rows[i][1],rows[i][2]),iid=c)
    
                        self.tree.see(self.item)
                    global con
                    con=len(rows)
                    if con ==0:
                        del(self.estatus)
                        self.estatus=Label(self.root,textvariable=self.estatusvar,fg="red").grid(row=1,column=1,padx=4,pady=10)
                        self.estatusvar.set(">>ARTICLE NOT FOUND")
                    else:
                        self.estatusvar.set(">>DONE")
                    records = self.tree.get_children()
                    vendido=list()
                    for i in range(len(records)):
            
                        vendido.append(int(self.tree.item(i+1)['values'][1]))
            
                    self.totalSV.set(sum(vendido))
                    del(vendido)
                    self.cod_articulo.set("")
                    
                else:
                    del(self.estatus)
                    self.estatus=Label(self.root,textvariable=self.estatusvar,fg="red",font=("VERDANA",10)).grid(row=1,column=1,padx=4,pady=10)
                    self.estatusvar.set(f">>NO SE CUENTA CON \nINVENTARIO\nDEL PRODUCTO CON \nCODIGO {self.cod_articulo.get()}")
            def Buscar(self,event):
                try:
                    conexion=sqlite3.connect("Gestion_Productos_0.db")
                    cursor=conexion.cursor()
                    cursor.execute(f"SELECT CODIGO,NOMBRE_PRODUCTO,PRECIO FROM PRODUCTOS WHERE CODIGO={self.cod_articulo.get()}")            
                    rows=cursor.fetchall()
                    conexion.close()
                except:
                    del(self.estatus)
                    self.estatus=Label(self.root,textvariable=self.estatusvar,fg="red",font=("VERDANA",10)).grid(row=1,column=1,padx=4,pady=10)

                    self.estatusvar.set(">>CARACTER NO VALIDO")

                else:

                    self.funcion()
            def grabar(self):
                try:
                    if int(self.pagoSV.get())>int(self.totalSV.get()):
                        
                        try:
                            conexion=sqlite3.connect("Gestion_Productos_0.db")
                            cursor=conexion.cursor()
                            cursor.execute("CREATE TABLE VENTAS (ID_VENTA INT PRIMARY KEY, MONTO INT)")
                            cursor.execute("CREATE TABLE CLIENTE_COMPRA (ID_CLIENTE INT , ID_ARTICULO INT, FOREIGN KEY (ID_ARTICULO) REFERENCES PRODUCTOS(CODIGO))")
                            conexion.close()
                        except:
                            del(self.estatus)
                            self.estatus=Label(self.root,textvariable=self.estatusvar,fg="blue",font=("VERDANA",15)).grid(row=1,column=1,padx=4,pady=10)

                            self.estatusvar.set(">>GRABANDO")
                        else:
                            del(self.estatus)
                            self.estatus=Label(self.root,textvariable=self.estatusvar,fg="blue",font=("VERDANA",15)).grid(row=1,column=1,padx=4,pady=10)

                            self.estatusvar.set(">>COBRADO")
                        try:
                            conexion=sqlite3.connect("Gestion_Productos_0.db")
                            cursor=conexion.cursor()
                            cursor.execute(f"INSERT INTO VENTAS VALUES({_id_venta},{self.totalSV.get()})")
                            records = self.tree.get_children()
        
                            for i in range(len(records)):
            
                                cursor.execute(f"INSERT INTO CLIENTE_COMPRA VALUES ({_id_cliente},{self.tree.item(i+1)['text']})")
                
                            for i in range(len(records)):
                                cursor.execute(f"UPDATE PRODUCTOS SET CANTIDAD = (SELECT CANTIDAD FROM PRODUCTOS WHERE CODIGO={self.tree.item(i+1)['text']})-1 WHERE CODIGO = {self.tree.item(i+1)['text']}")
                            conexion.commit()
                            conexion.close()
                        except:
                            messagebox.showinfo("ERROR","CODIGO XXXXXXX")
                        else:
                            cambio=int(self.pagoSV.get())-int(self.totalSV.get())
                            messagebox.showinfo("COMPLETED","THE SELLING HAS BEEN RECORDED")
                            messagebox.showinfo("CAMBIO","El cambio es de "+str(cambio)+" pejo mijo")
                            #se destruye ventana
                            self.root.destroy()
                            #se ejecuta la siguiente linea para que se reinicie el programa y no haya errores
                            os.execl(sys.executable, sys.executable, *sys.argv)
                    else:
                        messagebox.showerror("Error","Importe recibido debe ser mayor al por pagar")         
            

                except:
                    messagebox.showerror("Error","No es posible pagar con letras")         
            
            #funcion para pruebas
            def demo(self):
                pass
        v4=Toplevel()        
        SellWindow(v4)
    #funcion que abre la ventana para modificar un producto
    def modificar(self):
        self.root.iconify()
        


        class FifthWindow:
            def __init__(self,root):
                self.root=root
                self.root.title("Modificar Producto -Gestion de Productos v.1.0.1")
                self.root.geometry('1500x631')
                self.numero=StringVar()
                self.nombre=StringVar()
                self.precio=StringVar()
                self.cantidad=StringVar()
                self.estatus=StringVar()
                #barra menu crud_2
                self.barra_Menu=Menu(self.root)
                self.root.config(menu=self.barra_Menu)
                #inicio opcion
                self.inicioMenu = Menu(self.barra_Menu, tearoff=0)
                self.inicioMenu.add_command(label="Limpiar",command=self.clear)
                self.barra_Menu.add_cascade(label="Opciones",menu=self.inicioMenu)
                #frame
                self.frame_SV_1=Frame(self.root)
                self.frame_SV_1.grid(row=1,column=1,padx=525,pady=10)
                #id
                self.numeroProdLabel=Label(self.frame_SV_1,text="Codigo ").grid(row=1,column=0,padx=10,pady=10)
                self.numeroProdEntry=Entry(self.frame_SV_1,textvariable=self.numero).grid(row=2,column=0,padx=10,pady=10)
                #buscar
                self.btn_buscar=Button(self.frame_SV_1,text="BUSCAR",command=self.buscar).grid(row=3,column=0,padx=10,pady=10)
                #nombre
                self.nombreProdLabel=Label(self.frame_SV_1,text="Nombre ").grid(row=4,column=0,padx=10,pady=10)
                self.nombreProdEntry=Entry(self.frame_SV_1,textvariable=self.nombre).grid(row=5,column=0,padx=10,pady=10)
        
                #precio
                self.precioLabel=Label(self.frame_SV_1,text="Precio ").grid(row=6,column=0,padx=10,pady=10)
                self.precioEntry=Entry(self.frame_SV_1,textvariable=self.precio).grid(row=7,column=0,padx=10,pady=10)
                #cantidad
                self.cantidadLabel=Label(self.frame_SV_1,text="Cantidad").grid(row=8,column=0,padx=10,pady=10)
                self.cantidadEntry=Entry(self.frame_SV_1,textvariable=self.cantidad).grid(row=9,column=0,padx=10,pady=10)
                #estatus
                self.estatus_l=Label(self.frame_SV_1,textvariable=self.estatus).grid(row=11,column=0,padx=10,pady=10)
                #boton añadir
                self.añadir=Button(self.frame_SV_1,text="Editar",command=self.mod_producto).grid(row=12,column=0,padx=10,pady=10)
                #boton salir
                self.salir=Button(self.frame_SV_1,text="Volver",command=self.salir).grid(row=13,column=0,padx=10,pady=10)
                #funcion que hace que salas de la ventana y se recargue el sistema
            def salir(self):
                pregunta=messagebox.askyesno('SALIR','¿DESEA SALIR AL MENU PRINCIPAL?\nSE PERDERAN LOS DATOS CAPTURADOS\nQUE NO HAYAN SIDO GUARDADOS')
                if pregunta:
                    self.root.destroy()
                    os.execl(sys.executable, sys.executable, *sys.argv)
            #funcion que modifica el producto en cantidad,nombre o precio (en progreso)
            def mod_producto(self):
        
                codigo=self.numero.get()
                nombre=self.nombre.get()
                cantidad=self.cantidad.get()
                precio=self.precio.get()
                try:

                    conexion=sqlite3.connect("Gestion_Productos_0.db")
                    cursor=conexion.cursor()
                    cursor.execute("UPDATE PRODUCTOS SET NOMBRE_PRODUCTO=? WHERE CODIGO=?",(nombre,int(codigo)))
                    cursor.execute("UPDATE PRODUCTOS SET CANTIDAD=? WHERE CODIGO=?",(int(cantidad),int(codigo)))
                    cursor.execute("UPDATE PRODUCTOS SET PRECIO=? WHERE CODIGO=?",(int(precio),int(codigo)))
                    conexion.commit()
                    cursor.close()
                    conexion.close()
                except sqlite3.OperationalError:

                    self.estatus.set("ERROR EN LA BASE DE DATOS, FAVOR DE COMUNICARSE CON SOPORTE")
                else:
                    self.estatus.set("DONE")
                    self.clear()
        
            #funcion que busca un producto y arroja el nombre, precio y cantidad (terminada)
            def buscar(self):
        
                conexion=sqlite3.connect('Gestion_Productos_0.db')
                cursor=conexion.cursor()
                cursor.execute(f"SELECT NOMBRE_PRODUCTO,PRECIO,CANTIDAD FROM PRODUCTOS WHERE CODIGO={self.numero.get()}")
                producto=cursor.fetchall()
                conexion.close()
                nombreV=producto[0][0]
                precio=producto[0][1]
                q_producto=producto[0][2]
                self.precio.set(precio)
                self.cantidad.set(q_producto)
                self.nombre.set(nombreV)
        
            #funcion que limpia los campos (terminada)
            def clear(self):
                self.numero.set("")
                self.nombre.set("")
                self.precio.set("")
                self.cantidad.set("")
        
        m5=Toplevel()
        FifthWindow(m5)

if __name__=='__main__':

    app = Tk()

    window = MainWindow(app)
    app.mainloop()
