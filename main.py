import tkinter as tk, pyglet, time, os
from functools import partial
from PIL import Image as PImage, ImageTk as ImageTk
from tkinter import *
from PIL import ImageGrab
from pantallas.InformacionBasica.Seguidor_ocular import seguidor_ocular
from pantallas.Menu_principal import *
from pantallas.Informacion_basica import *
from pantallas.InformacionBasica.Que_es import *
from pantallas.InformacionBasica.Informacion_Pruebas import *
from pantallas.InformacionBasica.Seguidor_ocular import *
from pantallas.Inicio import *
from pantallas.Ingreso import *
from pantallas.Pruebas import *
from pantallas.Lista_Pruebas import *
from pantallas.Registro_1 import *
from pantallas.Splash import *
from pantallas.Instrucciones import *
from pantallas.Iniciar_sesion import *
from pantallas.Usuario import *
from pantallas.Historial import *
from pantallas.Entrevista import *
from pantallas.InformacionBasica.Resultados import *
from pantallas.EntrevistaEni.AntecedentesPrenatales import *
from pantallas.EntrevistaEni.AntecedentesNatales import *
from pantallas.EntrevistaEni.AntecedentesPostnatales import *
from pantallas.EntrevistaEni.ExploracionFisica import *
from pantallas.EntrevistaEni.HistoriaClinica import *
from pantallas.EntrevistaEni.HistoriaFamiliar import *
from pantallas.EntrevistaEni.Comportamiento import *
from pantallas.EntrevistaEni.MetodoDisciplina import *
from pantallas.EntrevistaEni.Escolaridad import *

# obtener resolucion de pantalla
resolution = ImageGrab.grab()
screenwidth, screenheight = resolution.size
del resolution

# obtenemos el directorio del programa
path = os.path.dirname(os.path.realpath(__file__))

# importamos la fuente a utilizar
pyglet.font.add_file(f'{path}/src/fonts/Mukta_Malar/MuktaMalar-ExtraLight.ttf')


class tkinterApp(tk.Tk):
    # función __init__ para la clase tkinterApp
    def __init__(self, *args, **kwargs):
        
        # función __init__ para la clase Tk
        tk.Tk.__init__(self, *args, **kwargs)
        print("CARGANDO")
        global tic
        tic = time.perf_counter()
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.withdraw()
        splash = Splash(self)
        
        # creando un contenedor
        self.container = tk.Frame(self) 
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        # inicializando frames en un arreglo vacío
        self.frames = {}
        
        # actualizamos el texto de la pantalla de carga
        splash.actualizar_texto(text_ = f'Cargando media')
        self.crear_media()
        self.id = 0
        splash.actualizar_texto(text_ = f'Cargando pantallas')
        self.comprobar_directorio_salida()
        
        # iterando a través de una lista que consta de los diferentes diseños de página
        frames = [menu_principal, inicio, ingreso, lista_pruebas, informacion_basica, que_es, info_pruebas, seguidor_ocular, registro1, registro2, instrucciones, iniciar_sesion, usuario_info, entrevista, pruebas, historial, resultados, historiaclinica, exploracionfisica, antecedentes_prenatales, antecedentes_prenatales2, antecedentes_prenatales3, antecedentes_prenatales4, historialfamiliar, historialfamiliar2, antecedentes_natales, antecedentes_natales2, antecedentes_postnatales, antecedentes_postnatales2, antecedentes_postnatales3, antecedentes_postnatales4, antecedentes_postnatales5, antecedentes_postnatales6, antecedentes_postnatales7, antecedentes_postnatales8, antecedentes_postnatales9, antecedentes_postnatales10, comportamiento, comportamiento2, comportamiento3, comportamiento4, comportamiento5, comportamiento6, comportamiento7, comportamiento8, comportamiento9, comportamiento10, comportamiento11, comportamiento12, disciplina, escolaridad, escolaridad2, escolaridad3, escolaridad4, escolaridad5, escolaridad6, escolaridad7, escolaridad8, escolaridad9, escolaridad10, escolaridad11, escolaridad12]

        for F in frames:
            frame = F(self.container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        # mostramos el frame del menu principal
        self.frame = self.frames[menu_principal]
        self.frame.tkraise()
        
        # actualizamos el texto en la pantal splash
        splash.actualizar_texto(text_ = f'Ya casi está listo')
        
        # colocar título de la ventana 
        self.title("NEURO INNOVA KIDS ®") 
        
        # colocar ícono
        self.iconphoto(False, PhotoImage(file = f'{path}/src/images/logo.png'))
        
        # mostrar programa en modo de pantalla completa
        self.wm_attributes('-fullscreen', 'True') 
        
        # cerrar la pantalla splash y eliminamos el objeto
        splash.destroy()
        del splash

    # inicialización de la matriz del historial de los frames
    back_frame = [menu_principal]
    
    # para mostrar el frame actual pasado como parámetro
    def mostrar_pantalla(self, current_frame, next_frame):
        self.back_frame.append(current_frame)
        self.frame = self.frames[next_frame]
        self.frame.tkraise()

    # para ir al frame anterior
    def previous_frame(self):
        for i in self.frames:
            if str(self.back_frame[-1]).split('!')[2] == str(i).split(".")[-1][:-2]:
                self.frame = self.frames[i]
                self.back_frame.pop()
                self.frame.tkraise()

    # para ir al menu principal
    def ir_menu_principal(self):
        self.back_frame = [menu_principal]
        self.frame = self.frames[menu_principal]
        self.frame.tkraise()
    
    # para ir a las instrucciones
    def ir_instrucciones(self, current_frame):
        self.mostrar_pantalla(current_frame, instrucciones)
        

    # función que llama a todas las imagenes para el programa
    def crear_media(self):
        # definimmos el tamaño de los botones
        self.boton_tamanio = int(screenheight * 0.018)
        
        # definimos el estilo de los botones
        self.estilo_rosa = {"borderwidth" : 0, 
                            "bg" : "#f6ddeb", 
                            "activebackground" : '#f692ca',
                            "fg" : 'black',
                            "highlightbackground" : "#f6ddeb",
                            "padx":0, 
                            "pady":0}
        self.estilo_verde = {"borderwidth" : 0, 
                            "bg" : "#e8eab9", 
                            "activebackground" : '#e2ea26',
                            "fg" : 'black',
                            "highlightbackground" : "#e8eab9",
                            "padx":0, 
                            "pady":0}
        self.size = {'width':screenwidth, 'height':screenheight}
        self.geometry(f'{screenwidth}x{screenheight}')
        
        # creacion de imagenes para el programa
        self.background = self.imagen_redimensionar(f"{path}/src/images/background.jpg", es_fondo = True)
        self.loguito = self.imagen_redimensionar(f"{path}/src/images/logo.png", ratio = 0.00002)
        self.logo = self.imagen_redimensionar(f"{path}/src/images/logo.png", ratio = 0.00007)
        self.boton_rosa_hover = self.imagen_redimensionar(f"{path}/src/images/image.png", ratio = 0.00035)
        self.boton_rosa = self.imagen_redimensionar(f"{path}/src/images/Boton rosa 12.png", ratio = 0.00035)
        self.boton_rosa_grande = self.imagen_redimensionar(f"{path}/src/images/Boton rosa 12.png", ratio = 0.0005)
        self.boton_rosa__hover_grande = self.imagen_redimensionar(f"{path}/src/images/image.png", ratio = 0.0005)
        self.back_ninios = self.imagen_redimensionar(f"{path}/src/images/fondo_ninios1.png", es_fondo = True)
        self.signo_iterrogacion_grande = self.imagen_redimensionar(f"{path}/src/images/Signo_de_interrogación.png", ratio = 0.0003)
        self.signo_iterrogacion = self.imagen_redimensionar(f"{path}/src/images/Signo_de_interrogación.png", ratio = 0.000075)
        self.signo_iterrogacion_chico = self.imagen_redimensionar(f"{path}/src/images/Signo_de_interrogación.png", ratio = 0.00006)
        self.logo_bn = self.imagen_redimensionar(f"{path}/src/images/Logo B Y N.png", ratio = 0.000075)
        self.registro_icono = self.imagen_redimensionar(f"{path}/src/images/Usuarios.png", ratio = 0.00007)
        self.registro_icono_grande = self.imagen_redimensionar(f"{path}/src/images/Usuarios.png", ratio = 0.00018)
        self.play_icono = self.imagen_redimensionar(f"{path}/src/images/Play.png", ratio = 0.00007)
        self.play_icono_grande = self.imagen_redimensionar(f"{path}/src/images/Play.png", ratio = 0.0003)
        self.boton_verde = self.imagen_redimensionar(f"{path}/src/images/boton_verde.png", ratio = 0.00035)
        self.boton_verde_hover = self.imagen_redimensionar(f"{path}/src/images/verde_hover.png", ratio = 0.00035)
        self.historial_icono = self.imagen_redimensionar(f"{path}/src/images/Historial.png", ratio = 0.00007)
        self.historial_icono_grande = self.imagen_redimensionar(f"{path}/src/images/Historial.png", ratio = 0.0003)
        self.barra_escribir = self.imagen_redimensionar(f"{path}/src/images/barra_escribir1.png", ratio = 0.000525)
        self.barra_seleccion = self.imagen_redimensionar(f"{path}/src/images/barra_seleccion.png", ratio = 0.000125)
        self.barra_seleccion_rellena = self.imagen_redimensionar(f"{path}/src/images/barra_seleccion_rellena.png", ratio = 0.000125)
        self.fondo_splash = self.imagen_redimensionar(f"{path}/src/images/background.jpg", ratio = 0.000125)
        self.eyetracker_img = self.imagen_redimensionar(f"{path}/src/images/eyetracker.jpg", ratio = 0.00035)
        self.figuras_img = self.imagen_redimensionar(f"{path}/src/images/figuras_prueba.png", ratio = 0.00035)
        self.cubos_img = self.imagen_redimensionar(f"{path}/src/images/cubos_prueba.png", ratio = 0.00035)
        self.domino_img = self.imagen_redimensionar(f"{path}/src/images/domino_prueba.png", ratio = 0.00035)
        # self.gifs = self.gif_imagenes("mygif.gif",1)
        self.gif_instruccion1_a = self.gif_imagenes(f"{path}/src/images/instruccion1_a", 0.0002)
        self.gif_instruccion1_b = self.gif_imagenes(f"{path}/src/images/instruccion1_b", 0.000177)
        # self.gif_instruccion2_a = self.gif_imagenes(f"{path}/src/images/instruccion2_a", 0.000177)
        self.gif_instruccion2_b = self.gif_imagenes(f"{path}/src/images/instruccion2_b", 0.0002)
        # self.gif_instruccion3_a = self.gif_imagenes(f"{path}/src/images/instruccion3_a", 0.0002)
        self.gif_instruccion3_b = self.gif_imagenes(f"{path}/src/images/instruccion3_b", 0.0002)

    # Funcion para pasar las imagenes de los gifs
    def gif_imagenes(self, path, ratio) -> list:
        lista = os.listdir(path)
        images = []
        for i in range(len(lista)):
            if i%2 == 0:
                imagen = self.imagen_redimensionar(path + '/' + lista[i], ratio)
                images.append(imagen)
        return images
        

    # función para redimensionar las imagenes
    def imagen_redimensionar(self, path: str, ratio: float = 1, es_fondo: bool = None) -> Image:
        imagen = PImage.open(path)
        imagen = imagen.convert('RGBA')
        if es_fondo:
            imagen = imagen.resize((screenwidth, screenheight), PImage.ANTIALIAS)
        else:
            imagen_ancho, imagen_alto = imagen.size
            imagen = imagen.resize((int(imagen_ancho*screenwidth*ratio), int(imagen_alto*screenwidth*ratio)), PImage.ANTIALIAS)
        return ImageTk.PhotoImage(imagen)

    # función para animar los botones
    def animacion_boton(self, button, canvas, tag, color = "rosa", tamaño = None):
        if color == "rosa":
            hightbg_hover = "#f692ca"
            hightbg_normal = "#f6ddeb"
            if tamaño == "grande":
                image_hover = self.boton_rosa__hover_grande
                image_normal = self.boton_rosa_grande
            else:
                image_hover = self.boton_rosa_hover
                image_normal = self.boton_rosa
        elif color == "verde":
            hightbg_hover = "#e2ea26"
            hightbg_normal = "#e8eab9"
            image_hover = self.boton_verde_hover
            image_normal = self.boton_verde
            
        def on_enter(e):
            button.config(highlightbackground = hightbg_hover, background = hightbg_hover, fg = 'white')
            canvas.itemconfig(tag, image = image_hover)

        def on_leave(e):
            button.config(highlightbackground = hightbg_normal,  background = hightbg_normal, fg = 'black')
            canvas.itemconfig(tag, image = image_normal)

        def on_click(e):
            button.config( fg = 'white')
            
        def on_unclick(e):
            button.config( fg = 'black')
        
        def on_enter_canvas(e):
            button.config(highlightbackground = hightbg_hover, background = hightbg_hover)
            canvas.itemconfig(tag, image = image_hover)

        def on_leave_canvas(e):
            button.config(highlightbackground = hightbg_normal, background = hightbg_normal)
            canvas.itemconfig(tag, image = image_normal)
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.bind("<Button-1>", on_click)
        button.bind("<ButtonRelease-1>", on_unclick)
        canvas.tag_bind(tag, '<Enter>', on_enter_canvas)
        canvas.tag_bind(tag, "<Leave>", on_leave_canvas)
    
    def comprobar_formularios(self, datos, canvas):
        print(datos)
        for item in datos.values():
            if item == "":
                texto_error = canvas.create_text(int(screenwidth*0.65),int(screenheight*0.25), 
                            text = "Por favor, responde cada formulario",
                            font = ('Mukta Malar ExtraLight', int(self.boton_tamanio)),
                            anchor = CENTER)
                self.after(3000,lambda: canvas.delete(texto_error))
                return False
        return True
    
    def comprobar_directorio_salida(self, id_paciente = None):
        import os, ctypes.wintypes
        CSIDL_PERSONAL = 5       
        SHGFP_TYPE_CURRENT = 0   

        dir = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, dir)

        docs = str(dir.value)
        self.docs = str(dir.value)
        directory = docs + "\\NEURO INNOVA KIDS"

        if not os.path.exists(directory):
            os.makedirs(directory)
            
        if not os.path.exists(directory + "\\PACIENTES"):
            os.makedirs(directory + "\\PACIENTES")
            
        if id_paciente:
            if not os.path.exists(directory + "\\PACIENTES" + f"\\{id_paciente}"):
                os.makedirs(directory + "\\PACIENTES" + f"\\{id_paciente}")

if __name__ == "__main__":
    app = tkinterApp()
    app.deiconify()
    toc = time.perf_counter()
    print("LISTO")
    print(f'La carga del programa tomó {str(int(toc-tic)).strip()}s')
    del tic, toc
    app.mainloop()