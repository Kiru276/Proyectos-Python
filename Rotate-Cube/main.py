from ursina import *

class Cubo(Entity):
    #Contructor
    def __init__(self):
        super().__init__(
            parent = scene, # Se establece que padre sera la escena
            model = 'cube', # Modelo de figura
            texture = 'jerma.jpg', # Variante: color = color.white,
        )

# Actualiza a tiempo real
def update():
        test.rotation_x += 30* time.dt 
        test.rotation_y += 30* time.dt
        test.rotation_z += 30* time.dt

# Inicializa ventana
Main = Ursina()

# Crea instancia de clase
test = Cubo()


# Ejecuta el programa
Main.run()