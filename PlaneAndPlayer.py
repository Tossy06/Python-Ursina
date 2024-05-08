from ursina import *
from ursina.prefabs.first_person_controller import *

app = Ursina()

ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
player = FirstPersonController(y = 100)
app.run()