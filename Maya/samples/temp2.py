import maya.cmds as cmds

#
all_info = {}

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

    all_info[j] = transform

# 打印测试. 不需要纠结语法，只是展示这个字典里面的内容
for k in all_info:
    transform = all_info[k]
    print ('Joint Name:\n\t'+k)

    print ('\tTranslation:\n\t\t'+','.join(map(str, transform[0])))
    print ('\tRotation:\n\t\t' + ','.join(map(str, transform[1])))
    print ('\tScale:\n\t\t' + ','.join(map(str, transform[2])))
    print ('-'*50)
