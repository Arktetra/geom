from typing import Tuple
import bpy

class Light:
    def __init__(self, name: str, light_type: str, energy: int = None):
        self.name = name
        self.light_type = light_type
        

        self.light_data = bpy.data.lights.new(name=self.name, type=light_type)
        if energy is not None:
            self.light_data.energy = energy

        self.objs = []

    def add(self, name: str, location: Tuple[float, float, float]):
        obj = bpy.data.objects.new(name=name, object_data=self.light_data)
        obj.location = location

        bpy.context.collection.objects.link(obj)

        self.objs.append(obj)
