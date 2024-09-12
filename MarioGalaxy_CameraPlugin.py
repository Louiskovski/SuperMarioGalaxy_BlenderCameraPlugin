bl_info = {
    "name": "Mario Galaxy Camera Plugin",
    "author": "Louis Miles",
    "version": (0, 9, 5),
    "blender": (3, 3, 2),
    "location": "In 3D Viewport right under Misc",
    "description": "Copies camera codes to paste into LaunchCamPlus and more options",
    "warning": "",
    "doc_url": "",
}


import bpy
import math
import os



def CamXYexport(context):
    C = bpy.context

    KamName = bpy.context.object["Camera Name"]
    EnterTime = bpy.context.object["Enter Time"]
    EnterTimeTic = bpy.context.object["Enter Time Activated"]
    ExitTime = bpy.context.object["Exit Time"]
    ExitTimeTic = bpy.context.object["Exit Time Activated"]
    DpadTic = bpy.context.object["Dpad Rotation Activated"]
    FirstPersonTic = bpy.context.object["No First Person"]
    CollisionTic = bpy.context.object["No Collision"]
    NoReset = bpy.context.object["No Reset"]
    EventTime = bpy.context.object["Event Time"]
    EventPrio = bpy.context.object["Event Priority"]
    VpanX = bpy.context.object["V Pan Axis X"]
    VpanY = bpy.context.object["V Pan Axis Y"]
    VpanZ = bpy.context.object["V Pan Axis Z"]
    VpanTic = bpy.context.object["V Pan Activated"]

    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    
    KamAxisY = bpy.context.view_layer.objects.active.rotation_euler[1]
    KamAxisX = bpy.context.view_layer.objects.active.rotation_euler[2] * -1
    KamAxisRoll = bpy.context.view_layer.objects.active.rotation_euler[0] * -1
    #Offset:
    KamOffX = bpy.context.view_layer.objects.active.location[0]
    KamOffY = bpy.context.view_layer.objects.active.location[1]
    KamOffZ = bpy.context.view_layer.objects.active.location[2]
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    KamZoom = bpy.context.view_layer.objects.active.location[0] * -1
    KamFOV = bpy.context.view_layer.objects.active.data.angle
    KamFOV = math.degrees(KamFOV)


    KamType = "CAM_TYPE_XZ_PARA"
    KamString = ""

    LCPexport_KamName = KamName
    LCPexport_KamType = KamType
    LCPexport_KamString = KamString
    LCPexport_KamAxisX = KamAxisX     
    LCPexport_KamAxisY = KamAxisY
    LCPexport_KamAxisRoll = KamAxisRoll
    LCPexport_KamZoom = KamZoom
    LCPexport_KamFOV = KamFOV
    LCPexport_CamInt = EnterTime #CamInt
    
    LCPexport_CamEndInt = 120
    LCPexport_GndInt = 160
    
    LCPexport_DpadTic = DpadTic
    
    LCPexport_Num2 = 0
    LCPexport_UPlay = 300
    LCPexport_LPlay = 800
    LCPexport_PushDelay = 120
    LCPexport_PushDelayLow = 120
    LCPexport_UDown = 120
    LCPexport_LOffset = 0
    LCPexport_LOffsetV = 0
    LCPexport_Upper = 0.3
    LCPexport_Lower = 0.1
    
    LCPexport_EventTime = EventTime
    LCPexport_EventPrio = EventPrio
    LCPexport_KamOffX = KamOffX
    LCPexport_KamOffY = KamOffY
    LCPexport_KamOffZ = KamOffZ
    
    LCPexport_KamPosX = 0.0 #Only Point Fix
    LCPexport_KamPosY = 0.0
    LCPexport_KamPosZ = 0.0
    LCPexport_MiscAxisX = 0.0 #For Point Fix its Rotation
    LCPexport_MiscAxisY = 1.0
    LCPexport_MiscAxisZ = 0.0
    
    LCPexport_VpanX = VpanX
    LCPexport_VpanY = VpanY
    LCPexport_VpanZ = VpanZ
    
    LCPexport_UpAxisX = 0.0
    LCPexport_UpAxisY = 1.0
    LCPexport_UpAxisZ = 0.0
    
    LCPexport_NoReset = NoReset
    
    LCPexport_FoVtic = 1
    LCPexport_LOfsErpOff = 0
    LCPexport_DpadInterpol = 0 #AntiBlurOff
    
    LCPexport_CollisionTic = CollisionTic
    LCPexport_FirstPersonTic = FirstPersonTic
    LCPexport_ExitTimeTic = ExitTimeTic
    
    LCPexport_GThru = 0
    
    LCPexport_ExitTime = ExitTime
    LCPexport_VpanTic = VpanTic
    
    LCPexport_EFlagEndErpFrm = 0
    
    LCPexport_EnterTimeTic = EnterTimeTic
    
    
   
    LCPcode = "LCP|14F51CD8%196631%Int32|00000D1B%" + str(LCPexport_KamName) + "%String|20C58F89%" + str(LCPexport_KamType) + "%String|CAD56011%" + str(LCPexport_KamString) + "%String|ABC4A1CF%" + str(LCPexport_KamAxisX) + "%Single|ABC4A1CE%" + str(LCPexport_KamAxisY) + "%Single|0035807D%" + str(LCPexport_KamAxisRoll) + "%Single|002F0DA6%" + str(LCPexport_KamZoom) + "%Single|00300D4C%" + str(LCPexport_KamFOV) + "%Single|AE79D1C0%" + str(LCPexport_CamInt) + "%Int32|EB66C5C3%" + str(LCPexport_CamEndInt) + "%Int32|B6004E72%" + str(LCPexport_GndInt) + "%Int32|0033C56B%" + str(LCPexport_DpadTic) + "%Int32|0033C56C%" + str(LCPexport_Num2) + "%Int32|06A54929%" + str(LCPexport_UPlay) + "%Single|062675A0%" + str(LCPexport_LPlay) + "%Single|D26F6AA9%" + str(LCPexport_PushDelay) + "%Int32|93AECC0B%" + str(LCPexport_PushDelayLow) + "%Int32|069FE297%" + str(LCPexport_UDown) + "%Int32|145863FF%" + str(LCPexport_LOffset) + "%Single|76B41C57%" + str(LCPexport_LOffsetV) + "%Single|06A558A2%" + str(LCPexport_Upper) + "%Single|06262B01%" + str(LCPexport_Lower) + "%Single|05C676D0%" + str(LCPexport_EventTime) + "%Int32|730D4555%" + str(LCPexport_EventPrio) + "%Int32|BEC02B34%" + str(LCPexport_KamOffX) + "%Single|BEC02B35%" + str(LCPexport_KamOffY) + "%Single|BEC02B36%" + str(LCPexport_KamOffZ) + "%Single|31CB1323%" + str(LCPexport_KamPosX) + "%Single|31CB1324%" + str(LCPexport_KamPosY) + "%Single|31CB1325%" + str(LCPexport_KamPosZ) + "%Single|AC52894B%" + str(LCPexport_MiscAxisX) + "%Single|AC52894C%" + str(LCPexport_MiscAxisY) + "%Single|AC52894D%" + str(LCPexport_MiscAxisZ) + "%Single|3B5CB472%" + str(LCPexport_VpanX) + "%Single|3B5CB473%" + str(LCPexport_VpanY) + "%Single|3B5CB474%" + str(LCPexport_VpanZ) + "%Single|0036D9C5%" + str(LCPexport_UpAxisX) + "%Single|0036D9C6%" + str(LCPexport_UpAxisY) + "%Single|0036D9C7%" + str(LCPexport_UpAxisZ) + "%Single|41E363AC%" + str(LCPexport_NoReset) + "%Int32|9F02074F%" + str(LCPexport_FoVtic) + "%Int32|82D5627E%" + str(LCPexport_LOfsErpOff) + "%Int32|E2044E84%" + str(LCPexport_DpadInterpol) + "%Int32|521E5C3F%" + str(LCPexport_CollisionTic) + "%Int32|BB74D6C1%" + str(LCPexport_FirstPersonTic) + "%Int32|DA484167%" + str(LCPexport_ExitTimeTic) + "%Int32|ED8DD072%" + str(LCPexport_GThru) + "%Int32|67D981E8%" + str(LCPexport_ExitTime) + "%Int32|26C8C3C0%" + str(LCPexport_VpanTic) + "%Int32|45E50EE5%" + str(LCPexport_EFlagEndErpFrm) + "%Int32|1BCD52AA%" + str(LCPexport_EnterTimeTic) + "%Int32"


    clipboard = bpy.context.window_manager.clipboard = LCPcode

    clipboard.encode("utf8")
    
    
    
    
def CamPointFixexport(context):
    C = bpy.context

    KamName = bpy.context.object["Camera Name"]
    EnterTime = bpy.context.object["Enter Time"]
    EnterTimeTic = bpy.context.object["Enter Time Activated"]
    ExitTime = bpy.context.object["Exit Time"]
    ExitTimeTic = bpy.context.object["Exit Time Activated"]
    
    DpadTic = bpy.context.object["Dpad Rotation Activated"]
    FirstPersonTic = bpy.context.object["No First Person"]
    CollisionTic = bpy.context.object["No Collision"]
    NoReset = bpy.context.object["No Reset"]
    
    EventTime = bpy.context.object["Event Time"]
    EventPrio = bpy.context.object["Event Priority"]
    
    VpanX = bpy.context.object["V Pan Axis X"]
    VpanY = bpy.context.object["V Pan Axis Y"]
    VpanZ = bpy.context.object["V Pan Axis Z"]
    VpanTic = bpy.context.object["V Pan Activated"]
    
    
    KamPosX = bpy.context.view_layer.objects.active.location[0]
    KamPosY = bpy.context.view_layer.objects.active.location[2]
    KamPosZ = bpy.context.view_layer.objects.active.location[1] * -1
    
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    
    KamAxisY = bpy.context.view_layer.objects.active.rotation_euler[1] - 1.570796 # +90, only Point Fix Cam type
    KamAxisX = bpy.context.view_layer.objects.active.rotation_euler[2] * -1
    KamAxisRoll = bpy.context.view_layer.objects.active.rotation_euler[0] * -1
    KamOffX = bpy.context.view_layer.objects.active.location[0]
    KamOffY = bpy.context.view_layer.objects.active.location[1]
    KamOffZ = bpy.context.view_layer.objects.active.location[2]
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    KamZoom = bpy.context.view_layer.objects.active.location[0] * -1
    KamFOV = bpy.context.view_layer.objects.active.data.angle
    KamFOV = math.degrees(KamFOV)
    

    KamType = "CAM_TYPE_POINT_FIX"
    KamString = ""

    LCPexport_KamName = KamName
    LCPexport_KamType = KamType
    LCPexport_KamString = KamString
    
    LCPexport_KamAxisX = 0     #Unused in this type.
    LCPexport_KamAxisY = 0
    LCPexport_KamAxisRoll = 0
    
    LCPexport_KamZoom = KamZoom
    LCPexport_KamFOV = KamFOV
    LCPexport_CamInt = EnterTime #CamInt
    
    LCPexport_CamEndInt = 120
    LCPexport_GndInt = 160
    
    LCPexport_DpadTic = DpadTic
    LCPexport_Num2 = 0
    
    LCPexport_UPlay = 300
    LCPexport_LPlay = 800
    LCPexport_PushDelay = 120
    LCPexport_PushDelayLow = 120
    LCPexport_UDown = 120
    LCPexport_LOffset = 0
    LCPexport_LOffsetV = 0
    LCPexport_Upper = 0.3
    LCPexport_Lower = 0.1
    
    LCPexport_EventTime = EventTime
    LCPexport_EventPrio = EventPrio
    LCPexport_KamOffX = KamOffX
    LCPexport_KamOffY = KamOffY
    LCPexport_KamOffZ = KamOffZ
    LCPexport_KamPosX = KamPosX #Only for Point Fix type
    LCPexport_KamPosY = KamPosY
    LCPexport_KamPosZ = KamPosZ
    LCPexport_MiscAxisX = KamAxisX #For Point Fix its rotation
    LCPexport_MiscAxisY = KamAxisY
    LCPexport_MiscAxisZ = KamAxisRoll
    LCPexport_VpanX = VpanX
    LCPexport_VpanY = VpanY
    LCPexport_VpanZ = VpanZ
    
    LCPexport_UpAxisX = 0.0
    LCPexport_UpAxisY = 1.0
    LCPexport_UpAxisZ = 0.0
    
    LCPexport_NoReset = NoReset
    
    LCPexport_FoVtic = 1
    LCPexport_LOfsErpOff = 0
    LCPexport_DpadInterpol = 0 #AntiBlurOff
    
    LCPexport_CollisionTic = CollisionTic
    LCPexport_FirstPersonTic = FirstPersonTic
    LCPexport_ExitTimeTic = ExitTimeTic
    
    LCPexport_GThru = 0
    
    LCPexport_ExitTime = ExitTime
    LCPexport_VpanTic = VpanTic
    
    LCPexport_EFlagEndErpFrm = 0
    
    LCPexport_EnterTimeTic = EnterTimeTic
    
    
    LCPcode = "LCP|14F51CD8%196631%Int32|00000D1B%" + str(LCPexport_KamName) + "%String|20C58F89%" + str(LCPexport_KamType) + "%String|CAD56011%" + str(LCPexport_KamString) + "%String|ABC4A1CF%" + str(LCPexport_KamAxisX) + "%Single|ABC4A1CE%" + str(LCPexport_KamAxisY) + "%Single|0035807D%" + str(LCPexport_KamAxisRoll) + "%Single|002F0DA6%" + str(LCPexport_KamZoom) + "%Single|00300D4C%" + str(LCPexport_KamFOV) + "%Single|AE79D1C0%" + str(LCPexport_CamInt) + "%Int32|EB66C5C3%" + str(LCPexport_CamEndInt) + "%Int32|B6004E72%" + str(LCPexport_GndInt) + "%Int32|0033C56B%" + str(LCPexport_DpadTic) + "%Int32|0033C56C%" + str(LCPexport_Num2) + "%Int32|06A54929%" + str(LCPexport_UPlay) + "%Single|062675A0%" + str(LCPexport_LPlay) + "%Single|D26F6AA9%" + str(LCPexport_PushDelay) + "%Int32|93AECC0B%" + str(LCPexport_PushDelayLow) + "%Int32|069FE297%" + str(LCPexport_UDown) + "%Int32|145863FF%" + str(LCPexport_LOffset) + "%Single|76B41C57%" + str(LCPexport_LOffsetV) + "%Single|06A558A2%" + str(LCPexport_Upper) + "%Single|06262B01%" + str(LCPexport_Lower) + "%Single|05C676D0%" + str(LCPexport_EventTime) + "%Int32|730D4555%" + str(LCPexport_EventPrio) + "%Int32|BEC02B34%" + str(LCPexport_KamOffX) + "%Single|BEC02B35%" + str(LCPexport_KamOffY) + "%Single|BEC02B36%" + str(LCPexport_KamOffZ) + "%Single|31CB1323%" + str(LCPexport_KamPosX) + "%Single|31CB1324%" + str(LCPexport_KamPosY) + "%Single|31CB1325%" + str(LCPexport_KamPosZ) + "%Single|AC52894B%" + str(LCPexport_MiscAxisX) + "%Single|AC52894C%" + str(LCPexport_MiscAxisY) + "%Single|AC52894D%" + str(LCPexport_MiscAxisZ) + "%Single|3B5CB472%" + str(LCPexport_VpanX) + "%Single|3B5CB473%" + str(LCPexport_VpanY) + "%Single|3B5CB474%" + str(LCPexport_VpanZ) + "%Single|0036D9C5%" + str(LCPexport_UpAxisX) + "%Single|0036D9C6%" + str(LCPexport_UpAxisY) + "%Single|0036D9C7%" + str(LCPexport_UpAxisZ) + "%Single|41E363AC%" + str(LCPexport_NoReset) + "%Int32|9F02074F%" + str(LCPexport_FoVtic) + "%Int32|82D5627E%" + str(LCPexport_LOfsErpOff) + "%Int32|E2044E84%" + str(LCPexport_DpadInterpol) + "%Int32|521E5C3F%" + str(LCPexport_CollisionTic) + "%Int32|BB74D6C1%" + str(LCPexport_FirstPersonTic) + "%Int32|DA484167%" + str(LCPexport_ExitTimeTic) + "%Int32|ED8DD072%" + str(LCPexport_GThru) + "%Int32|67D981E8%" + str(LCPexport_ExitTime) + "%Int32|26C8C3C0%" + str(LCPexport_VpanTic) + "%Int32|45E50EE5%" + str(LCPexport_EFlagEndErpFrm) + "%Int32|1BCD52AA%" + str(LCPexport_EnterTimeTic) + "%Int32"



    clipboard = bpy.context.window_manager.clipboard = LCPcode

    clipboard.encode("utf8")
    
    
    
def CamCreate(context):
    C = bpy.context
    #Add "Mario" Cone
    bpy.ops.object.empty_add(type='CONE',radius=71, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))
    
    #Camera Settings via Blender's properties
    bpy.context.object["Camera Name"] = "c:0000"
    bpy.context.object["Enter Time"] = 120
    bpy.context.object["Enter Time Activated"] = 1
    bpy.context.object["Exit Time"] = 120
    bpy.context.object["Exit Time Activated"] = 0
    bpy.context.object["Dpad Rotation Activated"] = 1
    bpy.context.object["No First Person"] = 1
    bpy.context.object["No Collision"] = 1
    
    bpy.context.object["V Pan Axis X"] = 0
    bpy.context.object["V Pan Axis Y"] = 1
    bpy.context.object["V Pan Axis Z"] = 0
    bpy.context.object["V Pan Activated"] = 1
    
    bpy.context.object["Event Time"] = 0
    bpy.context.object["Event Priority"] = 0
    bpy.context.object["No Reset"] = 0

    
    
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

    bpy.data.objects["xxTEMPLATExx_C:XXXX"].rotation_euler = (1.570796, 0.0, 0.0) # Rotate MarioPos so that Y is up

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.data.objects["xxTEMPLATExx_C:XXXX"]
    bpy.context.view_layer.objects.active.location = bpy.context.scene.cursor.location



    bpy.data.objects["xxTEMPLATExx_C:XXXX"].name = "GalaxyCamera"
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
        CamCreate(context) 
        return {'FINISHED'}


class GalaxycamOperator3(bpy.types.Operator):
    """Add required camera reference objects"""
    bl_idname = "objecti.galaxycam_operator3"
    bl_label = "POINT FIX" 
    def execute(self, context):
        CamPointFixexport(context) 
        return {'FINISHED'}
    
    

#LAYOUT -----------------------------------------------------

class LayoutSMGCameraPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Mario Galaxy - Camera Exporter"
    bl_idname = "SCENE_GalaxyCameraGenerator_layout" 
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mario Galaxy"

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
        
        layout.label(text="Camera Settings (select cone)")
        row = layout.row()
        
        row = layout.prop(bpy.context.view_layer.objects.active, '["Camera Name"]')



        split = layout.split()

        
        col = split.column(align=True)
        col.label(text="Time:")
        col.prop(bpy.context.view_layer.objects.active, '["Enter Time"]')
        col.prop(bpy.context.view_layer.objects.active, '["Exit Time"]')
        col.prop(bpy.context.view_layer.objects.active, '["Enter Time Activated"]')
        col.prop(bpy.context.view_layer.objects.active, '["Exit Time Activated"]')
        
        col = split.column(align=True)
        col.label(text="Event Time:")
        col.prop(bpy.context.view_layer.objects.active, '["Event Time"]')
        col.prop(bpy.context.view_layer.objects.active, '["Event Priority"]')
        
        split = layout.split()

        

        row = layout.row(align=True)

        col2 = split.column(align=True)
        col2.label(text="General Settings:")
        col2.prop(bpy.context.view_layer.objects.active, '["No First Person"]')
        col2.prop(bpy.context.view_layer.objects.active, '["Dpad Rotation Activated"]')
        col2.prop(bpy.context.view_layer.objects.active, '["No Collision"]') 
        col2.prop(bpy.context.view_layer.objects.active, '["No Reset"]') 
        
        col2 = split.column(align=True)
        col2.label(text="V Pan Settings:")
        col2.prop(bpy.context.view_layer.objects.active, '["V Pan Axis X"]')
        col2.prop(bpy.context.view_layer.objects.active, '["V Pan Axis Y"]')
        col2.prop(bpy.context.view_layer.objects.active, '["V Pan Axis Z"]')
        col2.prop(bpy.context.view_layer.objects.active, '["V Pan Activated"]')
    
        



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
