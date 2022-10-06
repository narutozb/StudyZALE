import os
from pathlib import Path
from psd_tools import PSDImage


def export_psd_group_to_dec(func):
    def dec(*args, **kwargs):
        if not kwargs.get('save_file_type'):
            kwargs['save_file_type'] = 'png'

        return func(*args, **kwargs)

    return dec


@export_psd_group_to_dec
def export_psd_group_to(psd_path=None, save_file_type=None, export_to=None, save_path=None):
    """

    :param save_path:当 export_to的SpecificFolder被激活时，需要输出保存地址。
    :param psd_path:
    :param save_file_type:'jpg' or 'tga' or 'png'
    :param export_to:
        ParentFolder-父级文件夹
        CurrentFolder-当前文件所在的文件夹
        SpecificFolder-特定文件夹。 当此选项被选中时，需要输入specific_path。

    :return:
    """
    NORMAL_EXPORT_NAME_LIST = ['C', 'N', 'ORM', 'shellMask']

    orig_short_file_name, orig_suffix = os.path.splitext(os.path.basename(psd_path))
    parent_folder = Path(psd_path).parent.parent.absolute()
    current_folder = Path(psd_path).parent.absolute()

    if export_to == 'ParentFolder':
        save_path = parent_folder

    elif export_to == 'CurrentFolder':
        save_path = current_folder

    elif export_to == 'SpecificFolder':
        if os.path.isdir(save_path):
            pass
        else:
            raise 'Path is not correct!!!'
    # if export_to == None or else
    else:
        save_path = current_folder

    psd = PSDImage.open(psd_path)

    save_file_prefix = ''
    save_file_suffix = ''

    for layer in psd:
        if not layer.visible:
            layer.visible = True

        group_name = layer.name
        if group_name not in NORMAL_EXPORT_NAME_LIST:
            continue

        _save_path = os.path.join(save_path,
                                  f'{save_file_prefix}{orig_short_file_name}_{group_name}{save_file_suffix}.{save_file_type}')

        if save_file_type.lower() == 'jpg':
            layer.composite().convert('RGB').save(_save_path)
        else:
            layer.composite().save(_save_path)



# # ------------------------------------------------
# for root, dirs, files in os.walk(r'D:\test_scenes\top'):
#     for file in files:
#         short_name, suffix = os.path.splitext(file)
#         if suffix == '.psd':
#             orig_file_path = os.path.join(root, file)
#             export_psd_group_to(psd_path=orig_file_path, save_file_type='jpg')
# #

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
