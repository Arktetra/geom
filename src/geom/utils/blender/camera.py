from typing import Tuple
import bpy

class Camera:
    def __init__(self, name: str):
        self.name = name

        self.data = bpy.data.cameras.new(name=self.name)
        self.objs = []

    def add(self, name: str, location: Tuple[float, float, float]):
        obj = bpy.data.objects.new(name=name, object_data=self.data)
        obj.location = location

        bpy.context.collection.objects.link(obj)

        self.objs.append(obj)

    def look_at(self, target):
        for obj in self.objs:
            direction = target.location - obj.location
            rot_quat = direction.to_track_quat("-Z", "Y")
            obj.rotation_euler = rot_quat.to_euler()

