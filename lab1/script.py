# Original cornel_box scene
scene = OpenScene("./cornel_box0")

light_node = scene.GetNode("F000001")
light_node.light.name = "point_1"
light_node.light.kind = LightKind.LIGHT_POINT
light_node_transform = Transform()
light_node_transform.azim = 90
light_node_transform.tilt = 180
light_node_transform.rot = 180
light_node.tr = light_node_transform
light_node.Translate(278000, -279500, 548700)

LoadScene(scene)

# IMAPS
kernel = GetKernel()
imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 60
kernel.CalculateIMaps()

# Render
params = scene.RenderParams()
params.time_limit  = 60
params.store_lum = True
params.path = "cornel_box0_map_ill"
kernel.Render()

scene.Save("cornel_box0_map_ill", OverwriteMode.OVERWRITE)

# ----------------------------------------------------------------------------------------------------

# Scene with direction light

scene = OpenScene("./cornel_box0_map_ill")

light_node = scene.GetNode("F000001")
light_node.light.name = "point_1"
light_node.light.kind = LightKind.LIGHT_POINT
light_node.light.gonio = IesGonio("./NewGonio.ies")
light_node_transform = Transform()
light_node_transform.azim = 90
light_node_transform.tilt = 0
light_node_transform.rot = 0
light_node.tr = light_node_transform
light_node.targ_dist = 548700
light_node.Translate(278000, -279500, 548700)

LoadScene(scene)

# IMAPS
kernel = GetKernel()
imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 60
kernel.CalculateIMaps()

# Render
params = scene.RenderParams()
params.time_limit  = 60
params.store_lum = True
params.path = "cornel_box0_map_ill_dir"
kernel.Render()

scene.Save("cornel_box0_map_ill_dir", OverwriteMode.OVERWRITE)

# ----------------------------------------------------------------------------------------------------

# Scene with sphere 

scene = OpenScene("./cornel_box0_map_ill_dir")

SphereClass = GetClass(Shape, 'Sphere')
sphere = SphereClass(name = "mySphere", radius = 70)
sphere.parts[0].surf_attrs.front_side.kd = 0
sphere.parts[0].surf_attrs.front_side.ktd = 1
sphere.parts[0].surf_attrs.front_side.kd_color = BWSurfColor(1)
sphere.parts[0].front_medium = scene.GetMedium('env')
sphere.parts[0].back_medium = scene.GetMedium('env')
sphere_node = MeshNode(sphere, name = "Sphere")
sphere_transform = XYZTransform()
sphere_transform.pos = (278000, -279500, 548700)
sphere_node.tr = sphere_transform

scene.AddNode(sphere_node)

LoadScene(scene)

# IMAPS
kernel = GetKernel()
imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 60
kernel.CalculateIMaps()

# Render
params = scene.RenderParams()
params.time_limit  = 60
params.store_lum = True
params.path = "cornel_box0_map_ill_dir_sphere"
kernel.Render()

scene.Save("cornel_box0_map_ill_dir_sphere", OverwriteMode.OVERWRITE)

# ----------------------------------------------------------------------------------------------------

# Scene with subdivision parameters

scene = OpenScene("./cornel_box0_map_ill_dir_sphere")

scene.SetSubdivision(use_subd = True, rel_step = 0.01)

LoadScene(scene)

# IMAPS
kernel = GetKernel()
imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 60
kernel.CalculateIMaps()

# Render
params = scene.RenderParams()
params.time_limit  = 60
params.store_lum = True
params.path = "cornel_box0_map_ill_dir_sphere_sub"
kernel.Render()

scene.Save("cornel_box0_map_ill_dir_sphere_sub", OverwriteMode.OVERWRITE)

# ----------------------------------------------------------------------------------------------------

# Scene with Gauss reflection

scene = OpenScene("./cornel_box0_map_ill_dir_sphere_sub")

brs_0 = scene.GetNode("brs_0")
brs_0.shape.parts[0].surf_attrs.front_side.kd = 0
brs_0.shape.parts[0].surf_attrs.front_side.gr_val = 1
brs_0.shape.parts[0].surf_attrs.front_side.gr_ang = 5

brs_1 = scene.GetNode("brs_1")
brs_1.shape.parts[0].surf_attrs.front_side.kd = 0
brs_1.shape.parts[0].surf_attrs.front_side.gr_val = 1
brs_1.shape.parts[0].surf_attrs.front_side.gr_ang = 5

brs_2 = scene.GetNode("brs_2")
brs_2.shape.parts[0].surf_attrs.front_side.kd = 0
brs_2.shape.parts[0].surf_attrs.front_side.gr_val = 1
brs_2.shape.parts[0].surf_attrs.front_side.gr_ang = 5

brs_3 = scene.GetNode("brs_3")
brs_3.shape.parts[0].surf_attrs.front_side.kd = 0
brs_3.shape.parts[0].surf_attrs.front_side.gr_val = 1
brs_3.shape.parts[0].surf_attrs.front_side.gr_ang = 5

sphere_node = scene.GetNode("Sphere")
sphere_node.SimHide()

LoadScene(scene)

# IMAPS
kernel = GetKernel()
imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 60
kernel.CalculateIMaps()

# Render
params = scene.RenderParams()
params.time_limit  = 60
params.store_lum = True
params.path = "cornel_box0_map_ill_dir_gauss"
kernel.Render()

# Path Tracing
pt_params = scene.PTRenderParams()
pt_params.time_limit  = 60
pt_params.store_lum = True
pt_params.path = "cornel_box0_map_ill_dir_gauss_pt"
kernel.PTRender()

scene.Save("cornel_box0_map_ill_dir_gauss", OverwriteMode.OVERWRITE)