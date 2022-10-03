import os
from pathlib import Path
from psd_tools import PSDImage




def export_psd_group_to(orig_=None):


    NORMAL_EXPORT_NAME_LIST = ['C', 'N', 'ORM', 'shellMask']


    orig_short_file_name, orig_suffix = os.path.splitext(os.path.basename(orig_))
    orig_parent_dir_path = Path(orig_).parent.parent.absolute()

    psd = PSDImage.open(orig_)
    save_file_type = 'png'

    save_file_prefix = ''
    save_file_suffix = ''

    for layer in psd:
        if not layer.visible:
            layer.visible = True

        group_name = layer.name
        if group_name not in NORMAL_EXPORT_NAME_LIST:
            continue

        save_path = os.path.join(orig_parent_dir_path,
                                 f'{save_file_prefix}{orig_short_file_name}_{group_name}{save_file_suffix}.{save_file_type}')
        layer.composite().save(save_path)



#------------------------------------------------
# for root,dirs, files in os.walk(r'D:\test_scenes\top'):
#     for file in files:
#         short_name, suffix = os.path.splitext(file)
#         if suffix == '.psd':
#             orig_file_path = os.path.join(root,file)
#             export_psd_group_to(orig_file_path)





def get_psd_infos(orig_=None):


    NORMAL_EXPORT_NAME_LIST = ['C', 'N', 'ORM', 'shellMask']
    LAYER_INFOS_REFERENCE = {
        'Name': [],
        'IsVisible': [],
        'Type?': [],
        'Size?': [],
        'ParentName?': [],
        'HasMask?': [],
        'HasEffect?': [],
    }

    psd = PSDImage.open(orig_)

    for layer in psd:
        group_name = layer.name
        if group_name not in NORMAL_EXPORT_NAME_LIST:
            continue
        LAYER_INFOS_REFERENCE.get('Name').append(layer.name)
        LAYER_INFOS_REFERENCE.get('IsVisible').append(str(layer.is_visible()))
        LAYER_INFOS_REFERENCE.get('Type?').append(layer.kind)
        # 如果不显示图层则无法判断图层大小
        if not layer.visible:
            layer.visible = True
        LAYER_INFOS_REFERENCE.get('Size?').append(layer.size)
        LAYER_INFOS_REFERENCE.get('ParentName?').append(layer.parent.name)
        LAYER_INFOS_REFERENCE.get('HasMask?').append(layer.has_mask())
        LAYER_INFOS_REFERENCE.get('HasEffect?').append(layer.has_effects())

    return LAYER_INFOS_REFERENCE





