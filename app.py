import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import os

NOMBRE = "MARIANO NICOLÁS RIVADENEIRA" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4) = 7

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9. 9-7 = 2

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=6, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        self.lista_nombre = []
        self.lista_monto = []
        self.lista_tipo_instrumento = []
        self.lista_cantidad_instrumento = []

        self.cantidad_operaciones = 10
    def btn_cargar_datos_on_click(self):
        verificando = True

        for persona in range(self.cantidad_operaciones):
            verificando = True
            while(verificando):

                nombre = prompt(f"Datos de la persona {(persona+1)}","Ingresar nombre")
                if(nombre != None):
                    if(nombre.isalpha()):
                        nombre = nombre.capitalize()
                        self.lista_nombre.append(nombre)
                        verificando = False
                    else:
                        alert("ADVERTENCIA","El nombre debe estar expresado en letras")


            verificando = True
            while(verificando):
                monto = prompt(f"Datos de la persona {(persona + 1)}","Ingresar monto en pesos mayor a $10000")
                if(monto.isdigit()):
                    monto = int(monto)
                    if(monto > 9999):
                        self.lista_monto.append(monto)
                        verificando = False
                else:
                    alert("ADVERTENCIA","El monto debe ser mayor a $10000 expresado en símbolos numéricos")
            
            verificando = True
            while(verificando):
                tipo_instrumento = prompt(f"Datos de la persona {(persona+1)}","Seleccionar instrumento: \n CEDEAR - BONOS - MEP ")
                if(tipo_instrumento.isalpha()):
                        tipo_instrumento = tipo_instrumento.upper() 
                        match(tipo_instrumento):
                             case "CEDEAR" | "BONOS" | "MEP":
                                 self.lista_tipo_instrumento.append(tipo_instrumento)
                                 verificando = False
                             case _: 
                                alert("ADVERTENCIA","Ingresar un instrumento válido: CEDEAR - BONOS - MEP")

            verificando = True
            while(verificando):
                cantidad_instrumentos = prompt(f"Datos de la persona {(persona+1)}","Ingresar cantidad de instrumentos")
                if(cantidad_instrumentos.isdigit()):
                    cantidad_instrumentos = int(cantidad_instrumentos)
                    if(cantidad_instrumentos > 0):
                        self.lista_cantidad_instrumento.append(cantidad_instrumentos)
                        verificando = False
                    else: 
                        alert("ADVERTENCIA","La cantidad de instrumentos debe ser mayor a 0 ")

    os.system('cls') 
#......................................................................INFORME 1......................................................................
   
    def btn_mostrar_informe_1(self):
       
        print("""
---------------------LISTADO DE PERSONAS---------------------""")
        for persona in range(self.cantidad_operaciones):
            mensaje = f"""
Posición {(persona+1)}
Nombre: {self.lista_nombre[persona]}
Monto: ${self.lista_monto[persona]}
Instrumento: {self.lista_tipo_instrumento[persona]}
Cantidad de instrumentos: {self.lista_cantidad_instrumento[persona]}
""" 
            print(mensaje)
        
#......................................................................INFORME 2......................................................................
   
    def btn_mostrar_informe_2(self):
  
        comprador_menos_bonos = "Nadie"
        primer_comprado_bonos = True
        minima_cantidad_bonos = 0
        posicion = 0

        for persona in range(self.cantidad_operaciones):
            if(self.lista_tipo_instrumento[persona] == "BONOS"):
                if(primer_comprado_bonos):
                    minima_cantidad_bonos = self.lista_cantidad_instrumento[persona]
                    comprador_menos_bonos = self.lista_nombre[persona]
                    posicion = (persona+1)
                    primer_comprado_bonos = False
                elif(self.lista_cantidad_instrumento[persona] < minima_cantidad_bonos ):
                    minima_cantidad_bonos = self.lista_cantidad_instrumento[persona]
                    comprador_menos_bonos = self.lista_nombre[persona]
                    posicion = (persona+1)
        
        mensaje = f"""
-------------------MENOR COMPRADOR DE BONOS-------------------
Nombre: {comprador_menos_bonos}
Posición: {posicion}
              """
        print(mensaje)
#......................................................................INFORME 3......................................................................
    
    def btn_mostrar_informe_3(self):
        
        primer_comprador_bonos_cedear = "Nadie"
        cantidad_invertida = 0

          #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
        for persona in range(self.cantidad_operaciones):
            if(self.lista_tipo_instrumento[persona] == "BONOS" or "CEDEAR"):
                primer_comprador_bonos_cedear = self.lista_nombre[persona]
                cantidad_invertida = self.lista_cantidad_instrumento[persona]
                break
        mensaje = f"""--------------PRIMER COMPRADOR DE BONOS O CEDEAR--------------
Nombre: {primer_comprador_bonos_cedear}
Cantidad invertida: {cantidad_invertida}
        """
        print(mensaje)

#................................................................TODOS LOS INFORMES ................................................................
    
    def btn_mostrar_todos_on_click(self):
       os.system('cls')
       self.btn_mostrar_informe_1()
       self.btn_mostrar_informe_2()
       self.btn_mostrar_informe_3()

        

if __name__ == "__main__":
    app = App()
    app.mainloop()
