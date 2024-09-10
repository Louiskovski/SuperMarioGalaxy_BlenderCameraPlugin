bl_info = {
    "name": "Mario Galaxy Camera Plugin",
    "author": "Louis Miles",
    "version": (0, 9, 3),
    "blender": (3, 3, 2),
    "location": "In 3D Viewport right under Misc",
    "description": "Copies camera codes to paste into LaunchCamPlus and more options",
    "warning": "Only compatible with LaunchCamPlus version 2.5.0.0 or higher",
    "doc_url": "",
}


import bpy
import math
import os



def CamXYexport(context):
    C = bpy.context

    KamName = bpy.context.object.name
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    KamAxisY = bpy.context.view_layer.objects.active.rotation_euler[1]
    KamAxisX = bpy.context.view_layer.objects.active.rotation_euler[2] * -1
    KamAxisRoll = bpy.context.view_layer.objects.active.rotation_euler[0] * -1
    KamOffX = bpy.context.view_layer.objects.active.location[0]
    KamOffY = bpy.context.view_layer.objects.active.location[1]
    KamOffZ = bpy.context.view_layer.objects.active.location[2]
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    KamZoom = bpy.context.view_layer.objects.active.location[0] * -1
    KamFOV = bpy.context.view_layer.objects.active.data.angle
    KamFOV = math.degrees(KamFOV)

    LCPcode = "LCP|14F51CD8%196631%Int32|ABC4A1CF%" + str(KamAxisX) + "%Single|ABC4A1CE%" + str(KamAxisY) + "%Single|0035807D%" + str(KamAxisRoll) + "%Single|002F0DA6%" + str(KamZoom) + "%Single|00300D4C%" + str(KamFOV) + "%Single|B6004E72%120%Int32|BEC02B34%" + str(KamOffX) + "%Single|BEC02B35%" + str(KamOffY) + "%Single|BEC02B36%" + str(KamOffZ) + "%Single|9F02074F%1%Int32|00000D1B%" + str(KamName) + "%String|20C58F89%CAM_TYPE_XZ_PARA%String"
    #LCPcode = LCPcode.replace(".", ",") #Only for LCP versions under 2.5.0.0. If this line is activated, it works with 2.3.9.4 and older

    clipboard = bpy.context.window_manager.clipboard = LCPcode

    clipboard.encode("utf8")
    
    
def CamPointFixexport(context):
    C = bpy.context

    KamName = bpy.context.object.name # Name bzw ID notieren
    KamPosX = bpy.context.view_layer.objects.active.location[0]
    KamPosY = bpy.context.view_layer.objects.active.location[2]
    KamPosZ = bpy.context.view_layer.objects.active.location[1] * -1
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    KamAxisY = bpy.context.view_layer.objects.active.rotation_euler[1] - 1.570796 # -90, only Point Fix Cam type
    KamAxisX = bpy.context.view_layer.objects.active.rotation_euler[2] * -1
    KamAxisRoll = bpy.context.view_layer.objects.active.rotation_euler[0] * -1
    KamOffX = bpy.context.view_layer.objects.active.location[0]
    KamOffY = bpy.context.view_layer.objects.active.location[1]
    KamOffZ = bpy.context.view_layer.objects.active.location[2]
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    #KamZoom = bpy.data.objects["Camera"].location[0]
    KamZoom = bpy.context.view_layer.objects.active.location[0] * -1
    #KamFOV = bpy.data.objects["Camera"].data.angle
    KamFOV = bpy.context.view_layer.objects.active.data.angle
    KamFOV = math.degrees(KamFOV)
    #KamFOV = 45 #test



    LCPcode = "LCP|14F51CD8%196631%Int32|002F0DA6%" + str(KamZoom) + "%Single|BB74D6C1%1%Int32|BEC02B35%" + str(KamOffY) + "%Single|BEC02B34%" + str(KamOffX) + "%Single|0035807D%" + str(KamAxisRoll) + "%Single|BEC02B36%" + str(KamOffZ) + "%Single|AE79D1C0%120%Int32|20C58F89%CAM_TYPE_POINT_FIX%String|00000D1B%" + str(KamName) + "%String|31CB1323%" + str(KamPosX) + "%Single|31CB1324%" + str(KamPosY) + "%Single|31CB1325%" + str(KamPosZ) + "%Single|AC52894B%" + str(KamAxisX) + "%Single|AC52894C%" + str(KamAxisY) + "%Single|EB66C5C3%0%Int32"
    #LCPcode = LCPcode.replace(".", ",") #Only for LCP versions under 2.5.0.0. If this line is activated, it works with 2.3.9.4 and older

    clipboard = bpy.context.window_manager.clipboard = LCPcode

    clipboard.encode("utf8")


def CamCreate(context):
    C = bpy.context
    #Add "Mario" Cone
    bpy.ops.object.empty_add(type='CONE',radius=71, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))
    bpy.context.view_layer.objects.active.name = "xxTEMPLATExx_C:XXXX"
    bpy.context.view_layer.objects.active.lock_rotation[0] = True
    bpy.context.view_layer.objects.active.lock_rotation[1] = True
    bpy.context.view_layer.objects.active.lock_rotation[2] = True
    bpy.context.view_layer.objects.active.lock_scale[0] = True
    bpy.context.view_layer.objects.active.lock_scale[1] = True
    bpy.context.view_layer.objects.active.lock_scale[2] = True


    #Add Sphere for Angle and Offset
    bpy.ops.object.empty_add(type='SPHERE', radius=100, location=(0.0, 0.0, 0.0))
    bpy.context.view_layer.objects.active.rotation_mode = 'XZY'
    bpy.context.view_layer.objects.active.name = "xxTEMPLATExx_Sphere"
    bpy.context.view_layer.objects.active.lock_scale[0] = True
    bpy.context.view_layer.objects.active.lock_scale[1] = True
    bpy.context.view_layer.objects.active.lock_scale[2] = True


    #Add Camera
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(-500.000, 0.0, 0.0), rotation=(0.00000000000000000000000, -1.570796, 0.00000000000000000000000))
    bpy.context.view_layer.objects.active.scale = 100,100,100
    bpy.context.view_layer.objects.active.name = "xxTEMPLATExx_Camera"
    bpy.context.view_layer.objects.active.data.clip_start = 6
    bpy.context.view_layer.objects.active.data.clip_end = 7.77778e+06
    bpy.context.view_layer.objects.active.data.sensor_fit = 'VERTICAL'
    bpy.context.view_layer.objects.active.data.sensor_height = 24
    bpy.context.view_layer.objects.active.data.angle = 0.785398
    bpy.context.view_layer.objects.active.data.type = 'PERSP'
    bpy.context.view_layer.objects.active.data.lens_unit = 'FOV'
    bpy.context.view_layer.objects.active.lock_location[1] = True
    bpy.context.view_layer.objects.active.lock_location[2] = True
    bpy.context.object.lock_rotation[0] = True
    bpy.context.object.lock_rotation[1] = True
    bpy.context.object.lock_rotation[2] = True
    bpy.context.object.lock_scale[0] = True
    bpy.context.object.lock_scale[1] = True
    bpy.context.object.lock_scale[2] = True

    #parenting:
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects["xxTEMPLATExx_Sphere"].select_set(True)
    bpy.data.objects["xxTEMPLATExx_Camera"].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects["xxTEMPLATExx_Sphere"]
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    
    
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects["xxTEMPLATExx_C:XXXX"].select_set(True)
    bpy.data.objects["xxTEMPLATExx_Sphere"].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects["xxTEMPLATExx_C:XXXX"]
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    bpy.data.objects["xxTEMPLATExx_C:XXXX"].rotation_euler = (1.570796, 0.0, 0.0)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.data.objects["xxTEMPLATExx_C:XXXX"]
    bpy.context.view_layer.objects.active.location = bpy.context.scene.cursor.location



    bpy.data.objects["xxTEMPLATExx_C:XXXX"].name = "c:XXXX"
    bpy.data.objects["xxTEMPLATExx_Sphere"].name = "Rot-Pos-Offset_GalaxyCam"
    bpy.data.objects["xxTEMPLATExx_Camera"].name = "CameraZoom"




class GalaxycamOperator1(bpy.types.Operator):
    """Copy Cameracode to paste into LaunchCamPlus
You must select the cone with the camera code as the name and nothing else!"""
    bl_idname = "object.galaxycam_operator1" 
    bl_label = "XY PARA"
    def execute(self, context):
        CamXYexport(context)
        return {'FINISHED'}
    
    
class GalaxycamOperator2(bpy.types.Operator):
    """Add required camera reference objects"""
    bl_idname = "objecto.galaxycam_operator2"
    bl_label = "Add Camera"
    def execute(self, context):
        CamCreate(context) #Was vor der Klammer steht ist was er jetzt executen soll
        return {'FINISHED'}


class GalaxycamOperator3(bpy.types.Operator):
    """Copy Cameracode to paste into LaunchCamPlus
You must select the cone with the camera code as the name and nothing else!"""
    bl_idname = "objecti.galaxycam_operator3"
    bl_label = "POINT FIX"
    def execute(self, context):
        CamPointFixexport(context) #Was vor der Klammer steht ist was er jetzt executen soll
        return {'FINISHED'}


class LayoutSMGCameraPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Mario Galaxy - Camera Exporter"
    bl_idname = "SCENE_GalaxyCameraGenerator_layout" 
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        layout.label(text="Copy Camera Code")
        row = layout.row()
        row.scale_y = 1.2
        row.operator("object.galaxycam_operator1", icon='CAMERA_DATA')
        row = layout.row()
        row.scale_y = 1.2
        row.operator("objecti.galaxycam_operator3", icon='CAMERA_DATA')

        layout.label(text="Camera Actions")
        row = layout.row()
        row.scale_y = 1.2
        row.operator("objecto.galaxycam_operator2", icon='OUTLINER_OB_CAMERA')


def register():
    bpy.utils.register_class(GalaxycamOperator1)
    bpy.utils.register_class(GalaxycamOperator2)
    bpy.utils.register_class(GalaxycamOperator3)
    bpy.utils.register_class(LayoutSMGCameraPanel)
    
def unregister():
    bpy.utils.unregister_class(GalaxycamOperator1)
    bpy.utils.unregister_class(GalaxycamOperator2)
    bpy.utils.unregister_class(GalaxycamOperator3)
    bpy.utils.unregister_class(LayoutSMGCameraPanel)
    


if __name__ == "__main__":
    register()
