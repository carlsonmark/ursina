import sys
sys.path.append("..")
from pandaeditor import *
import os
from panda3d.bullet import BulletDebugNode

class Editor(Entity):

    def __init__(self):
        super().__init__()
        self.name = 'editor'
        self.is_editor = True
        self.parent = scene.ui.entity
        self.editor_camera = load_script('scripts.editor_camera')
        self.editor_camera.position = (0, -100, 0)
        scene.editor_camera = self.editor_camera

        self.camera_pivot = Entity()
        self.camera_pivot.is_editor = True
        camera.parent = self.camera_pivot

        self.transform_gizmo = Entity()
        self.transform_gizmo.is_editor = True
        self.transform_gizmo.model = 'cube'
        self.transform_gizmo.scale = (.1, .1, .1)
        self.transform_gizmo.add_script('transform_gizmo')
        scene.entities.append(self.transform_gizmo)


        self.grid = load_prefab('panel')
        self.grid.name = 'grid'
        self.grid.parent = scene
        self.grid.position = (10, 0, 0)
        self.grid.rotation = (-90, 0, 0)
        self.grid.scale = (10, 10, 10)
        self.grid.collision = True
        # self.grid.collider = 'box'
        self.grid.button_script = self.add_script('button')
        self.grid.button_script.color = color.gray
        self.grid.color = color.lime


        toolbar = load_prefab('panel')
        toolbar.name = 'toolbar'
        toolbar.parent = self
        toolbar.origin = (0, 0, .5)
        toolbar.position = (0, 0, .485)
        toolbar.scale = (1, 1, .025)
        toolbar.color = color.gray

        for i in range(4):
            button = load_prefab('button')
            button.name = 'toolbar button'
            button.parent = toolbar
            button.origin = (-.5, 0, .5)
            button.position = (-.487 + (i * .061), 0, 0)
            button.scale = (.06, 1, 1)
            button.color = color.orange
            # button.text = 'button'
            # button.text.color = color.black


        sidebar = load_prefab('panel')
        sidebar.name = 'sidebar'
        sidebar.parent = self
        sidebar.origin = (-.5, 0, -0.0)
        sidebar.position = (-.5, 0, 0)
        sidebar.scale = (.04, 1, .9)
        # sidebar.color = color.gray
        sidebar.color = color.black33
        # test.color = hsv_color(210, 1, 1)
        # print(color.hsv_color(90, 1, 1))

        self.scene_list = load_prefab('panel')
        self.scene_list.name = 'scene_list'
        self.scene_list.parent = self
        self.scene_list.scale = (.4, 1, .5)
        self.scene_list.color = color.black33
        self.scene_list.visible = False

        self.model_list = load_prefab('panel')
        self.model_list.name = 'model_list'
        self.model_list.scale = (.4, 1, .5)
        self.model_list.color = color.black33
        self.model_list.visible = False

    #     text = load_prefab('text')
    #     text.parent = self.scene_list
    #     text.position = (0, -.1, 0)
    #     text.scale = (.9,.9,.9)
    #     t = 'test text'
    # #     t = '''zxcvb nmasd ghj qwetyutuoi phklz xcvbnma sdghjqwetyutuo iphkl xcvbnm
    # # asdgh jqwetyu tuoiphklzxcv bnma s ghjqw et yutu oiph klzxcvbnm asdgh jqwe tyut uoi phkl
    # # zxcvb nmasd ghj qwetyutuoi phklz xcvbnma sdghjqwetyutuo iphkl xcvbnm
    # # asdgh jqwetyu tuoiphklzxcv bnma s ghjqw et yutu oiph klzxcvbnm asdgh jqwe tyut uoi phkl
    # # zxcvb nmasd ghj qwetyutuoi phklz xcvbnma sdghjqwetyutuo iphkl xcvbnm
    # # asdgh jqwetyu tuoiphklzxcv bnma s ghjqw et yutu oiph klzxcvbnm asdgh jqwe tyut uoi phkl'''
    #     text.text = t
    #     # text.color = color.blue


        self.texture_list = load_prefab('filebrowser')
        # self.texture_list.collider = 'box'
        self.texture_list.parent = self
        # self.texture_list.scale = (1, 1, 1)
        self.texture_list.visible = False
        # print(scene.asset_folder)
        self.texture_list.file_types = ('.png', '.jpg', '.psd', '.gif')
        self.texture_list.path = os.path.join(os.path.dirname(scene.asset_folder), 'textures')


        self.entity_list = load_prefab('entity_list')
        self.entity_list.parent = self
        # self.entity_list.populate()

        # 2D / 3D toggle
        self.2d_button = load_prefab('button')
        self.2d_button.parent = self
        self.2d_button.name = '2d_button'
        self.2d_button.text = '2D'
        self.2d_button.position = (.1, 0)


    def input(self, key):
        if key == 'i':
            self.entity_list.populate()

        if key == 'h':
            self.show_colliders = not self.show_colliders
            if self.show_colliders:
                self.debugNP.show()
            else:
                self.debugNP.hide()

        if key == 'tab':
            # print(inspect.currentframe().f_back.f_locals['self'])
            self.visible = not self.visible
            if self.visible:
                camera.position = self.editor_camera.position
                for e in scene.entities:
                    e.show()
                    if not e.is_editor:
                        e.editor_collider = 'box'
                        e.collider.stash()
                        e.collider.node_path.show()
            else:
                self.editor_camera.position = camera.position
                for e in scene.entities:
                    e.editor_collider = None
                    e.collider.unstash()



        if self.visible:
            self.editor_camera.input(key)

        if key == 's':
            self.scene_list.visible = True
        if key == 's up':
            self.scene_list.visible = False
        if key == 'm':
            self.model_list.visible = True
        if key == 'm up':
            self.model_list.visible = False
        if key == 't':
            self.texture_list.visible = True
        if key == 't up':
            self.texture_list.visible = False
