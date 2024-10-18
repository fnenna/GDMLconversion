import pyg4ometry


r = pyg4ometry.gdml.Reader("Desktop/calorimeter_geometry.gdml")
registry = r.getRegistry()
print("Logical Volumes:")
v = pyg4ometry.visualisation.VtkViewerNew()
colors =[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1), (52,52,0), (140,52, 0), (140, 140, 52)]
i=0
v = pyg4ometry.visualisation.VtkViewerNew()
#for solidVolume in registry.solidDict.values():
for logical_volume in registry.logicalVolumeDict.values():
    color =  colors[i]
    v = pyg4ometry.visualisation.VtkViewerColouredNew(color)
    #vColoured = pyg4ometry.visualisation.VtkViewerColouredNew(color)
    print(f"Name: {logical_volume.name}")
    logical_volume.material.name = "None"#logical_volume.name
    print(logical_volume.material)
    print(logical_volume.solid)
    #v.addSolid(solidVolume, colour = color)
    v.addLogicalVolume(logical_volume)
    #sssssv.addLogicalVolume(element)
    #v.setMaterial(logical_volume.material)
    #v.setVolumeColor(logical_volume,color)
    
    v.buildPipelinesAppend()
    v.exportVTPScene(f"new_hcal_scene_part{i}.vtp")
    v.clear()
    print(i)
    i+=1
