# select

下载 [测试场文件](../resource/base_test_scene.mb)

执行例文前先执行以下导入模块代码
```pycon
import maya.cmds as cmds
```

## 常用的参数

在不添加任何指定参数时，可用一下方法选中物体。

```python
# 选择 pCube1
cmds.select('pCube1')

# 选择 pCube1,pCube2,pCube3 有以下两种方法

cmds.select('pCube1','pCube2','pCube3')

cmds.select(['pCube1','pCube2','pCube3'])

# 选中 名字中带有pCube的物体
cmds.select('pCube*')
```


### add

> 加选物体

```python
cmds.select()


```

### all


### clear


### hierarchy


### replace


### visible




