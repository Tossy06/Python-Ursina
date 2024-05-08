from ursina import *
def update():
    firstEntity.rotation_y += 50 * time.dt
    firstEntity.position += firstEntity.forward * time.dt
app = Ursina()
firstEntity = Entity(model = 'sphere',
                     color = color.rgb(0,0,255),
                     texture = 'brick',
                     position = (0,0,0),
                     rotation = (0,0,0),
                     scale = 2,
                     )
secondEntity = Entity(parent=firstEntity,
                      model = 'sphere',
                      texture = 'brick',
                      color = color.rgba(255,255,255, 0.4),
                      position = (1,1,1),
                      scale = 0.5,
                      )
EditorCamera()
app.run()