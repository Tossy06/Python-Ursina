from ursina import *
from ursina.prefabs.first_person_controller import *
app = Ursina()

my_object= Entity(model='skull2.obj', collider='mesh', scale = 1 ,color= color.rgba(255,0,0,0.7))

player= FirstPersonController(scale = 0.2 )



app.run()