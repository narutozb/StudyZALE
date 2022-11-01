import os

ROOT_PATH = r'D:\test'
STRUCT_REFERENCE = {
    'FBX': [],
    'Scene': ['model', 'mot', 'rig'],
    'Source': [],
}


def create_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    else:
        pass


def create_folder_by_reference(character_name='xxx'):
    """

    :param character_name:角色名字
    :return:
    """
    # Set Character root path
    character_root_path = os.path.join(ROOT_PATH, character_name)

    for k in STRUCT_REFERENCE:
        f1 = k
        f1_values = STRUCT_REFERENCE.get(f1)
        f1_path = os.path.join(character_root_path, f1)
        create_folder(f1_path)

        if len(f1_values) > 0:
            for f2_name in f1_values:
                f2_path = os.path.join(f1_path, f2_name)
                create_folder(f2_path)


def create_folder_by_character_list(character_list):
    for name in character_list:
        create_folder_by_reference(character_name=name)


create_folder_by_character_list(['xxx', 'character1', 'character2', 'character3'])
