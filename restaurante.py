from ctypes import resize
import tkinter as tk
from tkinter.font import BOLD
from tkinter.ttk import Style
from PIL import  Image, ImageTk, ImageFilter


from tkinter import Tk, Button, Label, Radiobutton, filedialog,PhotoImage





def calcular_precios():
    
    try:

        op1= radio1.get()
        op2= radio2.get()
        op3= radio3.get()

        if(op1 == 1):
            txtPlato = "Carne asada"
            plato = pcarne
        elif(op1 == 2):
            txtPlato = "Pollo guisado"
            plato = ppollo
        elif(op1 == 3):
            txtPlato = "Lasaña"
            plato = plasagna


        if(op2 == 1):
            txtSalad = "Fresca"
            salad = pensaladas
        elif(op2 == 2):
            txtSalad = "Coditos"
            salad = pensaladas
        elif(op2 == 3):
            txtSalad = "Rusa"
            salad = pensaladas


        if(op3 == 1):
            txtBebida = "Gaseosa"
            drink = pgaseosa
        elif(op3 == 2):
            txtBebida = "Fresco"
            drink = pfresco
        elif(op3 == 3):
            txtBebida = "Café"
            drink = pcafe

        total = plato+salad+drink
        
        ##FORMATO DE FACTURA A MOSTRRAR EN LA CONSOLA CON SUS RESPECTIVOS PRECIOS
        text= f"""
            Producto              Precio

            o {txtPlato}----------- ${plato}
            o {txtSalad}------------- ${salad}
            o {txtBebida}----------- ${drink}

            • Total a  pagar ------- ${total}
        """
        print(text)
    except:

        print("LO SENTIMOS SELECCIÓN NO VÁLIDA")




ventana = Tk()

ventana.geometry("650x800")
ventana.title("Menú")
ventana.config( bg="#ADD8E6")

##precios 
pcarne= 2.50
ppollo = 2.25
plasagna = 3.00
pensaladas = 0.25
pgaseosa = 0.75
pfresco = 0.50
pcafe = 0.65
#apertura y redimensionamiento de las imagenes

carne = Image.open("Carne.jpg")
redus = carne.resize((100,100), Image.Resampling.LANCZOS)
render = ImageTk.PhotoImage(redus)

pollo = Image.open("pollo-guisado.jpg")
redus2 = pollo.resize((100,100), Image.Resampling.LANCZOS)
render2= ImageTk.PhotoImage(redus2)

lasagna = Image.open("lasaña.jpg")
redus3 = lasagna.resize((100,100), Image.Resampling.LANCZOS)
render3= ImageTk.PhotoImage(redus3)


fresca = Image.open("Fresca.jpg")
redus4 = fresca.resize((100,100), Image.Resampling.LANCZOS)
render4= ImageTk.PhotoImage(redus4)

coditos = Image.open("coditos.jpg")
redus5= coditos.resize((100,100), Image.Resampling.LANCZOS)
render5= ImageTk.PhotoImage(redus5)


rusa = Image.open("rusa.jpg")
redus6 = rusa.resize((100,100), Image.Resampling.LANCZOS)
render6= ImageTk.PhotoImage(redus6)


gaseosa = Image.open("gaseosas.jpg")
redus7 = gaseosa.resize((100,100), Image.Resampling.LANCZOS)
render7= ImageTk.PhotoImage(redus7)

fresco = Image.open("fresco.jpg")
redus8= fresco.resize((100,100), Image.Resampling.LANCZOS)
render8= ImageTk.PhotoImage(redus8)

cafe = Image.open("cafe.jpg")
redus9= cafe.resize((100,100), Image.Resampling.LANCZOS)
render9= ImageTk.PhotoImage(redus9)


lbName= Label(ventana, text= "Anas' Coffe", font="Bahnschrift")

#Instaciación de los labels platos



lbcarne = Label(ventana, image=render)


lbpollo = Label(ventana, image= render2)
lblasagna = Label(ventana, image= render3)

lbSecEnsalda = Label(ventana, text="Ensaladas")

#labels ensaladas
lbfresca = Label(ventana, image= render4)
lbcoditos = Label(ventana, image= render5)
lbrusa = Label(ventana, image= render6)

lbsecBebidas = Label(ventana, text="Bebidas")

#labels bebidas
lbgaseosa = Label(ventana, image= render7)
lbfresco = Label(ventana, image= render8)
lbcafe = Label(ventana, image= render9)

###########Instanciación para los radio buttons 

#Instaciación de los RadioButtons carnes
radio1 = tk.IntVar()
rbcarne = Radiobutton(ventana, text= "Carne",value=1, variable=radio1, bg="#ADD8E6")
rbpollo = Radiobutton(ventana, text= "Pollo guisado",value=2, variable=radio1, bg="#ADD8E6")
rblasagna = Radiobutton(ventana, text= "Lasaña",value=3, variable=radio1, bg="#ADD8E6")


#RadioButtons ensaladas
radio2 = tk.IntVar()
rbfresca = Radiobutton(ventana, text= "Fresca",value=1, variable=radio2, bg="#ADD8E6")
rbcoditos = Radiobutton(ventana, text= "Coditos",value=2, variable=radio2, bg="#ADD8E6")
rbrusa = Radiobutton(ventana, text= "Rusa",value=3, variable=radio2, bg="#ADD8E6")

#RadioButtons bebidas
radio3 = tk.IntVar()
rbgaseosa = Radiobutton(ventana, text= "Gaseosa",value=1, variable=radio3, bg="#ADD8E6")
rbfresco = Radiobutton(ventana, text= "Fresco",value=2, variable=radio3, bg="#ADD8E6")
rbcafe = Radiobutton(ventana, text= "Cafe",value=3, variable=radio3, bg="#ADD8E6")

btnImprimirFactura = Button(ventana, text="Imprimir Factura", command=calcular_precios)
btnImprimirFactura.config(bg="#87CEFA")

#carga de los elementos en la interfaz gráfica

lbName.place(x=200, y=30, width=200, height=30)
lbcarne.place(x=30, y=80, width=100, height=100)
lbpollo.place(x=160, y=80, width=100, height=100)
lblasagna.place(x=290, y=80,width=100, height=100)

##radiobuttons

rbcarne.place(x=30, y=190, width=100, height=30)
rbpollo.place(x=160, y=190, width=100, height=30)
rblasagna.place(x=290, y=190, width=100, height=30)


lbSecEnsalda.place(x=50, y=250,width=100, height=30)

lbfresca.place(x=30, y=300,width=100, height=100)
lbcoditos.place(x=160, y=300,width=100, height=100)
lbrusa.place(x=290, y=300,width=100, height=100)

##radiobuttons

rbfresca.place(x=30, y=410, width=100, height=30)
rbcoditos.place(x=160, y=410, width=100, height=30)
rbrusa.place(x=290, y=410, width=100, height=30)


lbsecBebidas.place(x=50, y=450,width=100, height=30)

lbgaseosa.place(x=30, y=500, width=100, height=100)
lbfresco.place(x=160, y=500,width=100, height=100)
lbcafe.place(x=290, y=500, width=100, height=100)

##radiobuttons

rbgaseosa.place(x=30, y=610, width=100, height=30)
rbfresco.place(x=160, y=610, width=100, height=30)
rbcafe.place(x=290, y=610, width=100, height=30)


btnImprimirFactura.place(x=420, y=550,width=100, height=40)

##############seccion de radiobuttons



ventana.mainloop()
