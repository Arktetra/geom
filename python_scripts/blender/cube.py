import bpy
from pathlib import Path

from geom.utils.blender import (
    Camera, Light, Cube, remove_all_objects
)

# clean up the scene by removing all existing objects
remove_all_objects()

# create a cube with cyan material
cube = Cube("Cube")
cube.add_material("cyan", (0, 1, 1, 1))

# add a point light to illuminate the cube
light = Light("Point", "POINT", energy=3000)

# create and position multiple cameras around the cube
camera_locs = [(3, -3, 5), (3, 3, 5), (-3, 3, 5), (-3, -3, 5)]
camera = Camera("Camera")
for i, loc in enumerate(camera_locs):
    camera.add(f"camera_{i}", loc)
camera.look_at(cube.obj)

assets_dir = Path("./assets/cube/")
assets_dir.mkdir(parents=True, exist_ok=True)

bpy.context.scene.render.resolution_x = 640
bpy.context.scene.render.resolution_y = 480

bpy.context.scene.render.image_settings.file_format = "PNG"
bpy.context.scene.render.image_settings.color_mode = "RGBA"

for i, cam_obj in enumerate(camera.objs):
    bpy.context.scene.camera = cam_obj
    bpy.ops.render.render()
    bpy.data.images["Render Result"].save_render(filepath=str(assets_dir / f"{i}.png"))
