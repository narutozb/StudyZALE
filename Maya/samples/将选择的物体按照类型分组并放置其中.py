import maya.cmds as cmds


def get_node_type(name):
    lr = cmds.listRelatives(name, c=True, shapes=True)
    if lr:
        node_type = cmds.nodeType(lr)
        return node_type
    else:
        node_type = cmds.nodeType(i)
        if node_type == 'joint':
            return 'joint'
        elif node_type == 'transform':
            return 'group'
        else:
            return node_type

# 创建一个字典
ref_dict = {}

# 获取选择的物体
sel = cmds.ls(sl=True)

# 创建参照字典
for i in sel:
    node_type = get_node_type(i)
    if not ref_dict.get(node_type):
        # 如果物体类型不在字典中，就创建一个列表。将物体类型作为key，并且将列表作为value。
        ref_dict[node_type] = []
    # 将物体添加到列表中
    ref_dict[node_type].append(i)

# 清空选择
cmds.select(cl=True)

# 遍历字典
for k, v in ref_dict.items():
    if not cmds.objExists(k):
        # 如果组不存在，就创建一个组
        cmds.group(n=k, em=True)

    # 将物体添加到组中
    cmds.parent(v, k)
