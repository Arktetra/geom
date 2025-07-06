from typing import Tuple
import bpy

class Cube:
    def __init__(
        self, 
        name: str,
        size: float = 2.0, 
        location: Tuple[float, float, float] = (0, 0, 0),
        scale: Tuple[float, float, float] = (1, 1, 1)
    ):
        self.size = size
        
        bpy.ops.mesh.primitive_cube_add(
            size=2,
            enter_editmode=False,
            align="WORLD",
            location=location,
            scale=scale
        )

        self.obj = bpy.context.object
        self.obj.name = name

    def add_material(
        self,
        name: str, 
        color: Tuple[float, float, float, float]
    ):
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True

        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Base Color"].default_value = color

        mat.diffuse_color = color

        self.obj.data.materials.append(mat)

