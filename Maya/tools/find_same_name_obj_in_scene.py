import os
import re
import pymel.core as pm
import maya.cmds as cmds

ALL_SAME_OBJ_SCENE = {}


def filter_mesh_obj(func):
    def dec(obj, suffix=None, auto_suffix=True, *args, **kwargs):
        suffix = kwargs.get('suffix')
        template_suffix_spliter = kwargs.get('template_suffix_spliter') or '_'

        if len(obj.getChildren(shapes=True)) > 0:
            if auto_suffix:
                suffix = '%s%s' % (template_suffix_spliter, obj.getChildren(shapes=True)[0].__class__.__name__)

            # rename
            short_short_name = obj.name().split('|')[-1]
            obj.rename('%s%s' % (short_short_name, suffix))

    return dec


@filter_mesh_obj
def rename_same_mesh_name():
    pass


def check_one_scene_same_obj():

    all_same_obj_name = []

    transforms_obj_list = pm.ls(transforms=True, readOnly=False)

    all_transforms_lower_name_list = [i.split('|')[-1].lower() for i in cmds.ls(transforms=True, readOnly=False)]
    same_name_lower_name_list = list(
        set(i for i in all_transforms_lower_name_list if all_transforms_lower_name_list.count(i) > 1))

    scene_path = cmds.file(q=True, sn=True)

    if len(same_name_lower_name_list) > 0:
        ALL_SAME_OBJ_SCENE[scene_path] = True


def check_all_scene_same_obj(root_directory):
    for root, dirs, files in os.walk(root_directory):
        # re.match('',files)
        print()




# for i in transforms_obj_list:
#     if i.__class__.__name__ == 'Joint':
#         continue
#
#     short_short_name = i.name().split('|')[-1]
#
#     if short_short_name.lower() in same_name_lower_name_list:
#         rename_same_mesh_name(i)
