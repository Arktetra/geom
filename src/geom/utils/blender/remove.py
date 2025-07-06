import bpy

def remove_all_objects():
    bpy.ops.object.select_all(action="DESELECT")

    for obj in bpy.data.objects:
        obj.select_set(True)
    bpy.ops.object.delete(use_global=False)

    for _ in range(3):
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True,
            do_linked_ids=True,
            do_recursive=True
        )

