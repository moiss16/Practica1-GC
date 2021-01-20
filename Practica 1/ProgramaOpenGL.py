from OpenGL.GL import *
from glew_wish import *
import glfw
import random

def main():
    #inicia glfw
    if not glfw.init():
        return

    #crea una ventana,
    #indeendientemente del SO que usemos
    window = glfw.create_window(800,600,"Mi ventana", None, None)

    #configuramos opengl
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contxto
    glfw.make_context_current(window)

    #Activamos la validacion de funciones modernas de opengl
    glewExperimental = True

    if glewInit() != GLEW_OK:
        pint("No se pudo inicializar GLEW")
        return
    
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        color1 = random.random()
        color2 = random.random()
        color3 = random.random()
        color4 = random.random()
        #establece region de dibujo
        glViewport(0,0,800,600)
        #establece color de borrado
        
        glClearColor(color1,color2,color3,color4)
        #borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        
        #dibujar
        #preguntar si hubo entradas de perifericos
        #(teclado, mouse, etc)
        glfw.poll_events()
        #intercambia las buffers
        glfw.swap_buffers(window)

    #se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #termina los procesos que inicio glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()

