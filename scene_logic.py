from my_rects import *

class scene:
    def __init__(self, name, objects):
        self.name = name
        self.objects = objects
    
    def add_object(self, object):
        self.objects.append(object)

    def update(self):
        for num,obj in enumerate(self.objects):
            obj.draw()
            if type(obj) == player:
                obj.move(0, 0)
            for other in self.objects:
                obj.collide(other)
            

    def draw(self):
        for obj in self.objects:
            obj.draw()


class gravity_scene(scene):
    def __init__(self, name, objects, gravity):
        super().__init__(name, objects)
        self.gravity = gravity
    
    def update(self):
        for num,obj in enumerate(self.objects):
            obj.update(self.gravity)
            obj.draw()
            if type(obj) == player:
                obj.move(0, 0)
            for other in self.objects:
                #if the object extends type physicsObject
                if isinstance(obj, (physicsObject, player)):
                    obj.collide(other)

            