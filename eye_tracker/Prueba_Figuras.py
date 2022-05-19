# Importamos todo desde el archivo constants.py
from pickle import FALSE
import turtle

from numpy import true_divide
from constants import *

def Figuras_superpuestas():
    if sys.argv[1]:
        global id_paciente, ruta_archivo
        id_paciente = sys.argv[1]
        ruta_archivo = docs + "\\NEURO INNOVA KIDS\\"+"DATA"+f"\{id_paciente}_figuras_{str(datetime.now().strftime('%d_%m_%Y %H_%M_%S'))}.json"
        LOGFILENAME = f"{id_paciente}_figuras_{str(datetime.now().strftime('%d_%m_%Y %H_%M_%S'))}"
    
    # Creamos los objetos para el eyetracker y la pantalla
    display = Display()
    pantalla = Screen()

    # Creamos los objetos para el mouse, el seguidor ocular y el teclado
    teclado = Keyboard()
    mouse = Mouse()
    eyetracker = EyeTracker(display, eyedatafile = LOGFILENAME, logfile = LOGFILENAME)
    eyetracker.calibrate()

    # Archivos de salida
    LOGFILE = os.path.join(DATADIR, LOGFILENAME)
    log = Logfile(filename = LOGFILE)
    log.write(["trialnr", "image", "imgtime"])
    print(log)

    # Configuramos la entrada del mouse
    mouse.set_visible(visible = True)

    # Leemos todos los nombres de la imagenes
    # images = os.listdir(IMGDIR)

    # Coloreamos la pantalla
    pantalla.set_background_colour((250, 235, 255))
    display.fill(pantalla)
    display.show()


    # Colocamos la imagen de fondo y las instrucciones en Pantalla 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_text(text="Prueba de las figuras\nsuperpuestas\nObserva las figuras a la izquierda\ny selecciona la figura que NO se encuentre", 
                fontsize=TEXTSIZE, 
                font='Mukta Malar ExtraLight',
                pos = (screenwidth*0.35,screenheight*0.5),
                colour =(0,0,0))

    # Mostrar pantalla
    display.fill(pantalla)
    display.show()
    

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()

    # Calibrar eyetracker
    # eyetracker.calibrate()
    
    # Mostrar la primer prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_1.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\16.png",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\17.png",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    # Comenzar a capturar datos
    imagen = 'prueba_1.jpg'
    eyetracker.start_recording()
    eyetracker.log("TRIALSTART %d" % 1)
    eyetracker.log("IMAGENAME %s" % 'prueba_1.jpg')
    
    display.fill(pantalla)
    t0 = display.show()

    eyetracker.log("image online at %d" % t0)
    
    # Esperar click en el boton para continuar
    x , y = 0,0
    respuestas = {}
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["1"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["1"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["1"] = True
                break
            if boton_presionado(x,y,boton4):
                respuestas["1"] = False
                break
        
        if boton_presionado(mouseX, mouseY, boton1):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\16a.png", 
                         0.4, 
                         screenwidth*0.5,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\coloreadas\\16.png", 0.6, screenwidth*0.5,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton2):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\17a.png", 
                         0.4, 
                         screenwidth*0.62,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\coloreadas\\17.png", 0.6, screenwidth*0.62,screenheight*0.5)
        
        if boton_presionado(mouseX, mouseY, boton3):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\15a.png", 
                         0.5, 
                         screenwidth*0.75,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg", 0.6, screenwidth*0.75,screenheight*0.5)
        
        if boton_presionado(mouseX, mouseY, boton4):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\13a.png", 
                         0.65, 
                         screenwidth*0.88,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg", 0.6, screenwidth*0.88,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        t1 = display.show()
    eyetracker.log("image offline at %d" % t1)

    # stop recording
    eyetracker.log("TRIALEND %d" % 1)
    eyetracker.stop_recording()

    # TRIAL AFTERMATH
    log.write([1, imagen, t1-t0])
        
    # Mostrar la segunda prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_2.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\16.png",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg",0.6,screenwidth*0.88,screenheight*0.5)
    
    # Comenzar a capturar datos
    imagen = 'prueba_2.jpg'
    prueba = 2
    eyetracker.start_recording()
    eyetracker.log("TRIALSTART %d" % prueba)
    eyetracker.log("IMAGENAME %s" % imagen)
    
    display.fill(pantalla)
    t0 = display.show()

    eyetracker.log("image online at %d" % t0)

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["2"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["2"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["2"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["2"] = False
                break
        
        if boton_presionado(mouseX, mouseY, boton1):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\9a.png", 
                         0.52, 
                         screenwidth*0.5,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg", 0.6, screenwidth*0.5,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton2):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\15a.png", 
                         0.5, 
                         screenwidth*0.62,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg", 0.6, screenwidth*0.62,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton3):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\16a.png", 
                         0.4, 
                         screenwidth*0.75,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\coloreadas\\16.png", 0.6, screenwidth*0.75,screenheight*0.5)
        
        if boton_presionado(mouseX, mouseY, boton4):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\13a.png", 
                         0.65, 
                         screenwidth*0.88,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg", 0.6, screenwidth*0.88,screenheight*0.5)  

        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        t1 = display.show()
    eyetracker.log("image offline at %d" % t1)

    # stop recording
    eyetracker.log("TRIALEND %d" % 2)
    eyetracker.stop_recording()

    # TRIAL AFTERMATH
    log.write([2, imagen, t1-t0])

    # Mostrar la tercer prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_3.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\9.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    # Comenzar a capturar datos
    imagen = 'prueba_3.jpg'
    prueba = 3
    eyetracker.start_recording()
    eyetracker.log("TRIALSTART %d" % prueba)
    eyetracker.log("IMAGENAME %s" % imagen)
    
    display.fill(pantalla)
    t0 = display.show()

    eyetracker.log("image online at %d" % t0)

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["3"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["3"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["3"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["3"] = True
                break

        if boton_presionado(mouseX, mouseY, boton1):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\15a.png", 
                         0.5, 
                         screenwidth*0.5,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg", 0.6, screenwidth*0.5,screenheight*0.5)             

        if boton_presionado(mouseX, mouseY, boton2):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\9a.png", 
                         0.52, 
                         screenwidth*0.62,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg", 0.6, screenwidth*0.62,screenheight*0.5)
        
        if boton_presionado(mouseX, mouseY, boton3):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\14a.png", 
                         0.52, 
                         screenwidth*0.75,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\9.jpg", 0.6, screenwidth*0.75,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton4):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\10a.png", 
                         0.71, 
                         screenwidth*0.88,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg", 0.6, screenwidth*0.88,screenheight*0.5)
        
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        t1 = display.show()
    eyetracker.log("image offline at %d" % t1)

    # stop recording
    eyetracker.log("TRIALEND %d" % prueba)
    eyetracker.stop_recording()

    # TRIAL AFTERMATH
    log.write([prueba, imagen, t1-t0]) 
    
    # Mostrar la cuarta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_4.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\16.png",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    # Comenzar a capturar datos
    imagen = 'prueba_4.jpg'
    prueba = 4
    eyetracker.start_recording()
    eyetracker.log("TRIALSTART %d" % prueba)
    eyetracker.log("IMAGENAME %s" % imagen)
    
    display.fill(pantalla)
    t0 = display.show()

    eyetracker.log("image online at %d" % t0)

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["4"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["4"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["4"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["4"] = True
                break

        if boton_presionado(mouseX, mouseY, boton1):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\16a.png", 
                         0.4, 
                         screenwidth*0.5,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\coloreadas\\16.png", 0.6, screenwidth*0.5,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton2):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\9a.png", 
                         0.52, 
                         screenwidth*0.62,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg", 0.6, screenwidth*0.62,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton3):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\15a.png", 
                         0.5, 
                         screenwidth*0.75,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg", 0.6, screenwidth*0.75,screenheight*0.5)   

        if boton_presionado(mouseX, mouseY, boton4):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\10a.png", 
                         0.71, 
                         screenwidth*0.88,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg", 0.6, screenwidth*0.88,screenheight*0.5)           

        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        t1 = display.show()
    eyetracker.log("image offline at %d" % t1)

    # stop recording
    eyetracker.log("TRIALEND %d" % prueba)
    eyetracker.stop_recording()
    
    # TRIAL AFTERMATH
    log.write([prueba, imagen, t1-t0])

    # Mostrar la quinta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_5.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\5.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    # Comenzar a capturar datos
    imagen = 'prueba_5.jpg'
    prueba = 5
    eyetracker.start_recording()
    eyetracker.log("TRIALSTART %d" % prueba)
    eyetracker.log("IMAGENAME %s" % imagen)
    
    display.fill(pantalla)
    t0 = display.show()

    eyetracker.log("image online at %d" % t0)

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["5"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["5"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["5"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["5"] = False
                break

        if boton_presionado(mouseX, mouseY, boton1):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\11a.png", 
                         0.62, 
                         screenwidth*0.5,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\5.jpg", 0.6, screenwidth*0.5,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton2):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\9a.png", 
                         0.52, 
                         screenwidth*0.62,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg", 0.6, screenwidth*0.62,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton3):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\15a.png", 
                         0.5, 
                         screenwidth*0.75,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg", 0.6, screenwidth*0.75,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton4):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\10a.png", 
                         0.71, 
                         screenwidth*0.88,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg", 0.6, screenwidth*0.88,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        t1 = display.show()
    eyetracker.log("image offline at %d" % t1)

    # stop recording
    eyetracker.log("TRIALEND %d" % prueba)
    eyetracker.stop_recording()
    
    # TRIAL AFTERMATH
    log.write([prueba, imagen, t1-t0])

    # Mostrar la sexta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_6.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\6.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\16.png",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    # Comenzar a capturar datos
    imagen = 'prueba_6.jpg'
    prueba = 6
    eyetracker.start_recording()
    eyetracker.log("TRIALSTART %d" % prueba)
    eyetracker.log("IMAGENAME %s" % imagen)
    
    display.fill(pantalla)
    t0 = display.show()

    eyetracker.log("image online at %d" % t0)

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["6"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["6"] = True
                break
            if boton_presionado(x,y,boton3):
                respuestas["6"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["6"] = False
                break
        
        if boton_presionado(mouseX, mouseY, boton1):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\12a.png", 
                         0.6, 
                         screenwidth*0.5,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\6.jpg", 0.6, screenwidth*0.5,screenheight*0.5)


        if boton_presionado(mouseX, mouseY, boton2):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\16a.png", 
                         0.4, 
                         screenwidth*0.62,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\coloreadas\\16.png", 0.6, screenwidth*0.62,screenheight*0.5)
        
        if boton_presionado(mouseX, mouseY, boton3):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\15a.png", 
                         0.5, 
                         screenwidth*0.75,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg", 0.6, screenwidth*0.75,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton4):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\9a.png", 
                         0.52, 
                         screenwidth*0.88,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg", 0.6, screenwidth*0.88,screenheight*0.5)
        
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        t1 = display.show()
    eyetracker.log("image offline at %d" % t1)

    # stop recording
    eyetracker.log("TRIALEND %d" % prueba)
    eyetracker.stop_recording()
    
    # TRIAL AFTERMATH
    log.write([prueba, imagen, t1-t0])

    # Mostrar la séptima prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_7.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\9.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\5.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    # Comenzar a capturar datos
    imagen = 'prueba_7.jpg'
    prueba = 7
    eyetracker.start_recording()
    eyetracker.log("TRIALSTART %d" % prueba)
    eyetracker.log("IMAGENAME %s" % imagen)
    
    display.fill(pantalla)
    t0 = display.show()

    eyetracker.log("image online at %d" % t0)

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["7"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["7"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["7"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["7"] = False
                break

        if boton_presionado(mouseX, mouseY, boton1):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\14a.png", 
                         0.52, 
                         screenwidth*0.5,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\9.jpg", 0.6, screenwidth*0.5,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton2):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\9a.png", 
                         0.52, 
                         screenwidth*0.62,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg", 0.6, screenwidth*0.62,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton3):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\15a.png", 
                         0.5, 
                         screenwidth*0.75,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg", 0.6, screenwidth*0.75,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton4):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\11a.png", 
                         0.62, 
                         screenwidth*0.88,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\5.jpg", 0.6, screenwidth*0.88,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        t1 = display.show()
    eyetracker.log("image offline at %d" % t1)

    # stop recording
    eyetracker.log("TRIALEND %d" % prueba)
    eyetracker.stop_recording()
    
    # TRIAL AFTERMATH
    log.write([prueba, imagen, t1-t0])

    # Mostrar la octava prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_8.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\6.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    # Comenzar a capturar datos
    imagen = 'prueba_8.jpg'
    prueba = 8
    eyetracker.start_recording()
    eyetracker.log("TRIALSTART %d" % prueba)
    eyetracker.log("IMAGENAME %s" % imagen)
    
    display.fill(pantalla)
    t0 = display.show()

    eyetracker.log("image online at %d" % t0)

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["8"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["8"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["8"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["8"] = False
                break
        
        if boton_presionado(mouseX, mouseY, boton1):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\12a.png", 
                         0.6, 
                         screenwidth*0.5,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\6.jpg", 0.6, screenwidth*0.5,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton2):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\13a.png", 
                         0.65, 
                         screenwidth*0.62,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg", 0.6, screenwidth*0.62,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton3):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\15a.png", 
                         0.5, 
                         screenwidth*0.75,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg", 0.6, screenwidth*0.75,screenheight*0.5)

        if boton_presionado(mouseX, mouseY, boton4):
            colocarBoton(pantalla, 
                         FONDODIR+"\coloreadas\\9a.png", 
                         0.52, 
                         screenwidth*0.88,
                         screenheight*0.5)
        else: 
            colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg", 0.6, screenwidth*0.88,screenheight*0.5)
        
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        t1 = display.show()
    eyetracker.log("image offline at %d" % t1)

    # stop recording
    eyetracker.log("TRIALEND %d" % prueba)
    eyetracker.stop_recording()
    
    # TRIAL AFTERMATH
    log.write([prueba, imagen, t1-t0])
        
    # Mostrar pantalla de guardando datos
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_text(text="Listo, se están guardando los datos", 
                    fontsize=TEXTSIZE, 
                    font='Mukta Malar ExtraLight',
                    pos = (screenwidth*0.35,screenheight*0.5),
                    colour =(0,0,0))

    display.fill(pantalla)
    display.show()

    if sys.argv[1]:
        with open(ruta_archivo, "w") as archivo:
            print(ruta_archivo)
            json.dump(respuestas, archivo, indent = 4)
        pruebas_sql(id_paciente, "figuras", ruta_archivo)
        
    # Cerramos la conexion con el eyetracker
    # Esto cerará el archivo de datos
    eyetracker.close()

    # Cerramos el archivo de log
    log.close()

    # Colocamos la imagen de fondo y las instrucciones en Pantalla 
    pantalla.clear()
    colocar_fondo(pantalla)
    pantalla.draw_text(text="Listo, haz completado la prueba haz click para salir", 
                fontsize=TEXTSIZE, 
                font='Mukta Malar ExtraLight',
                pos = (screenwidth*0.35,screenheight*0.5),
                colour =(0,0,0))
    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        if clickpos:
            break
        display.fill(pantalla)
        display.show()

    # Cerramos la pantalla
    display.close()
        
if __name__ == "__main__":
    Figuras_superpuestas()