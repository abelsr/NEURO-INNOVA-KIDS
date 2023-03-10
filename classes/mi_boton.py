from tkinter import *
from main import *

class mi_boton():
    
    def __init__(self, canvas, x, y, texto, color_boton, command, **kwargs):
        """Botón
        
        Parametros:
        -----------
        canvas: Canvas
            Canvas donde se dibujará el botón
        x: int
            Posición x del botón
        y: int
            Posición y del botón
        texto: str
            Texto que tendrá el botón
        color_boton: str
            Color del botón (rosa o verde)
        command: function
            Función que se ejecutará al presionar el botón
            
        Parámetros opcionales:
        ---------
        icono: PhotoImage
            Icono que tendrá el botón
        icono_dentro: bool
            Si el icono estará dentro del botón o fuera
        grande: bool
            Si el botón será grande o no
        tamano_letra: float
            Tamaño de la letra del botón"""
        self.canvas = canvas
        self.alto = self.canvas.master.alto
        self.ancho = self.canvas.master.ancho
        self.x = x * self.ancho
        self.y = y * self.alto
        self.texto = texto
        self.command = command
        self.color_boton = color_boton
        self.icono = kwargs.get('icono', None)
        self.grande = kwargs.get('grande', False)
        self.tamano_letra = kwargs.get('tamano_letra', 1)
        self.icono_dentro = kwargs.get('icono_dentro', False)
        self.dibujar_boton()

    def dibujar_boton(self):
        """Dibuja el boton en el canvas"""
        if self.color_boton == 'rosa':
            if self.grande:
                self.image_id = self.canvas.create_image(self.x, self.y, image = self.canvas.master.controller.boton_rosa_grande)
                self.tamano_letra = 1.45
            else:
                self.image_id = self.canvas.create_image(self.x, self.y, image = self.canvas.master.controller.boton_rosa, anchor = CENTER)
        elif self.color_boton == 'verde':
            self.image_id = self.canvas.create_image(self.x, self.y, image = self.canvas.master.controller.boton_verde, anchor = CENTER)
        
        self.texto_id = self.canvas.create_text(self.x, self.y, text = self.texto, 
                                                font = ('Mukta Malar ExtraLight', int(self.canvas.master.controller.boton_tamanio * self.tamano_letra)), 
                                                anchor = CENTER)
        
        if self.icono:
            if self.icono_dentro == True:
                if not self.grande:
                    bounds = self.canvas.bbox(self.texto_id)
                    width = bounds[2] - bounds[0]
                    self.icono_id = self.canvas.create_image(self.x - 0.9 * width, self.y, image = self.icono, anchor = CENTER)
                else:
                    bounds = self.canvas.bbox(self.image_id)
                    width = bounds[2] - bounds[0]
                    self.icono_id = self.canvas.create_image(self.x - 0.375 * width, self.y, image = self.icono, anchor = CENTER)

            else:
                bounds = self.canvas.bbox(self.image_id)
                width = bounds[2] - bounds[0]
                self.icono_id = self.canvas.create_image(self.x - 0.625 * width, self.y, image = self.icono, anchor = CENTER)
        
        self.animacion()
    
    def animacion(self):
        """Agrega las animaciones al boton"""
        self.canvas.tag_bind(self.image_id, '<Enter>', self.hover_img)
        self.canvas.tag_bind(self.image_id, '<Leave>', self.leave_img)
        self.canvas.tag_bind(self.texto_id, '<Enter>', self.hover_texto)
        self.canvas.tag_bind(self.texto_id, '<Leave>', self.leave_texto)
        self.canvas.tag_bind(self.image_id, '<ButtonRelease-1>', self.command)
        self.canvas.tag_bind(self.texto_id, '<ButtonRelease-1>', self.command)
        if self.icono and self.icono_dentro:
            self.canvas.tag_bind(self.icono_id, '<Enter>', self.hover_img)
            self.canvas.tag_bind(self.icono_id, '<Leave>', self.leave_img)
            self.canvas.tag_bind(self.icono_id, '<ButtonRelease-1>', self.command)

    def hover_img(self, event):
        """Cambia la imagen del boton cuando el mouse esta encima"""
        if self.color_boton == 'rosa':
            if self.grande:
                self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_rosa__hover_grande)
            else:
                self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_rosa_hover)
        elif self.color_boton == 'verde':
            self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_verde_hover)
    
    def leave_img(self, event):
        """Cambia la imagen del boton cuando el mouse deja de estar encima"""
        if self.color_boton == 'rosa':
            if self.grande:
                self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_rosa_grande)
            else:
                self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_rosa)
        elif self.color_boton == 'verde':
            self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_verde)
        
    def hover_texto(self, event):
        """Cambia el color del texto cuando el mouse esta encima"""
        self.canvas.itemconfig(self.texto_id, fill = 'white')
        if self.color_boton == 'rosa':
            if self.grande:
                self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_rosa__hover_grande)
            else:
                self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_rosa_hover)
        elif self.color_boton == 'verde':
            self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_verde_hover)

    def leave_texto(self, event):
        """Cambia el color del texto cuando el mouse deja de estar encima"""
        self.canvas.itemconfig(self.texto_id, fill = 'black')
        if self.color_boton == 'rosa':
            if self.grande:
                self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_rosa_grande)
            else:
                self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_rosa)
        elif self.color_boton == 'verde':
            self.canvas.itemconfig(self.image_id, image = self.canvas.master.controller.boton_verde)
    
    def destroy(self):
        """Destruye el boton"""
        self.canvas.delete(self.image_id)
        self.canvas.delete(self.texto_id)
        if self.icono:
            self.canvas.delete(self.icono_id)

    def deshabilitar(self):
        """Deshabilita el boton"""
        self.canvas.itemconfig(self.image_id, state = 'disabled')
        self.canvas.itemconfig(self.texto_id, state = 'disabled')
        if self.icono:
            self.canvas.itemconfig(self.icono_id, state = 'disabled')

    def habilitar(self):
        """Habilita el boton"""
        self.canvas.itemconfig(self.image_id, state = 'normal')
        self.canvas.itemconfig(self.texto_id, state = 'normal')
        if self.icono:
            self.canvas.itemconfig(self.icono_id, state = 'normal')


class boton_atras(mi_boton):
    def __init__(self, canvas, x, y, **kwargs):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.command = kwargs.get('command', lambda x: self.canvas.master.controller.ir_atras())
        super().__init__(self.canvas, x, y, 'Atrás', 'verde', 
                        self.command)