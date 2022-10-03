import os
from pathlib import Path
from psd_tools import PSDImage



orig_ = r'D:\test_scenes\top\psd\test_psd.psd'

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
    save_path = os.path.join(orig_parent_dir_path,
                             f'{save_file_prefix}{group_name}{save_file_suffix}.{save_file_type}')
    layer.composite().save(save_path)
