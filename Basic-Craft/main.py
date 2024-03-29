from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
# Bloque por defecto
current_block_type = 'grass'

# Crear objeto de texto
texto = Text(text="", position=(-0.5, 0.4), scale=2, origin=(0, 0), color=color.brown)

# Actualiza el texto del bloque actual
def updateTextBlock():
        texto.text = "Bloque actual: " + current_block_type

imagen = Entity(model='quad', texture='grass')

# Bloque por defecto
class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = current_block_type,
            color = rgb(255,255,255),
            hightlight_color = color.lime,
        )
    
    def input(self,key):
        global current_block_type
        if self.hovered:
            # Click derecho pone bloque
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
                voxel.texture = current_block_type

            # Click izquierdo destruye bloque
            if key == 'left mouse down':
                destroy(self)

            if key == '1':
                current_block_type = 'grass'
                updateTextBlock()

            if key == '2':
                current_block_type = 'brick'
                updateTextBlock()

            if key == '3':
                current_block_type = 'grass_tintable'
                updateTextBlock()

            if key == '4':
                current_block_type = 'rainbow'
                updateTextBlock()

            if key == '0':
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