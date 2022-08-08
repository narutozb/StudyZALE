# select

> Top
* [select官方帮助文档](https://help.autodesk.com/cloudhelp/2023/CHS/Maya-Tech-Docs/CommandsPython/select.html)
* 下载 [测试场文件](../resource/select_sample.mb)
* [如何下载测试文件](如何下载场景文件.md)

## 例文

执行例文前先执行以下导入模块代码
```pycon
import maya.cmds as cmds
```

在不添加任何指定参数时，可用一下方法选中物体。

```python
# 选中所有
cmds.select('*')

# 选择 pCube1
cmds.select('pCube1')

# 选择 pCube1,pCube2,pCube3

cmds.select('pCube1','pCube2','pCube3')

cmds.select(['pCube1','pCube2','pCube3'])

# 选中 名字中带有pCube的物体
cmds.select('pCube*')
```

```python
# 选中 joint1,joint2,joint3
cmds.select(['joint1','joint2','joint3'])
```

### add

> Indicates that all deletable root level dag objects and all deletable non-dag dependency nodes should be selected.
> 可简单的理解为加选物体

```python
# 选择 pCube1,pCube2,pCube3
cmds.select('pCube1')
cmds.select('pCube2', add=True)
cmds.select('pCube3', add=True)

# 或者
cmds.select('pCube1')
cmds.select(['pCube2','pCube3'],add=True)
```

### all

> Indicates that all deletable root level dag objects and all deletable non-dag dependency nodes should be selected.
> 
> 在Maya中有一些物体是不可以被删除的。例如，打开或者新建场景时自带的摄像机节点。persp, top, front, side。
> 利用此参数可以选择所有不可被删除的根节点。

```python
cmds.select(all=True)
```

### clear

> Clears the active list. This is more efficient than "select -d;". Also "select -d;" will not remove sets from the active list unless the "-ne" flag is also specified.
> 可理解为解除选择，或者意为取消选择。

```python
# 取消选择。测试或者学习时请逐行执行代码。
cmds.select(all=True)
cmds.select(cl=True)
```

### deselect
> Indicates that the specified items should be removed from the active list if they are on the active list.
> 取消选择某个或某些特定物体。

```python
cmds.select(all=True)
cmds.select(['joint1','light_group'],deselect=True)
```


### hierarchy
> Indicates that all children, grandchildren, ... of the specified dag objects should also be selected.
> 此选项为True时，被选择的物体连同其所有子物体都会被选中。

```python
# 选中 joint1和其所有子物体
cmds.select('joint1', hi=True)
```

### replace
> Indicates that the specified items should replace the existing items on the active list.
> 通常来说，结果与不填加此选项一样。

```python
# 选择所有名字中带 pCube 的物体。
cmds.select('pCube*',replace=True)

# 效果与此命令一样
cmds.select('pCube*')
```

### visible
> Indicates that of the specified items only those that are visible should be affected.
> 只有没被隐藏的物体才会被选中。

```python
# 选择名字中带有 pCube 的物体，并且其不是被隐藏的物体。
cmds.select('pCube*', visible=True)
```


## 更多例文和活用

### 情况1

> 选择名字以 pCube 开始的物体，并且其结尾的数字必须为偶数。
> pCube2,pCube4,pCube6,...

### 方法1
```python
object_list = ['pCube2', 'pCube4', 'pCube6', 'pCube8', 'pCube10', 'pCube12', 'pCube14', 'pCube16', 'pCube18', 'pCube20', 'pCube22', 'pCube24']
cmds.select(object_list)
```

### 方法2
```python
cmds.select('pCube2')
cmds.select(['pCube4', 'pCube6', 'pCube8', 'pCube10', 'pCube12', 'pCube14', 'pCube16', 'pCube18', 'pCube20', 'pCube22', 'pCube24'],add=True)
```

### 方法3
```python
# 避免执行命令之前已经选择物体。执行此命令取消选择。
cmds.select(cl=True)
# 
for i in range(1,25):
    if i%2 == 0:
        cmds.select('pCube'+str(i),add=True)
```

### 情况2
选择 light_group1 组中的所有子物体。

#### 方法1
```python
cmds.select('light_group1', hi=True)
cmds.select('light_group1', deselect=True)
```

#### 方法2
```python
cmds.select('light_group1|*')
```






