from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.core import NodePath
# from panda3d.core import CollisionNode
from panda3d.core import Vec3
import scene


class Collider(object):
    def __init__(self):
        # super().__init__('empty')

        self.entity = None
        self.node_path = None
        # self.collision_node = None
        # self.shape = None
    def make_collider(self):
        start, end = self.entity.model.getTightBounds()
        size = (end - start) / 2
        y = max(.01, size[1])
        z = max(.01, size[2])
        shape = BulletBoxShape(Vec3(size[0], y, z))
        # body = BulletRigidBodyNode('Bullet')
        # self.node_path = self.entity.attachNewNode(BulletRigidBodyNode('Bullet'))
        self.node_path = scene.render.attachNewNode(BulletRigidBodyNode('Bullet'))

        self.node_path.node().addShape(shape)
        # self.node_path.node().setMass(1.0)
        scene.world.attachRigidBody(self.node_path.node())
        print('added collider')


    def remove(self):
        self.collision_node.removeNode()


    # def __setattr__(self, name, value):
    #     super().__setattr__(name, value)
    #
    #     if name == 'rotation':
    #         try:
    #             # convert value from hpr to axis
    #             value = (value[2] , value[0], value[1])
    #             self.node_path.setHpr(value)
    #         except:
    #             pass
    #


        # if name == 'parent' and value != None:
        #     self.reparentTo(value)

    #         self.collision_node = value.model.attachNewNode(BulletRigidBodyNode('Bullet'))
    #
    #     if name == 'shape':
    #         if value == 'box':
    #             if self.parent.model:
    #                 min, max = self.parent.model.getTightBounds()
    #                 size = (max - min)
    #             else:
    #                 size = Vec3(1,1,1)
    #             self.shape = BulletBoxShape(size / 2)
    #             self.collision_node.node().addShape(self.shape)
    #
    #     if name == 'scale':
    #         pass
    #         # self.shape = BulletBoxShape(Vec3(value[0], value[1], value[2]))
    #         # self.setScale(value[0], value[1], value[2])
    #
    #
    #     if name == 'position' and self.collision_node:
    #         # if self.parent:
    #             # np = self.parent.attachNewNode(self)
    #         self.collision_node.setPos(value[0], value[1], value[2])