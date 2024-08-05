from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2
import Proyecto.login as login


class Register:
    def __init__(self, ventana_registro):
        self.window = ventana_registro
        self.window.title("REGISTRARSE AL SISTEMA")
        self.window.geometry("1020x630+245+110")
        self.window.resizable(0, 0)

        frame_division = Frame(self.window, 
                            width=2, 
                            bd=1, 
                            relief=SUNKEN)
        frame_division.grid(row=0, 
                            column=1, 
                            sticky='ns')
        frame_izquierdo = Frame(self.window, 
                                bg='#B7DEF1', 
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
                            bg='#B7DEF1')
        label_imagen.image = render
        label_imagen.pack(pady=5)
        # Información
        info_text = '''Dirección: Av. Micaela Bastidas 634\n          Celular: +51 928 097 889\nEmail: cevicheria.delmar@gmail.com\n            Huánuco - Amarilis'''
        label_info = Label(frame_izquierdo, 
                        text=info_text, 
                        font=('Comic Sans', 12), 
                        bg="#B7DEF1", 
                        fg='black', 
                        justify=LEFT)
        label_info.pack()
        # Frame derecho para el formulario de inicio de sesión
        frame_derecho = Frame(self.window, 
                            padx=20, 
                            pady=20, 
                            bg='#99B6C4')
        frame_derecho.grid(row=0, 
                        column=2, 
                        sticky='nsew')
        # Título
        titulo = Label(frame_derecho, 
                    text='REGISTRO', 
                    fg='black', 
                    font=('Comic Sans', 20, 'bold'), 
                    pady=10, 
                    bg='#99B6C4')
        titulo.grid(row=0, 
                    column=0, 
                    columnspan=2, 
                    pady=10)

        # Etiquetas y campos de entrada
        label_correo = Label(frame_derecho, 
                            text="Email: ", 
                            font=("Comic Sans", 15, "bold"), 
                            bg='#99B6C4')
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
                                bg='#99B6C4')
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
        label_nombre = Label(frame_derecho, 
                                text="Nombre: ", 
                                font=("Comic Sans", 15, "bold"), 
                                bg='#99B6C4')
        label_nombre.grid(row=3, 
                            column=0, 
                            sticky='e', 
                            padx=10, 
                            pady=10)
        
        self.name = Entry(frame_derecho, 
                            width=35,
                            font=("Comic Sans", 12))
        self.name.grid(row=3, 
                        column=1, 
                        padx=10, 
                        pady=10,
                        ipady=5)
        btn_register = Button(frame_derecho, 
                        text="Registrarse", 
                        font=("Comic Sans", 12, "bold"), 
                        bg='#DDDDDD', 
                        fg='black', 
                        command=self.registrarse)
        btn_register.grid(row=4, 
                    column=0, 
                    columnspan=2, 
                    pady=10)
        btn_volver = Button(frame_derecho, 
                            text="Volver",
                            font=("Comic Sans", 12, "bold"),
                            bg='#DDDDDD', 
                            fg='black',
                            command=self.volver)
        btn_volver.grid(row=5,
                        column=0,
                        columnspan=2,
                        pady=10)
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
            return None

    def validar_registrarse(self, correo, password, name):
        conexion = self.conectar_postgres()

        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "INSERT INTO login (email, password, name) VALUES (%s, %s, %s)"
                datos = (correo, password, name)
                cursor.execute(sql, datos)
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
            except psycopg2.Error as e:
                messagebox.showerror("Error de consulta", f"No se pudo ejecutar la consulta: {e}")
                return False

    def registrarse(self):
        email = self.correo.get()
        password = self.password.get()
        name = self.name.get()

        if email and password and name:
            resultado = self.validar_registrarse(email, password, name)
            if resultado:
                messagebox.showinfo("Bienvenido", "Gracias por registrarse")
            else:
                messagebox.showerror("Error de registro", "Email ya existe")
        else:
            messagebox.showerror("Error de registro", "Ingrese email, contraseña y su nombre")

    def volver(self):
        self.window.destroy()
        ventana_login = Tk()
        login_app = login.LoginApp(ventana_login)
        ventana_login.mainloop()


ventana_registro = Tk()
app = Register(ventana_registro)
ventana_registro.mainloop()
