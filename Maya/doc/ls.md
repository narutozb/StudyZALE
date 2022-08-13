# ls

命令返回场景中对象的名称（以及可选的类型名称）。

> Top
* [ls官方帮助文档](https://help.autodesk.com/cloudhelp/2023/CHS/Maya-Tech-Docs/CommandsPython/ls.html)
* 下载 [测试场文件](../resource/select_sample.mb)
* [如何下载测试文件](如何下载场景文件.md)
* 什么是长名字？(完整地址)


## 例文

执行例文前先执行以下导入模块代码
```pycon
import maya.cmds as cmds
```

简单的例子
### 获取列表示例1
```python
# joint1 和其内所有子物体
cmds.select('joint1', hi=True)

# 利用ls获取所选择物体的列表
sel_ls = cmds.ls(sl=True)

# 打印查看列表内容
for i in sel_ls:
    print (i)
```
结果
```
# joint1
# joint2
# joint3
# joint4
# joint5
```

### 获取列表示例2
选择并且获取所选物体列表。
```python
# |joint_test 和其内所有子物体
cmds.select('|joint_test', hi=True)

# 利用ls获取所选择物体的列表
sel_ls = cmds.ls(sl=True)

# 打印查看列表内容
for i in sel_ls:
    print (i)
```
结果
```
# |joint_test
# |joint_test|joint_test
# |joint_test|joint_test|joint_test
# |joint_test|joint_test|joint_test|joint_test
# |joint_test|joint_test|joint_test|joint_test|joint_test 
```