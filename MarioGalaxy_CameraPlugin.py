bl_info = {
    "name": "Mario Galaxy Camera Plugin",
    "author": "Louis Miles",
    "version": (0, 9, 7),
    "blender": (4, 3, 2),
    "location": "In 3D Viewport right under Misc",
    "description": "Copies camera codes to paste into LaunchCamPlus and more. Including CANM Keyframe export",
    "warning": "",
    "doc_url": "",
}


import bpy
import math
import os
import struct


def CamXYexport(context):
    C = bpy.context

    KamName = bpy.context.object["Camera Name"]
    EnterTime = bpy.context.object["Enter Time"]
    EnterTimeTic = bpy.context.object["Enter Time Activated"]
    if EnterTimeTic == True: #If camera uses integer prop instead of boolean
        EnterTimeTic = 1
    if EnterTimeTic == False:
        EnterTimeTic = 0
    ExitTime = bpy.context.object["Exit Time"]
    ExitTimeTic = bpy.context.object["Exit Time Activated"]
    if ExitTimeTic == True:
        ExitTimeTic = 1
    if ExitTimeTic == False:
        ExitTimeTic = 0
    DpadTic = bpy.context.object["Dpad Rotation Activated"]
    if DpadTic == True:
        DpadTic = 1
    if DpadTic == False:
        DpadTic = 0
    FirstPersonTic = bpy.context.object["No First Person"]
    if FirstPersonTic == True:
        FirstPersonTic = 1
    if FirstPersonTic == False:
        FirstPersonTic = 0
    CollisionTic = bpy.context.object["No Collision"]
    if CollisionTic == True:
        CollisionTic = 1
    if CollisionTic == False:
        CollisionTic = 0
    NoReset = bpy.context.object["No Reset"]
    if NoReset == True:
        NoReset = 1
    if NoReset == False:
        NoReset = 0
    EventTime = bpy.context.object["Event Time"]
    EventPrio = bpy.context.object["Event Priority"]
    VpanX = bpy.context.object["V Pan Axis X"]
    VpanY = bpy.context.object["V Pan Axis Y"]
    VpanZ = bpy.context.object["V Pan Axis Z"]
    VpanTic = bpy.context.object["V Pan Activated"]
    if VpanTic == True:
        VpanTic = 1
    if VpanTic == False:
        VpanTic = 0

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
    if EnterTimeTic == True: #If camera uses integer prop instead of boolean
        EnterTimeTic = 1
    if EnterTimeTic == False:
        EnterTimeTic = 0
    ExitTime = bpy.context.object["Exit Time"]
    ExitTimeTic = bpy.context.object["Exit Time Activated"]
    if ExitTimeTic == True:
        ExitTimeTic = 1
    if ExitTimeTic == False:
        ExitTimeTic = 0
    DpadTic = bpy.context.object["Dpad Rotation Activated"]
    if DpadTic == True:
        DpadTic = 1
    if DpadTic == False:
        DpadTic = 0
    FirstPersonTic = bpy.context.object["No First Person"]
    if FirstPersonTic == True:
        FirstPersonTic = 1
    if FirstPersonTic == False:
        FirstPersonTic = 0
    CollisionTic = bpy.context.object["No Collision"]
    if CollisionTic == True:
        CollisionTic = 1
    if CollisionTic == False:
        CollisionTic = 0
    NoReset = bpy.context.object["No Reset"]
    if NoReset == True:
        NoReset = 1
    if NoReset == False:
        NoReset = 0
    EventTime = bpy.context.object["Event Time"]
    EventPrio = bpy.context.object["Event Priority"]
    VpanX = bpy.context.object["V Pan Axis X"]
    VpanY = bpy.context.object["V Pan Axis Y"]
    VpanZ = bpy.context.object["V Pan Axis Z"]
    VpanTic = bpy.context.object["V Pan Activated"]
    if VpanTic == True:
        VpanTic = 1
    if VpanTic == False:
        VpanTic = 0
    
    
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
    bpy.context.object["Enter Time Activated"] = True #1
    bpy.context.object["Exit Time"] = 120
    bpy.context.object["Exit Time Activated"] = False #0
    bpy.context.object["Dpad Rotation Activated"] = True #1
    bpy.context.object["No First Person"] = True #1
    bpy.context.object["No Collision"] = True #1
    
    bpy.context.object["V Pan Axis X"] = 0
    bpy.context.object["V Pan Axis Y"] = 1
    bpy.context.object["V Pan Axis Z"] = 0
    bpy.context.object["V Pan Activated"] = True #1
    
    bpy.context.object["Event Time"] = 0
    bpy.context.object["Event Priority"] = 0
    bpy.context.object["No Reset"] = False #0

    
    
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





#### CANM Stuff #####

def export_axis_keyframes(obj, data_path, axis_index, HandleTypeIsFree, SwapPlusMinus, ToDegrees, f, BlaToFOV):
    
    if not obj.animation_data or not obj.animation_data.action:
        print("Kein Animations-Data vorhanden.")
        return

    fcurves = [fcurve for fcurve in obj.animation_data.action.fcurves if fcurve.data_path == data_path and fcurve.array_index == axis_index]
    
    if not fcurves:
        print("Keine F-Curve für den angegebenen Pfad gefunden.")
        
        return

    keyframes = []
    for fcurve in fcurves:
        for kp in fcurve.keyframe_points:
            frame = kp.co.x
            value = kp.co.y
            handle_left = kp.handle_left.y - value
            handle_right = kp.handle_right.y - value
            
            
            if SwapPlusMinus == True: # Y in Blender -> -Z in Galaxy
                keyframes.append((frame, value * -1, handle_left, handle_right))
            else:
                keyframes.append((frame, value, handle_left * -1, handle_right * -1)) #In SMG handles are up side down
    
    
    
    
    if HandleTypeIsFree == True:
        for frame, value, handle_left, handle_right in keyframes:
            
            if ToDegrees == True:
                value = (math.degrees(value))
            
            if BlaToFOV == True:
                SensorSize = obj.sensor_height
                value = 2 * math.degrees(math.atan(SensorSize / (2 * value))) # Focal Length to FoV
            
            if data_path == "rotation_euler":   #Roll is upside down in Galaxy
                value = value * -1
            
            
            f.write(struct.pack(">ffff", frame, value, handle_left, handle_right)) 

    else:
        for frame, value, handle_left, handle_right in keyframes:
            
            if ToDegrees == True:
                value = (math.degrees(value))
                       
            f.write(struct.pack(">fff", frame, value, handle_left)) 
               

def is_fcurve_aligned(fcurve):
    keyframe_count = len(fcurve.keyframe_points)
    
    for kp in fcurve.keyframe_points:
        if kp.interpolation != 'BEZIER':  # Falls nicht Bezier, kann es nicht 'Aligned' sein
            return False, keyframe_count
        if kp.handle_left_type != 'ALIGNED' or kp.handle_right_type != 'ALIGNED':
            return False, keyframe_count
    
    return True, keyframe_count


def check_axis_handle_type(obj, data_path, axis_index):
    if not obj.animation_data or not obj.animation_data.action:
        return False, 0  # Kein Animations-Data vorhanden

    for fcurve in obj.animation_data.action.fcurves:
        if fcurve.data_path == data_path and fcurve.array_index == axis_index:
            return is_fcurve_aligned(fcurve)

    return False, 0  # Keine passende F-Curve gefunden


def get_first_keyframe(obj, data_path, index=0):
    if obj is None or obj.animation_data is None or obj.animation_data.action is None:
        return None  # Keine Anims da

    action = obj.animation_data.action
    for fcurve in action.fcurves:
        if fcurve.data_path == data_path and fcurve.array_index == index:
            if len(fcurve.keyframe_points) > 0:
                first_keyframe = fcurve.keyframe_points[0]  # Erster Keyframe
                return first_keyframe.co.x, first_keyframe.co.y  # (Frame, Wert)
    
    return None  # Keine passenden Keyframes gefunden



def CANMexport(context):
    ### CANM erstellen:
    obj = bpy.context.object

    Frames = bpy.context.object["CANM Export Frames"] 
    CANMFilename = bpy.context.object["CANM Filename"]

    if bpy.context.object["Export To SuperBlenderGalaxy"] == False:
        CANMfilepath = bpy.path.abspath("//" + CANMFilename + ".canm")
        print(CANMfilepath)
    else:
        
        for col in bpy.data.collections:
            if "Zone ID" in col:
                if col["Zone ID"] == 0:
                    MapName = col.name
        CANMfilepath = bpy.path.abspath("//05_MapExport\\" + MapName + "Map\\stage\\camera\\" + CANMFilename + ".canm")






    with open(CANMfilepath, "wb") as f:
        
        # Header Zeug
        f.write(b"ANDOCKAN\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04")
        
        #Frames
        f.write(struct.pack(">I", int(Frames)))

        #Axen Setup Info Block Länge, ist immer gleich oder
        f.write(b"\x00\x00\x00\x60")
        
        
        ##### FRAME SETUP INFO BLOCK ######
        
        
        StartIndexCounter = 0
        
        
        ## KAMERA ##
        
        # X #
        is_aligned, keyframe_count = check_axis_handle_type(bpy.context.object, "location", 0)
        
        if keyframe_count <= 1:  #CANM braucht immer mindestens 1 frame -> nehme momentane pos
            keyframe_count = 1
            KamPosX_Empty = True
            is_aligned = True  #spart speicherplatz
        else:
            KamPosX_Empty = False
        
        f.write(struct.pack(">i", keyframe_count)) # Keyframe Anzahl
        f.write(b"\x00\x00\x00\x00")               # Start value index im Frame Info Block 
        if is_aligned == True:                     # Handle Typ
            KamPosX_HandleType = "Symmetric"
            f.write(b"\x00\x00\x00\x00")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 3 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -2  #Der Blcok ist nur 4 bytes gross, also nur 1 adden
            
        else:
            KamPosX_HandleType = "PieceWise"
            f.write(b"\x00\x00\x00\x01")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 4 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -3
            
            
        
        # Y #
        is_aligned, keyframe_count = check_axis_handle_type(bpy.context.object, "location", 2)
        
        if keyframe_count <= 1:
            keyframe_count = 1
            KamPosY_Empty = True
            is_aligned = True
        else:
            KamPosY_Empty = False
        
        f.write(struct.pack(">i", keyframe_count)) # Keyframe Anzahl
        f.write(struct.pack(">i", StartIndexCounter)) # Start value index im Frame Info Block 
        if is_aligned == True:                     # Handle Typ
            KamPosY_HandleType = "Symmetric"
            f.write(b"\x00\x00\x00\x00")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 3 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -2
            
        else:
            KamPosY_HandleType = "PieceWise"
            f.write(b"\x00\x00\x00\x01")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 4 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -3
            
            
        # Z #
        is_aligned, keyframe_count = check_axis_handle_type(bpy.context.object, "location", 1)
        
        if keyframe_count <= 1:
            keyframe_count = 1
            KamPosZ_Empty = True
            is_aligned = True
        else:
            KamPosZ_Empty = False
        
        f.write(struct.pack(">i", keyframe_count)) # Keyframe Anzahl
        f.write(struct.pack(">i", StartIndexCounter)) # Start value index im Frame Info Block 
        if is_aligned == True:                     # Handle Typ
            KamPosZ_HandleType = "Symmetric"
            f.write(b"\x00\x00\x00\x00")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 3 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -2
            
        else:
            KamPosZ_HandleType = "PieceWise"
            f.write(b"\x00\x00\x00\x01")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 4 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -3
            
            
        
        ## LOOK AT Objekt ##
        
        # Zugriff auf das constraints objekt fuer Look At
        for constraint in obj.constraints:
            if constraint.type == 'TRACK_TO':  # Prüfen, ob es ein "Track To"-Constraint ist
                target_obj = constraint.target
                if target_obj:
                    print("Track To-Ziel:", target_obj.name)
                else:
                    print("Kein Zielobjekt im Track To-Constraint gesetzt.")
                break

        print(target_obj.name)
        print("tada")
        print(obj.name)
        
        
        # X #
        is_aligned, keyframe_count = check_axis_handle_type(target_obj, "location", 0)
        
        if keyframe_count <= 1:
            keyframe_count = 1
            LookAtPosX_Empty = True
            is_aligned = True
        else:
            LookAtPosX_Empty = False
        
        f.write(struct.pack(">i", keyframe_count)) # Keyframe Anzahl
        f.write(struct.pack(">i", StartIndexCounter)) # Start value index im Frame Info Block
        if is_aligned == True:                     # Handle Typ
            LookAtPosX_HandleType = "Symmetric"
            f.write(b"\x00\x00\x00\x00")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 3 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -2

        else:
            LookAtPosX_HandleType = "PieceWise"
            f.write(b"\x00\x00\x00\x01")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 4 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -3

            
        
        # Y #
        is_aligned, keyframe_count = check_axis_handle_type(target_obj, "location", 2)
        
        if keyframe_count <= 1:
            keyframe_count = 1
            LookAtPosY_Empty = True
            is_aligned = True
        else:
            LookAtPosY_Empty = False
        
        f.write(struct.pack(">i", keyframe_count)) # Keyframe Anzahl
        f.write(struct.pack(">i", StartIndexCounter)) # Start value index im Frame Info Block
        if is_aligned == True:                     # Handle Typ
            LookAtPosY_HandleType = "Symmetric"
            f.write(b"\x00\x00\x00\x00")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 3 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -2

        else:
            LookAtPosY_HandleType = "PieceWise"
            f.write(b"\x00\x00\x00\x01")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 4 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -3

            
            
        # Z #
        is_aligned, keyframe_count = check_axis_handle_type(target_obj, "location", 1)
        
        if keyframe_count <= 1:
            keyframe_count = 1
            LookAtPosZ_Empty = True
            is_aligned = True
        else:
            LookAtPosZ_Empty = False
        
        f.write(struct.pack(">i", keyframe_count)) # Keyframe Anzahl
        f.write(struct.pack(">i", StartIndexCounter)) # Start value index im Frame Info Block
        if is_aligned == True:                     # Handle Typ
            LookAtPosZ_HandleType = "Symmetric"
            f.write(b"\x00\x00\x00\x00")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 3 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -2

        else:
            LookAtPosZ_HandleType = "PieceWise"
            f.write(b"\x00\x00\x00\x01")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 4 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -3

        
        
        
        ## KAMERA ROLL ##
        
        is_aligned, keyframe_count = check_axis_handle_type(target_obj, "rotation_euler", 0)
        
        if keyframe_count <= 1:
            keyframe_count = 1
            KamRoll_Empty = True
            is_aligned = True
        else:
            KamRoll_Empty = False
        
        f.write(struct.pack(">i", keyframe_count)) # Keyframe Anzahl
        f.write(struct.pack(">i", StartIndexCounter)) # Start value index im Frame Info Block
        if is_aligned == True:                     # Handle Typ
            KamRoll_HandleType = "Symmetric"
            f.write(b"\x00\x00\x00\x00")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 3 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -2

        else:
            KamRoll_HandleType = "PieceWise"
            f.write(b"\x00\x00\x00\x01")
            
            StartIndexCounter = StartIndexCounter + ( keyframe_count * 4 )
            
            if keyframe_count == 1:
                 StartIndexCounter = StartIndexCounter -3

        
        
        ## FOV ##
        is_aligned, keyframe_count = check_axis_handle_type(bpy.context.object.data, "lens", 0)
        
        # if bpy.context.object.data.lens_unit == 'FOV': #FOV can not be animated, but Focal Lenght yes 
            # keyframe_count = 1
            # KamFOV_Empty = True
            # KamFOV_realFOV = True
            # is_aligned = True
        # else:
        if keyframe_count <= 1:
            keyframe_count = 1
            KamFOV_Empty = True
            #KamFOV_realFOV = False
            is_aligned = True
        else:
            KamFOV_Empty = False
            #KamFOV_realFOV = False
        
        f.write(struct.pack(">i", keyframe_count)) # Keyframe Anzahl
        f.write(struct.pack(">i", StartIndexCounter)) # Start value index im Frame Info Block
        if is_aligned == True:                     # Handle Typ
            FOV_HandleType = "Symmetric"
            f.write(b"\x00\x00\x00\x00")

        else:
            FOV_HandleType = "PieceWise"
            f.write(b"\x00\x00\x00\x01")
        
        
        
        
        
        
        
        ## Frame Info Block Laenge
        f.write(b"\xAA\xBB\xCC\xDD") # Platzhalter erstmal
        
        
        
        
        
        
        
        ###### FRAMES EXPORT #####         #################################
        
        ### KAMERA ###

        
        # X Axe #######
        
        if KamPosX_Empty == True:
            
            FirstKeyframe = get_first_keyframe(obj, "location", 0)
            if FirstKeyframe:
                print(FirstKeyframe[1])
                f.write(struct.pack(">f", FirstKeyframe[1])) #nehme einzige keyframe in die canm
        
            else:
                print("Keine X-Positions-Keyframes gefunden.")
                f.write(struct.pack(">f", obj.location[0])) #nehme momentane pos in die CANM
        
        else:
            if KamPosX_HandleType == "Symmetric":
                HandleTypeIsFree = False
            else:
                HandleTypeIsFree = True
            export_axis_keyframes(obj, "location", 0, HandleTypeIsFree, False, False, f, False) #0 für X-Achse, 1 für Y, 2 für Z
            
        
        # Y Axe #####
        
        if KamPosY_Empty == True:
            
            FirstKeyframe = get_first_keyframe(obj, "location", 2)
            if FirstKeyframe:
                print(FirstKeyframe[1])
                f.write(struct.pack(">f", FirstKeyframe[1])) #nehme einzige keyframe in die canm
        
            else:
                print("Keine X-Positions-Keyframes gefunden.")
                f.write(struct.pack(">f", obj.location[2])) #nehme momentane pos in die CANM
            
        else:
            if KamPosY_HandleType == "Symmetric":
                HandleTypeIsFree = False
            else:
                HandleTypeIsFree = True
            export_axis_keyframes(obj, "location", 2, HandleTypeIsFree, False, False, f, False)

        
        # Z Axe ##########
        
        if KamPosZ_Empty == True:
            
            FirstKeyframe = get_first_keyframe(obj, "location", 1)
            if FirstKeyframe:
                print(FirstKeyframe[1])
                f.write(struct.pack(">f", (FirstKeyframe[1]*-1))) #nehme einzige keyframe in die canm
        
            else:
                print("Keine X-Positions-Keyframes gefunden.")
                f.write(struct.pack(">f", (obj.location[1]*-1) )) #nehme momentane pos in die CANM
        
        else:
            if KamPosZ_HandleType == "Symmetric":
                HandleTypeIsFree = False
            else:
                HandleTypeIsFree = True
            export_axis_keyframes(obj, "location", 1, HandleTypeIsFree, True, False, f, False)
        
        
        
        ### LOOK AT OBJ ###

        # X Axe
        
        if LookAtPosX_Empty == True:
            
            FirstKeyframe = get_first_keyframe(target_obj, "location", 0)
            if FirstKeyframe:
                print(FirstKeyframe[1])
                f.write(struct.pack(">f", FirstKeyframe[1])) #nehme einzige keyframe in die canm
        
            else:
                print("Keine X-Positions-Keyframes gefunden.")
                f.write(struct.pack(">f", target_obj.location[0])) #nehme momentane pos in die CANM
            
        else:
            if LookAtPosX_HandleType == "Symmetric":
                HandleTypeIsFree = False
            else:
                HandleTypeIsFree = True
            export_axis_keyframes(target_obj, "location", 0, HandleTypeIsFree, False, False, f, False) #0 für X-Achse, 1 für Y, 2 für Z
        
        
        # Y Axe
        
        if LookAtPosY_Empty == True:
            
            FirstKeyframe = get_first_keyframe(target_obj, "location", 2)
            if FirstKeyframe:
                print(FirstKeyframe[1])
                f.write(struct.pack(">f", FirstKeyframe[1])) #nehme einzige keyframe in die canm
        
            else:
                print("Keine X-Positions-Keyframes gefunden.")
                f.write(struct.pack(">f", target_obj.location[2])) #nehme momentane pos in die CANM
            
        else:
        
            if LookAtPosY_HandleType == "Symmetric":
                HandleTypeIsFree = False
            else:
                HandleTypeIsFree = True
            export_axis_keyframes(target_obj, "location", 2, HandleTypeIsFree, False, False, f, False)

        
        # Z Axe
        
        if LookAtPosZ_Empty == True:
            
            FirstKeyframe = get_first_keyframe(target_obj, "location", 1)
            if FirstKeyframe:
                print(FirstKeyframe[1])
                f.write(struct.pack(">f", (FirstKeyframe[1]*-1) )) #nehme einzige keyframe in die canm
        
            else:
                print("Keine X-Positions-Keyframes gefunden.")
                f.write(struct.pack(">f", (target_obj.location[1]*-1) )) #nehme momentane pos in die CANM
            
        else:
        
            if LookAtPosZ_HandleType == "Symmetric":
                HandleTypeIsFree = False
            else:
                HandleTypeIsFree = True
            export_axis_keyframes(target_obj, "location", 1, HandleTypeIsFree, True, False, f, False)



        ### Kam Roll ###
        
        if KamRoll_Empty == True:
            
            FirstKeyframe = get_first_keyframe(target_obj, "rotation_euler", 0)
            if FirstKeyframe:
                print(FirstKeyframe[1])
                f.write(struct.pack(">f", ( (math.degrees(FirstKeyframe[1])) * -1) ) ) #nehme einzige keyframe in die canm
        
            else:
                print("Keine X-Positions-Keyframes gefunden.")
                f.write(struct.pack(">f", ( (math.degrees(target_obj.rotation_euler[0]) * -1 ) ))) #nehme momentane rotation in die CANM
            
        else:
        
            if KamRoll_HandleType == "Symmetric":
                HandleTypeIsFree = False
            else:
                HandleTypeIsFree = True
            export_axis_keyframes(target_obj, "rotation_euler", 0, HandleTypeIsFree, False, True, f, False) #0 für X-Achse, 1 für Y, 2 für Z
            
        
        ### FOV ###
        
        if KamFOV_Empty == True:
            
            FirstKeyframe = get_first_keyframe(bpy.context.object.data, "lens", 0)
            if FirstKeyframe:
                print(FirstKeyframe[1])
                f.write(struct.pack(">f", FirstKeyframe[1] )) #nehme einzige keyframe in die canm
        
            else:
                print("Keine X-Positions-Keyframes gefunden.")
                FovValue = math.degrees(bpy.context.object.data.angle)
                f.write(struct.pack(">f", FovValue)) #nehme momentane fov in die CANM

            
        else:
        
            if FOV_HandleType == "Symmetric":
                HandleTypeIsFree = False
            else:
                HandleTypeIsFree = True
                
            export_axis_keyframes(obj.data, "lens", 0, HandleTypeIsFree, False, False, f, True)
        
        
        
        #Ende des Frame  info Block:
        f.write(b"\x3D\xCC\xCC\xCD\x4E\x6E\x6B\x28")
        
        
        #Ende der Datei:
        f.write(b"\xFF\xFF\xFF\xFF")
        
        
        
        #Frame Info Block Size schreiben
        
        print(hex(f.tell()))
        print(f.tell())
        
        
        FrameInfoBlockSIZE = f.tell() - 136
        
        print(FrameInfoBlockSIZE)
        print(hex(FrameInfoBlockSIZE))
        
        
        f.seek(128)
        f.write(struct.pack(">i", FrameInfoBlockSIZE))
       
       
def CANMcreate(context):

    ## Look At Add
    bpy.ops.object.empty_add(type='SPHERE', radius=100)
    bpy.context.view_layer.objects.active.rotation_mode = 'XZY'
    bpy.context.view_layer.objects.active.name = "xxxTEMPLATExxx__CANM_LookAt"
    bpy.context.view_layer.objects.active.lock_scale[0] = True
    bpy.context.view_layer.objects.active.lock_scale[1] = True
    bpy.context.view_layer.objects.active.lock_scale[2] = True
    bpy.context.view_layer.objects.active.lock_rotation[1] = True
    bpy.context.view_layer.objects.active.lock_rotation[2] = True

    ## Camera Add
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', rotation=(0.00000000000000000000000, 0.00000000000000000000000, 0.00000000000000000000000))
    bpy.context.view_layer.objects.active.scale = 100,100,100
    bpy.context.view_layer.objects.active.name = "xxxTEMPLATExxx__CANM_CAMERA"
    bpy.context.view_layer.objects.active.data.clip_start = 6
    bpy.context.view_layer.objects.active.data.clip_end = 7.77778e+06
    bpy.context.view_layer.objects.active.data.sensor_fit = 'VERTICAL'
    bpy.context.view_layer.objects.active.data.sensor_height = 24
    bpy.context.view_layer.objects.active.data.angle = 0.785398
    bpy.context.view_layer.objects.active.data.type = 'PERSP'
    bpy.context.view_layer.objects.active.data.lens_unit = 'FOV'
    bpy.context.object.lock_rotation[0] = True
    bpy.context.object.lock_rotation[1] = True
    bpy.context.object.lock_rotation[2] = True
    bpy.context.object.lock_scale[0] = True
    bpy.context.object.lock_scale[1] = True
    bpy.context.object.lock_scale[2] = True
    bpy.context.object.location[0] = bpy.context.object.location[0] + 500

    bpy.ops.object.constraint_add(type='TRACK_TO')
    bpy.context.object.constraints["Track To"].target = bpy.data.objects["xxxTEMPLATExxx__CANM_LookAt"]
    bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
    bpy.context.object.constraints["Track To"].up_axis = 'UP_Y'
    bpy.context.object.constraints["Track To"].use_target_z = True
    bpy.context.object.constraints["Track To"].target_space = 'WORLD'
    bpy.context.object.constraints["Track To"].owner_space = 'WORLD'
    bpy.context.object.constraints["Track To"].influence = 1


    bpy.context.object["CANM Export Frames"] = 480
    bpy.context.object["CANM Filename"] = "StartScenario1"
    bpy.context.object["Export To SuperBlenderGalaxy"] = False


    #Rename
    bpy.data.objects["xxxTEMPLATExxx__CANM_CAMERA"].name = "Galaxy-CANM__Camera"
    bpy.data.objects["xxxTEMPLATExxx__CANM_LookAt"].name = "Galaxy-CANM__LookAt"
        
        


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
    bl_label = "Create Galaxy Camera" 
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
    
    
class GalaxyCANMexport(bpy.types.Operator):
    """Export selected Camera with track to modifier to CANM file"""
    bl_idname = "canm.galaxycanm_operator1" 
    bl_label = "Export CANM Keyframe file" 
    def execute(self, context):
        CANMexport(context)
        return {'FINISHED'}
        
class GalaxyCANMcreate(bpy.types.Operator):
    """Export selected Camera with track to modifier to CANM file"""
    bl_idname = "canm2.galaxycanm_operator2" 
    bl_label = "Create CANM Keyframe Camera" 
    def execute(self, context):
        CANMcreate(context)
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
        

        layout.label(text="Camera Actions")
        row = layout.row()
        row.scale_y = 1.2
        row.operator("objecto.galaxycam_operator2", icon='OUTLINER_OB_CAMERA') 
        

        if "Dpad Rotation Activated" in bpy.context.object:
            layout.label(text="Copy Camera as LaunchCamPlus Code")
            row = layout.row()
            row = layout.row()
            row.scale_y = 1.2
            row.operator("object.galaxycam_operator1", icon='CAMERA_DATA') 
            row = layout.row()
            row.scale_y = 1.2
            row.operator("objecti.galaxycam_operator3", icon='CAMERA_DATA') 
        
            
            layout.label(text="Camera Settings")
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
        
        else:
            layout.label(text="No valid Galaxy Camera Selected")
            layout.label(text="Select the cone")

        layout.label(text="-----------------")
        row = layout.row()
        row.scale_y = 1.2
        row = layout.row()
        row.scale_y = 1.2
       
        layout.label(text="CANM Keyframe Camera Tools")
        row = layout.row()
        row.scale_y = 1.2
        row.operator("canm2.galaxycanm_operator2", icon='CAMERA_DATA') 

        if "CANM Export Frames" in bpy.context.object:
            row = layout.row()
            row.scale_y = 1.2
            row.operator("canm.galaxycanm_operator1", icon='CAMERA_DATA')
            row = layout.prop(bpy.context.view_layer.objects.active, '["CANM Filename"]')
            row = layout.prop(bpy.context.view_layer.objects.active, '["CANM Export Frames"]')
            row = layout.prop(bpy.context.view_layer.objects.active, '["Export To SuperBlenderGalaxy"]')
        else:
            layout.label(text="No valid CANM Camera selected")
            layout.label(text="Select the camera object")


def register():
    bpy.utils.register_class(GalaxycamOperator1)
    bpy.utils.register_class(GalaxycamOperator2)
    bpy.utils.register_class(GalaxycamOperator3)
    bpy.utils.register_class(GalaxyCANMexport)
    bpy.utils.register_class(GalaxyCANMcreate)
    bpy.utils.register_class(LayoutSMGCameraPanel)
    
def unregister():
    bpy.utils.unregister_class(GalaxycamOperator1)
    bpy.utils.unregister_class(GalaxycamOperator2)
    bpy.utils.unregister_class(GalaxycamOperator3)
    bpy.utils.unregister_class(GalaxyCANMexport)
    bpy.utils.unregister_class(GalaxyCANMcreate)
    bpy.utils.unregister_class(LayoutSMGCameraPanel)
    
    


if __name__ == "__main__":
    register()
