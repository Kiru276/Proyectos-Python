from ursina import *

class Player(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'jerma.jpg',
            #rotation = Vec3(30,45,45),
        )


def update():
        test.rotation_x += 30* time.dt
        test.rotation_y += 30* time.dt
        test.rotation_z += 30* time.dt

Game = Ursina()

test = Player()



Game.run()