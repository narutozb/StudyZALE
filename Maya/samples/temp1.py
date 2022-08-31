import maya.cmds as cmds

# 所有骨骼的自定义transform情报
all_info_list = []

# 遍历骨骼获取每一个骨头的translation，rotation，scale
for j in cmds.ls(type='joint'):
    translation = [
        cmds.getAttr(j + '.tx'),
        cmds.getAttr(j + '.ty'),
        cmds.getAttr(j + '.tz'),
    ]

    rotation = [
        cmds.getAttr(j + '.rx'),
        cmds.getAttr(j + '.ry'),
        cmds.getAttr(j + '.rz')
    ]

    scale = [
        cmds.getAttr(j + '.sx'),
        cmds.getAttr(j + '.sy'),
        cmds.getAttr(j + '.sz')
    ]

    # 合并translation rotation scale 到一个列表中
    transform = [translation, rotation, scale]

    # 添加到总列表中
    all_info_list.append(transform)

# 打印测试
for i in all_info_list:
    print (i)