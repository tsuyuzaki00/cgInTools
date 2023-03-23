# -*- coding: iso-8859-15 -*-
import bpy
bpy.ops.mesh.primitive_plane_add()

plane = bpy.context.active_object
plane.name = "MyPlane"