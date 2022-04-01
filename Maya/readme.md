# 常见的问题解决

此页面包含了各种疑难杂症的解决方案，一点也不难。
本页面各种说明适用于Maya2018或以上版本。

## 专业术语

> 建模类型
+ [多边形(Polygon)](https://help.autodesk.com/view/MAYAUL/2020/CHS/?guid=GUID-7941F97A-36E8-47FE-95D1-71412A3B3017)
+ [曲面(NURBS)](https://help.autodesk.com/view/MAYAUL/2020/CHS/?guid=GUID-735A0B9A-2180-4FB8-9A7B-68F21F306E97)
虽然这两种建模方式都有自己的优缺点，但目前绝大多数工作室或公司都会使用多边形建模。

> 高模

通过[平滑](https://help.autodesk.com/view/MAYAUL/2020/CHS/?guid=GUID-DF6EC285-5436-4FF1-A402-3498014BDE74)(Smooth)或者加线等方式提高模型的平滑度或者细节。

![](https://help.autodesk.com/cloudhelp/2020/CHS/Maya-GettingStarted/images/GUID-5439DA76-275B-4830-B5BA-4A8983B8B286.png)

> 法线

简而言之，法线就是确定模型（面）的正面或背面的参考线。如果法线面反向你则你看到的面为灰白色（受光面），如果法线背对你则你看到的面便是黑色的（不受光）。

![](https://github.com/narutozb/StudyZALE/blob/master/Maya/images/%E9%9D%A2%E6%B3%95%E7%BA%BF_%E6%AD%A3%E5%8F%8D%E9%9D%A2%E5%AF%B9%E6%AF%94.PNG?raw=true)

[学习更多关于法线的知识。](https://help.autodesk.com/view/MAYAUL/2020/CHS/?guid=GUID-9C257D44-924D-4B3F-ADEF-C71FAA98EAB1)

> UV
> 贴图
> 材质
> 渲染
> 绑定
> 动画
> FBX
> MA
> MB
> 

## 初级

### Q&A
+ 如何切换Maya的显示语言?
+ [什么是大纲视图?（Outliner）](https://help.autodesk.com/view/MAYAUL/2020/CHS/?guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406)
+ [调整窗口的背景颜色（Viewport Background Color）](https://knowledge.autodesk.com/zh-hans/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2022/CHS/Maya-Basics/files/GUID-E506209A-CCCD-4886-86EB-0F7825F3003B-htm.html)
+ 如何切换各种视图模式?
+ 为什么模型的面黑了？(法线反了？材质半透明？)
+ 菜单栏里的按钮后面的方盒子是什么？(Options)
+ 节点编辑器在哪里？(Node Editor)
+ 设置场景单位(米，厘米，帧速率)
+ 中心点偏了怎么办？(看不见了？)
+ 物体消失了怎么查看它在哪？
+ (整个场景)全黑了怎么办？
+ 菜单没了怎么办？(shelf, Status Line)
+ 属性编辑器在哪？(Attribute Editor)
+ 通道编辑器在哪？(Channel Box)



### 操作
+ 如何选择物体 
  - 如何初始化选择选项
+ 如何隐藏物体
+ 如何初始化移动选项
+ 如何初始化旋转选项
+ 如何初始化缩放选项
+ 如何选择点(多边形)
+ 如何选择边(多边形)
+ 如何选择面(多边形)
+ 查看多边形的顶点

## 建模

+ 多边形(Mesh)
  - 倒角(Bevel)
  - 桥接(Bridge)
  - 挤出(Extrude)
  - 平滑(Smooth)
  - 合并(Combine)
  - 分离(Sparate)
+ 优化和清理(Cleanup)
+ 传递属性(Transfer Attributes)
+ UV

## 材质
+ 材质编辑器
+ 材质类型
  - Lambert
  - Blinn
  - Phong
  - SurfaceShader
  - RampShader
+ 如何给多边形添加材质

## 绑定
+ 骨骼
+ 权重
+ 控制器
+ 变形器
+ Cluster
+ FK
+ IK
+ HumanIK

## 渲染
+ 灯光
  - 点光源
  - 面光源
  - 平行光源
  - 体积光源
+ 渲染器
  - Maya Software
    - 渲染设置 
  - Arnold Renderer
    - 渲染设置  
  - vRay
    - 渲染设置 

## 特效
+ 流体
+ nCloth
+ Bifrost