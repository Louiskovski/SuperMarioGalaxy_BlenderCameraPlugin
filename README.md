# Super Mario Galaxy - Blender Camera Plugin
Blender plugin with useful functions for *Super Mario Galaxy 2* cameras like copying a camera as code to paste into [LaunchCamPlus](https://github.com/SuperHackio/LaunchCamPlus) (version 2.5.0.0).

Currently only for the commonly used *XY PARA* type.

Planned for new versions are among others the types *POINT FIX* and *TOWER* as well as the possibility to copy cameras from LaunchCamPlus into Blender.




# How to use it

After installing the plugin, you can find it in the 3D view on the right under the *Misc* tab.

Click on *Add Camera* to create the objects needed to create a camera:

- The cone corresponds to the position of Mario or the focused object. Its object name will be used for the Camera ID
- The sphere is responsible for the rotation and the offsets
- The camera itself is only responsible for the zoom and the FoV (Field of View)


Simply adjust the rotation and position of the sphere and camera object as required. Simply view the camera actively in the 3D view to get exactly the viewing angle that will be used in the game.


Tip: Use one 3D view for positioning and another with the camera active. You can then also move the cone in the active camera to see how Mario would move with this camera.


Give the cone object the camera ID or name to be used (example: c:0000).



When you are happy with the camera, select the cone object and click on “XY PARA” under Copy Camera Code in the plugin. In LaunchCamPlus you can now insert the camera by pressing *CTRL + V*.
