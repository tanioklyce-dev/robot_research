// ===========================================================================
// XLeRobot  ->  Intel RealSense D435i  mounting bracket
// Bolts to the camera's two front-face M3 holes (45 mm pitch) and presents a
// flat foot to the XLeRobot "last mounting link".
//
// Units: millimetres.  Frame: X = camera width, Y = depth (camera front face
// at Y=0, robot side at +Y), Z = up (camera bottom edge at Z=0).
//
// Render/export:  openscad -o d435i_bracket.stl d435i_bracket.scad
// (The shipped d435i_bracket.stl was generated from the defaults below.)
// ===========================================================================

/* [Camera interface] */
m3_pitch   = 45;    // FIXED: center-to-center of the two front M3 holes
m3_clear_d = 3.4;   // M3 clearance hole diameter (use 2.9 for self-tapping)
// *** VERIFY WITH CALIPERS *** height of the M3 holes above the camera's
// bottom edge. NOT published in the Intel datasheet; measure your unit.
cam_m3_z   = 17;

/* [Strap = camera-contact plate] */
strap_w = 64;   // width
strap_t = 4;    // thickness (front-to-back)
strap_h = 12;   // height (kept short so it clears the optics band)

/* [Foot = plate over the camera top, to the robot] */
foot_depth = 42;
foot_w     = 64;
foot_t     = 4;
gusset_depth = 22;

/* [Robot-side holes - ADAPT to the XLeRobot mounting link] */
robot_hole_d = 3.4;
robot_hole_x = 20;        // +/- X
robot_hole_y = [16, 32];  // Y positions (distance back from camera face)

$fn = 48;

hx  = m3_pitch / 2;
sz0 = cam_m3_z - strap_h/2;
sz1 = cam_m3_z + strap_h/2;
fz0 = sz1;
fz1 = sz1 + foot_t;

module gusset(xc) {
    // right triangle in the Y-Z plane, extruded 4 mm along X
    translate([xc, 0, 0])
      rotate([90, 0, 90])
        linear_extrude(height = 4)
          polygon([[strap_t, fz0],
                   [strap_t + gusset_depth, fz0],
                   [strap_t, sz0]]);
}

difference() {
    union() {
        // strap (vertical, against the camera front face)
        translate([-strap_w/2, 0, sz0]) cube([strap_w, strap_t, strap_h]);
        // foot (horizontal, over the camera top)
        translate([-foot_w/2, 0, fz0]) cube([foot_w, foot_depth, foot_t]);
        // side gussets
        gusset( strap_w/2 - 4);
        gusset(-strap_w/2);
    }
    // camera M3 holes (axis along Y)
    for (sx = [-hx, hx])
        translate([sx, -2, cam_m3_z])
          rotate([-90, 0, 0]) cylinder(d = m3_clear_d, h = strap_t + 4);
    // robot-side holes (axis along Z)
    for (ry = robot_hole_y, rx = [-robot_hole_x, robot_hole_x])
        translate([rx, ry, fz0 - 2])
          cylinder(d = robot_hole_d, h = foot_t + 4);
}
