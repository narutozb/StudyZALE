import re
import maya.cmds as cmds
import pymel.core as pm

def get_startup_cameras():
    return [camera.getParent() for camera in pm.ls(type=('camera'), l=True) if pm.camera(camera.parent(0), startupCamera=True, q=True)]

def renamer(func):
    def wrapper(*args,**kwargs):
        '''

        :param args:
        :param kwargs:
        :return:
        '''
        result = {}

        #
        # {'mesh': {'type': ['mesh'] or 'mesh', 'new_name': 'i', 'prefix': 'aa_', 'suffix': '_mesh',
        #                              'allow_stacking_prefix': False, 'allow_stacking_suffix': False}}
        #
        type_reference = kwargs.get('type_reference')

        for k in type_reference:
            type_name = k
            type = type_reference.get(type_name).get('type')
            prefix = type_reference.get(type_name).get('prefix')
            suffix = type_reference.get(type_name).get('suffix')
            allow_stacking_prefix = type_reference.get(type_name).get('allow_stacking_prefix')
            allow_stacking_suffix = type_reference.get(type_name).get('allow_stacking_suffix')
            new_name = type_reference.get(type_name).get('new_name')

            for i in pm.ls(type=type,readOnly=False):
                obj = i
                if is_shape(obj):
                    obj = i.getParent()
                else:
                    pass

                rename_object(
                    obj = obj, prefix=prefix, suffix=suffix, new_name=new_name,
                    allow_stacking_prefix=allow_stacking_prefix,allow_stacking_suffix=allow_stacking_suffix,type_name=type_name,
                )


        return func(*args,**kwargs)
    return wrapper

def authenticate_obj(func):
    def wrapper(*args, **kwargs):
        obj = kwargs.get('obj')

        if obj in get_startup_cameras():
            return

        if kwargs.get('type_name') == 'group':
            if is_group(obj):
                pass
            else:
                return

        return func(*args, **kwargs)
    return wrapper


@authenticate_obj
def rename_object(obj=None, suffix='', prefix='', new_name='', allow_stacking_prefix=False, allow_stacking_suffix=False,**kwargs):
    r = re.compile(r'^[a-zA-Z0-9_]+$')
    match = filter(r.match, [suffix,new_name,prefix])

    long_name = obj.longName()

    if not match:
        return 'This is an unacceptable name'

    short_name = long_name.split('|')[-1]

    if not allow_stacking_suffix:
        match_suffix = re.match(r'.*%s$'%suffix, short_name)
        if match_suffix:
            suffix = ''

    if not allow_stacking_prefix:
        match_prefix = re.match(r'^%s.*'%prefix, short_name)
        if match_prefix:
            prefix = ''

    if len(new_name)>0:
        new_name = '%s%s%s'%(prefix,new_name,suffix)
    else:
        new_name = '%s%s%s'%(prefix,short_name,suffix)

    cmds.rename(long_name, new_name)

    return new_name

@renamer
def rename_objects_by_type(*args,**kwargs):
    pass

def is_shape(obj):
    parent = obj.getParent()
    if parent:
        if parent.getShape():
            return True
        else:
            return
    else:
        return

def is_group(obj):
    children = obj.getChildren()
    if obj.__class__ != pm.nodetypes.Transform:
        return False
    for child in children:
        if child.__class__ != pm.nodetypes.Transform:
            return False
    return True



aa = rename_objects_by_type(
    type_reference={
        'mesh': {'type': 'mesh', 'new_name':'', 'prefix': 'aa_', 'suffix': '_mesh', 'allow_stacking_prefix': False, 'allow_stacking_suffix': False},
        'camera':{'type': 'camera', 'new_name':'', 'prefix': 'ca_', 'suffix': '_cam', 'allow_stacking_prefix': False, 'allow_stacking_suffix': False},
        'light': {'type': 'light', 'new_name': '', 'prefix': 'light_', 'suffix': '_lit','allow_stacking_prefix': False, 'allow_stacking_suffix': False},
        'nurbsCurve': {'type': 'nurbsCurve', 'new_name': '', 'prefix': 'cv_', 'suffix': '_c','allow_stacking_prefix': False, 'allow_stacking_suffix': False},
        'locator': {'type': 'locator', 'new_name': '', 'prefix': 'locator_', 'suffix': '_lc','allow_stacking_prefix': False, 'allow_stacking_suffix': False},
        'joint': {'type': 'joint', 'new_name': '', 'prefix': '', 'suffix': '_jnt','allow_stacking_prefix': False, 'allow_stacking_suffix': False},
        'group': {'type': 'transform', 'new_name': '', 'prefix': 'group_', 'suffix': '_grp','allow_stacking_prefix': False, 'allow_stacking_suffix': False},
    }
)


import pymel.core as pm

template = uiTemplate('ExampleTemplate', force=True)
template.define(button, width=100, height=40, align='left')
template.define(frameLayout, borderVisible=True, labelVisible=False)

# with pm.window(menuBar=True, menuBarVisible=True) as win:
#     with


