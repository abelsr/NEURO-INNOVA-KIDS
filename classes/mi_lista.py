from tkinter import *
from classes.mi_boton import *

class mi_lista(mi_boton):
    def __init__(self, canvas, x, y, texto, elementos,**kwargs):
        """Lista de opciones desplegable
        
        Parámetros:
        -----------
        canvas : tkinter.Canvas
            Canvas donde se dibujará la lista
        x : int
            Posición x del elemento
        y : int
            Posición y del elemento
        texto : str
            Texto que se mostrará el boton para despelgar la lista
        elementos : list
            Lista de elementos que se mostrarán
        """
        self.x = x
        self.y = y
        self.canvas = canvas
        self.frame = self.canvas.master
        self.texto = texto
        self.elementos = elementos
        self.controller = self.canvas.master.controller
        super().__init__(self.canvas, x, y, texto, 'rosa', 
                        command = lambda x: self.desplegar_list(),
                        grande = True, **kwargs)

    def desplegar_list(self):
        """Despliega la lista de elementos"""
        self.seleccion = None
        self.lista = Listbox(self.canvas.master, selectmode = 'single', width = len(max(self.elementos, key = len)),
                                font = ('Mukta Malar ExtraLight', int(self.canvas.master.controller.boton_tamanio * self.tamano_letra)),
                                selectbackground = '#f692ca', 
                                selectforeground = '#000000', 
                                borderwidth = 0, 
                                highlightthickness = 0, 
                                relief = 'flat', 
                                activestyle = 'none')
        self.current = -1
        self.lista.place(x = self.x, y = self.y, anchor = CENTER)
        for elemento in self.elementos:
            self.lista.insert(END, elemento)
        self.lista.bind('<ButtonRelease-1>', self.seleccionar_elemento)
        self.lista.bind('<Double-Button-1>', self.seleccionar_elemento)
        self.lista.bind('<Enter>',  self.hover_seleccion)
        self.lista.bind('<Motion>', self.hover_seleccion)
        self.lista.bind('<Leave>',  self.descolorear)
        self.canvas.bind('<Button-1>',  lambda x: self.ocultar_lista())

    def hover_seleccion(self, event):
        """Colorea el elemento seleccionado"""
        self.lista.selection_clear(0, END)
        self.lista.selection_set(self.lista.nearest(event.y))

    def descolorear(self, event = None):
        """Descolorea los elementos de la lista"""
        self.lista.selection_clear(0, END)

    def seleccionar_elemento(self, event):
        """Selecciona el elemento de la lista"""
        self.seleccion = str(self.lista.get(self.lista.curselection()))
        self.lista.destroy()
        self.lista = None
        self.canvas.itemconfig(self.texto_id, text = f'{self.texto.split(" ")[1].title()}: ' + self.seleccion.split(' ')[0].title())
    
    def ocultar_lista(self):
        """Oculta la lista de elementos"""
        if not self.seleccion:
            self.lista.destroy()
            self.lista = None
    
    def datos(self) -> str:
        """Devuelve los datos de la lista"""
        return self.seleccion
    
    def destroy(self):
        """Destruye la lista"""
        super().destroy()
        try:
            self.lista.destroy()
        except:
            pass