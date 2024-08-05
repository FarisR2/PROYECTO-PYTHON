from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2
import Proyecto.mi_restaurante as mi_restaurante  # SELECT * FROM login
import Proyecto.registro as registro

class LoginApp:

    def __init__(self, ventana_login):
        self.window = ventana_login
        self.window.title("INGRESAR AL SISTEMA")
        self.window.geometry("1020x630+245+110")
        self.window.resizable(0, 0)

        # Frame para la división
        frame_division = Frame(self.window, 
                            width=2, 
                            bd=1, 
                            relief=SUNKEN)
        frame_division.grid(row=0, 
                            column=1, 
                            sticky='ns')

        # Frame izquierdo para la imagen y la información
        frame_izquierdo = Frame(self.window, 
                                bg='#DDDDDD', 
                                padx=20, 
                                pady=20)
        frame_izquierdo.grid(row=0, 
                            column=0, 
                            sticky='nsew')

        # Cargar y mostrar la imagen
        imagen_login = Image.open("img.png")
        nueva_imagen = imagen_login.resize((350, 350))
        render = ImageTk.PhotoImage(nueva_imagen)

        label_imagen = Label(frame_izquierdo, 
                            image=render, 
                            bg='#DDDDDD')
        label_imagen.image = render
        label_imagen.pack(pady=5)

        # Información
        info_text = '''Dirección: Av. Micaela Bastidas 634\n          Celular: +51 928 097 889\nEmail: cevicheria.delmar@gmail.com\n            Huánuco - Amarilis'''
        label_info = Label(frame_izquierdo, 
                        text=info_text, 
                        font=('Comic Sans', 12), 
                        bg="#DDDDDD", 
                        fg='black', 
                        justify=LEFT)
        label_info.pack()

        # Frame derecho para el formulario de inicio de sesión
        frame_derecho = Frame(self.window, 
                            padx=20, 
                            pady=20, 
                            bg='#BDD0D9')
        frame_derecho.grid(row=0, 
                        column=2, 
                        sticky='nsew')

        # Título
        titulo = Label(frame_derecho, 
                    text='INICIAR SESIÓN', 
                    fg='black', 
                    font=('Comic Sans', 20, 'bold'), 
                    pady=10, 
                    bg='#BDD0D9')
        titulo.grid(row=0, 
                    column=0, 
                    columnspan=2, 
                    pady=10)

        # Etiquetas y campos de entrada
        label_correo = Label(frame_derecho, 
                            text="Email: ", 
                            font=("Comic Sans", 15, "bold"), 
                            bg='#BDD0D9')
        label_correo.grid(row=1, 
                        column=0, 
                        sticky='e', 
                        padx=10, 
                        pady=10)
        
        self.correo = Entry(frame_derecho, 
                            width=35,
                            font=("Comic Sans", 12))
        self.correo.grid(row=1, 
                        column=1, 
                        padx=10, 
                        pady=10,
                        ipady=5)

        label_contraseña = Label(frame_derecho, 
                                text="Contraseña: ", 
                                font=("Comic Sans", 15, "bold"), 
                                bg='#BDD0D9')
        label_contraseña.grid(row=2, 
                            column=0, 
                            sticky='e', 
                            padx=10, 
                            pady=10)
        
        self.password = Entry(frame_derecho, 
                            width=35, 
                            show="*",
                            font=("Comic Sans", 12))
        self.password.grid(row=2, 
                        column=1, 
                        padx=10, 
                        pady=10,
                        ipady=5)

        # Botón de inicio de sesión
        btn_login = Button(frame_derecho, 
                        text="Iniciar Sesión", 
                        font=("Comic Sans", 12, "bold"), 
                        bg='#DDDDDD', 
                        fg='black', 
                        command=self.iniciar_sesion)
        btn_login.grid(row=3, 
                    column=0, 
                    columnspan=2, 
                    pady=10)

        btn_register = Button(frame_derecho, 
                            text="Registrarse",
                            font=("Comic-Sans", 12, "bold"),
                            bg='#DDDDDD', 
                            fg='black',
                            command=self.registrarse)
        btn_register.grid(row=4,
                        column=0,
                        columnspan=2,
                        pady=10)

        # Ajuste de columnas y filas para que se expandan correctamente
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

    def conectar_postgres(self):
        try:
            conexion = psycopg2.connect(user='postgres',
                                        password='jorge_22d3',
                                        host='127.0.0.1',
                                        port='5432',
                                        database='db_login')
            return conexion    
        except psycopg2.Error as e:
            messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")

    def registrarse(self):
        self.window.destroy()
        ventana_registrar = Tk()
        registro = registro.Register(ventana_registrar)
        registro.mainloop()

    def validar_login(self, correo, password):
        conexion = self.conectar_postgres()

        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "SELECT * FROM login WHERE email = %s AND password = %s"
                datos = (correo, password)
                cursor.execute(sql, datos)
                validacion = cursor.fetchone()
                cursor.close()
                conexion.close()
                return validacion
            except psycopg2.Error as e:
                messagebox.showerror("Error de consulta", f"No se pudo ejecutar la consulta: {e}")
                return None

    def iniciar_sesion(self):
        email = self.correo.get()
        password = self.password.get()

        if email and password:
            resultado = self.validar_login(email, password)
            if resultado:
                messagebox.showinfo("Bienvenido", "Inicio de sesión exitoso")
                self.window.destroy()  # Cerrar la ventana de inicio de sesión
                mainApp = mi_restaurante.MainApp()  # Lanzar tu aplicación principal
                mainApp.mainloop()
            else:
                messagebox.showerror("Error de inicio de sesión", "Email o contraseña incorrectos")
        else:
            messagebox.showerror("Error de inicio de sesión", "Ingrese email y contraseña")

# Crear la ventana principal y la aplicación de inicio de sesión
ventana_login = Tk()
app = LoginApp(ventana_login)
ventana_login.mainloop()
