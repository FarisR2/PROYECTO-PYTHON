from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

class MainApp:
    def __init__(self):
        precios_comida = [14, 16, 19, 20, 22, 23, 18, 14]
        precios_bebidas = [4.5, 4.5, 3, 8, 3, 3, 3]

        def click_boton(numero):
            global operador
            operador = operador + numero
            visor_calculadora.delete(0, END)
            visor_calculadora.insert(END, operador)

        def borrar():
            global operador
            operador = ''
            visor_calculadora.delete(0, END)

        def obtener_resultado():
            global operador
            resultado = str(eval(operador))
            visor_calculadora.delete(0, END)
            visor_calculadora.insert(0, resultado)
            operador = ''

        def revisar_check():
            x = 0
            for c in cuadros_comida:
                if variables_comida[x].get() == 1:
                    cuadros_comida[x].config(state=NORMAL)
                    if cuadros_comida[x].get() == 0:
                        cuadros_comida[x].delete(0, END)
                    cuadros_comida[x].focus()
                else:
                    cuadros_comida[x].config(state=DISABLED)
                    texto_comida[x].set('0')
                x+=1

            x = 0    
            for c in cuadro_bebida:
                if variables_bebida[x].get() == 1:
                    cuadro_bebida[x].config(state=NORMAL)
                    if cuadro_bebida[x].get == 0:
                        cuadro_bebida[x].delete(0, END)
                    cuadro_bebida[x].focus()
                else:
                    cuadro_bebida[x].config(state=DISABLED)
                    texto_bebida[x].set('0')
                x+=1

        def total():
            sub_total_comida = 0
            p = 0
            for cantidad in texto_comida:
                sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
            p += 1
            print(sub_total_comida)

            sub_total_bebida = 0
            p = 0
            for cantidad in texto_bebida:
                sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebidas[p])
            p += 1
            print(sub_total_bebida)

            sub_total = sub_total_comida + sub_total_bebida
            impuestos = sub_total * 0.08
            total = impuestos + sub_total

            var_costo_comida.set(f'S/. {round(sub_total_comida, 2)}')
            var_costo_bebida.set(f'S/. {round(sub_total_bebida, 2)}')
            var_costo_subtotal.set(f'S/. {round(sub_total, 2)}')
            var_costo_impuestos.set(f'S/. {round(impuestos, 2)}')
            var_costo_total.set(f'S/. {round(total, 2)}')

        def recibo():
            texto_recibo.delete(1.0, END)
            num_recibo = f'N# - {random.randint(1000, 9999)}'
            fecha = datetime.datetime.now()
            fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}:{fecha.second}'
            texto_recibo.insert(END, f'CEVICHERIA - RESTAURANTES PERUANOS S.A\n')
            texto_recibo.insert(END, f'''          Av. Tito Jaime 285 P-2 Tingo María\n''')
            texto_recibo.insert(END, f'''                  Tingo María - Rupa Rupa\n''')
            texto_recibo.insert(END, f'''           BOLETA DE VENTA ELECTRONICA\n''')
            texto_recibo.insert(END, f'Datos: \t{num_recibo}\t\t{fecha_recibo}\n')
            texto_recibo.insert(END, f'-' * 66 + '\n')
            texto_recibo.insert(END, f'Items\t\tCant.\tCosto Items\n')
            texto_recibo.insert(END, f'-' * 66 + '\n')

            x = 0
            for comida in texto_comida:
                if comida.get() != '0':
                    texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\tS/. {int(comida.get()) * precios_comida[x]}\n')
                x+=1

            x = 0
            for bebida in texto_bebida:
                if bebida.get() != '0':
                    texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\tS/. {int(bebida.get()) * precios_bebidas[x]}\n')
                x+=1

            texto_recibo.insert(END, f'-' * 66 + '\n')
            texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
            texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
            texto_recibo.insert(END, f'-' * 66 + '\n')
            texto_recibo.insert(END, f' Sub-Total: \t\t\t{var_costo_subtotal.get()}\n')
            texto_recibo.insert(END, f' Impuestos: \t\t\t{var_costo_impuestos.get()}\n')
            texto_recibo.insert(END, f' Total: \t\t\t{var_costo_total.get()}\n')
            texto_recibo.insert(END, f'-' * 66 + '\n')
            texto_recibo.insert(END, f'''                    ¡Gracias por su pago! ''')
        def guardar():
            info_recibo = texto_recibo.get(1.0, END)
            archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
            archivo.write(info_recibo)
            archivo.close()

            messagebox.showinfo('Informacion', 'El recibo se ha guardado')
        def resetear():
            texto_recibo.delete(0.1, END)

            for texto in texto_comida:
                texto.set('0')
            for texto in texto_bebida:
                texto.set('0')

            for cuadro in cuadros_comida:
                cuadro.config(state=DISABLED)
            for cuadro in cuadro_bebida:
                cuadro.config(state=DISABLED)

            for v in variables_comida:
                v.set('0')
            for v in variables_bebida:
                v.set('0')

            var_costo_comida.set('0')
            var_costo_bebida.set('0')
            var_costo_subtotal.set('0')
            var_costo_impuestos.set('0')
            var_costo_total.set('0')

        # Iniciar tkinter
        aplicacion = Tk()

        # Tamaño de la ventana
        aplicacion.geometry('1020x630+245+110')

        # Evitar maximizar
        aplicacion.resizable(0, 0)

        # Titulo
        aplicacion.title('Mi Restaurante - Sistema de facturación')

        # Color de fondo de ventana
        aplicacion.config(bg="#1799D2")

        # Panel superior
        panel_superior = Frame(aplicacion, 
                            bd=1, 
                            relief=FLAT)

        panel_superior.pack(side=TOP)

        # Etiqueta titulo
        etiqueta_titulo = Label(panel_superior, 
                                text='Sistema de Facturación', 
                                fg='#1799D2',
                                font=('Acme-Regular.ttf', 50), 
                                bg='#05415B', 
                                width=27,)

        etiqueta_titulo.grid(row=0, 
                            column=0)

        # Panel izquierdo
        panel_izquierdo = Frame(aplicacion, 
                                bd=1, 
                                relief=FLAT)
        panel_izquierdo.pack(side=LEFT)

        # Panel costos
        panel_costos = Frame(panel_izquierdo, 
                            bd=1, 
                            relief=FLAT,
                            bg='#1799D2')
        panel_costos.pack(side=BOTTOM)

        # Panel comidas
        panel_comidas = LabelFrame(panel_izquierdo, 
                                text='Comida', 
                                font=('Acme-Regular.ttf', 19, 'bold'),
                                bd=1, 
                                relief=FLAT, 
                                fg='#1799D2', 
                                padx=10, 
                                pady=10)

        panel_comidas.pack(side=LEFT, 
                        padx=10, pady=10)
        panel_comidas.config(width=250, 
                        height=400)  # Establecer un tamaño fijo adecuado para el panel de comidas

        panel_comidas.grid_propagate(False)  # Evitar que el tamaño del panel cambie automáticamente

        # Panel bebidas
        panel_bebidas = LabelFrame(panel_izquierdo, 
                                text='Bebidas', 
                                font=('Acme-Regular.ttf', 19, 'bold'),
                                bd=1, 
                                relief=FLAT, 
                                fg='#1799D2', 
                                padx=10, 
                                pady=10)

        panel_bebidas.pack(side=LEFT, 
                        padx=10, 
                        pady=10)

        panel_bebidas.config(width=250, 
                            height=400)  # Establecer un tamaño fijo adecuado para el panel de bebidas

        panel_bebidas.grid_propagate(False)  # Evitar que el tamaño del panel cambie automáticamente


        # Panel derecha
        panel_derecha = Frame(aplicacion, 
                            bd=1, 
                            relief=FLAT)
        panel_derecha.pack(side=RIGHT)

        # Panel calculadora
        panel_calculadora = Frame(panel_derecha, 
                                bd=1, 
                                relief=FLAT, 
                                bg="#1799D2")
        panel_calculadora.pack()

        # Panel recibo
        panel_recibo = Frame(panel_derecha, 
                            bd=1, 
                            relief=FLAT, 
                            bg="#1799D2")
        panel_recibo.pack()

        # Panel botones
        panel_botones = Frame(panel_derecha, 
                            bd=1, 
                            relief=FLAT, 
                            bg="#1799D2")
        panel_botones.pack()

        # Lista Comidas
        lista_comidas = ['Ceviche', 'Ceviche Mixto', 'Arroz Chaufa de Mariscos', 'Arroz con Mariscos', 'Jalea Mixta', 'Causa de Ceviche', 'Chicharron de Pota']
        lista_bebidas = ['InkaCola', 'CocaCola', 'Pepsi', 'Cerveza Cristal', 'Chicha Morada', 'Chicha Maracúya', 'Limonada']

        # Variables y Checkbuttons para comidas
        variables_comida = []
        cuadros_comida = []
        texto_comida = []
        contador = 0
        for comida in lista_comidas:
            # crear checkbutton
            variables_comida.append('')
            variables_comida[contador] = IntVar()
            comida = Checkbutton(panel_comidas,
                                text=comida.title(), 
                                font=('Acme-Regular.ttf', 10, 'bold'), 
                                onvalue=1,
                                offvalue=0, 
                                variable=variables_comida[contador],
                                command=revisar_check)
            comida.grid(row=contador, 
                        column=0,
                        sticky=W)
            # Crear cuadros comida
            cuadros_comida.append('')
            texto_comida.append('')
            texto_comida[contador] = StringVar()
            texto_comida[contador].set(0)
            cuadros_comida[contador] = Entry(panel_comidas,
                                            font=('Acme-Regular.ttf,', 9, 'bold'),
                                            bd=1,
                                            width=6,
                                            state=DISABLED,
                                            textvariable=texto_comida[contador]
                                            )
            cuadros_comida[contador].grid(row=contador,
                                        column=1)

            contador += 1

        # Variables y Checkbuttons para bebidas
        variables_bebida = []
        cuadro_bebida = []
        texto_bebida = []

        contador = 0
        for bebida in lista_bebidas:
            variables_bebida.append('')
            variables_bebida[contador] = IntVar()
            bebida = Checkbutton(panel_bebidas, 
                                text=bebida.title(), 
                                font=('Acme-Regular.ttf', 10, 'bold'),
                                onvalue=1, 
                                offvalue=0, 
                                variable=variables_bebida[contador],
                                command=revisar_check)
            bebida.grid(row=contador, 
                        column=0, 
                        sticky=W)   
            
            cuadro_bebida.append('')
            texto_bebida.append('')
            texto_bebida[contador] = StringVar()
            texto_bebida[contador].set(0)
            cuadro_bebida[contador] = Entry(panel_bebidas,
                                            font=('Acme-Regular.ttf', 10, 'bold'),
                                            bd=1,
                                            width=6,
                                            state=DISABLED,
                                            textvariable=texto_bebida[contador])
            cuadro_bebida[contador].grid(row=contador, 
                                        column=1)


            contador += 1

        # Variables
        var_costo_comida = StringVar()
        var_costo_bebida = StringVar()
        var_costo_subtotal = StringVar()
        var_costo_total = StringVar()
        var_costo_impuestos = StringVar()


        etiqueta_costo_comida = Label(panel_costos,
                                    text="Costo Comida",
                                    font=('Acme-Regular.ttf', 12, 'bold'),
                                    bg='#1799D2',
                                    fg='white')

        etiqueta_costo_comida.grid(row=0, column=0)

        # Comida
        texto_costo_comida = Entry(panel_costos,
                                font=('Acme-Regular.ttf', 12, 'bold'),
                                bd=1,
                                width=10,
                                state='readonly',
                                textvariable=var_costo_comida)

        texto_costo_comida.grid(row=0, column=1, padx=10)

        etiqueta_costo_bebida = Label(panel_costos,
                                    text="Costo Bebida",
                                    font=('Acme-Regular.ttf', 12, 'bold'),
                                    bg='#1799D2',
                                    fg='white')

        etiqueta_costo_bebida.grid(row=1, column=0)

        # Bebida
        texto_costo_bebida = Entry(panel_costos,
                                font=('Acme-Regular.ttf', 12, 'bold'),
                                bd=1,
                                width=10,
                                state='readonly',
                                textvariable=var_costo_bebida)

        texto_costo_bebida.grid(row=1, column=1)

        # Subtotal
        etiqueta_costo_subtotal = Label(panel_costos,
                                    text="Subtotal",
                                    font=('Acme-Regular.ttf', 12, 'bold'),
                                    bg='#1799D2',
                                    fg='white')

        etiqueta_costo_subtotal.grid(row=0, column=2)

        texto_costo_subtotal = Entry(panel_costos,
                                font=('Acme-Regular.ttf', 12, 'bold'),
                                bd=1,
                                width=10,
                                state='readonly',
                                textvariable=var_costo_subtotal)

        texto_costo_subtotal.grid(row=0, column=3, padx=10)


        etiqueta_costo_subtotal = Label(panel_costos,
                                    text="Subtotal",
                                    font=('Acme-Regular.ttf', 12, 'bold'),
                                    bg='#1799D2',
                                    fg='white')

        # Impuestos

        etiqueta_costo_impuesto = Label(panel_costos,
                                    text="Impuestos",
                                    font=('Acme-Regular.ttf', 12, 'bold'),
                                    bg='#1799D2',
                                    fg='white')

        etiqueta_costo_impuesto.grid(row=1, column=2)

        texto_costo_impuesto = Entry(panel_costos,
                                font=('Acme-Regular.ttf', 12, 'bold'),
                                bd=1,
                                width=10,
                                state='readonly',
                                textvariable=var_costo_impuestos)

        texto_costo_impuesto.grid(row=1, column=3, padx=10)


        etiqueta_costo_impuesto = Label(panel_costos,
                                    text="Impuestos",
                                    font=('Acme-Regular.ttf', 12, 'bold'),
                                    bg='#1799D2',
                                    fg='white')



        # Total
        etiqueta_costo_total = Label(panel_costos,
                                    text="Total",
                                    font=('Acme-Regular.ttf', 12, 'bold'),
                                    bg='#1799D2',
                                    fg='white')

        etiqueta_costo_total.grid(row=2, column=2)

        texto_costo_total = Entry(panel_costos,
                                font=('Acme-Regular.ttf', 12, 'bold'),
                                bd=1,
                                width=10,
                                state='readonly',
                                textvariable=var_costo_total)

        texto_costo_total.grid(row=2, column=3, padx=10)

        # Botones

        botones = ['total', 'recibo', 'guardar', 'resetear']
        botones_creados = []
        columnas = 0

        for boton in botones:
            boton = Button(panel_botones,
                        text=boton.title(),
                        font=('Acme-Regular', 14, 'bold'),
                        fg='white',
                        bg='#1799D2',
                        bd=1,
                        width=9)
            
            botones_creados.append(boton)
            
            boton.grid(row=0, 
                    column=columnas)
            columnas += 1

        botones_creados[0].config(command=total)
        botones_creados[1].config(command=recibo)
        botones_creados[2].config(command=guardar)
        botones_creados[3].config(command=resetear)
            
        # area de recibo
        texto_recibo = Text(panel_recibo,
                            font=('Acme-Regular.ttf', 15, 'bold'),
                            bd=1,
                            width=42,
                            height=10)

        texto_recibo.grid(row=0, 
                        column=0)

        # calculadora

        visor_calculadora = Entry(panel_calculadora,
                                font=('Acme-Regular.ttf', 19, 'bold'),
                                width=33,
                                bd=1)

# POINT RESTAURANT

        visor_calculadora.grid(row=0, 
                            column=0,    
                            columnspan=4)
        botones_calculadora = ['7','8','9','+', 
                            '4', '5', '6', '-',
                            '1', '2', '3', 'x',
                            'CE', 'B', '0', '/']

        botones_guardados = []

        fila = 1
        columna = 0

        for boton in botones_calculadora:
            boton = Button(panel_calculadora,
                        text=boton.title(),
                        font=('Acme-Regular', 16, 'bold'),
                        fg='white',
                        bg='#1799D2',
                        bd=1,
                        width=8)
            
            botones_guardados.append(boton)

            boton.grid(row=fila, 
                    column=columna)
            if columna == 3:
                fila += 1
            columna += 1

            if columna == 4:
                columna = 0
            
        botones_guardados[0].config(command=lambda : click_boton('7'))
        botones_guardados[1].config(command=lambda : click_boton('8'))
        botones_guardados[2].config(command=lambda : click_boton('9'))
        botones_guardados[3].config(command=lambda : click_boton('+'))
        botones_guardados[4].config(command=lambda : click_boton('4'))
        botones_guardados[5].config(command=lambda : click_boton('5'))
        botones_guardados[6].config(command=lambda : click_boton('6'))
        botones_guardados[7].config(command=lambda : click_boton('-'))
        botones_guardados[8].config(command=lambda : click_boton('1'))
        botones_guardados[9].config(command=lambda : click_boton('2'))
        botones_guardados[10].config(command=lambda : click_boton('3'))
        botones_guardados[11].config(command=lambda : click_boton('*'))
        botones_guardados[12].config(command=obtener_resultado)
        botones_guardados[13].config(command=borrar)
        botones_guardados[14].config(command=lambda : click_boton('0'))
        botones_guardados[15].config(command=lambda : click_boton('/'))

        # Evitar que la pantalla se cierre
        aplicacion.mainloop()

if __name__ == "__main__":
    app = MainApp()