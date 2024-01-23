from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Bloque por defecto
class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'grass',
            color = rgb(255,255,255),
            hightlight_color = color.lime,
        )

    def input(self,key):
        if self.hovered:
            # Click derecho pone bloque
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            # Click izquierdo destruye bloque
            if key == 'left mouse down':
                destroy(self)
            # Pinta un bloque a textura de ladrillo
            if key == '2':
                self.texture = 'brick'
            if key == 'escape':
                quit()

# Tamaño de chuck por defecto
chuncksize = 16

# Crea un chunck de bloques
for z in range(chuncksize):
    for x in range(chuncksize):
        voxel = Voxel(position = (x,0,z))

# Crea instancia de jugador en primera persona
player = FirstPersonController()

# Crea cielo por defecto
Sky()

app.run()