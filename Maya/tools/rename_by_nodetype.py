import maya.cmds as cmds

init_nodes = ['persp', 'top','front', 'side']

light_types = ['aiPhotometricLight', 'ambientLight', 'aiLightBlocker', 'aiAreaLight', 'aiMeshLight', 'directionalLight',
    'pointLight', 'areaLight', 'volumeLight', 'aiSkyDomeLight', 'spotLight']

camera_types = ['camera', 'stereoRigCamera']



for i in cmds.ls(type='mesh'):
    print i


