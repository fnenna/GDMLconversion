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
    #vColoured = pyg4ometry.visualisation.VtkViewerColouredNew(color)
    print(f"Name: {logical_volume.name}")
    logical_volume.materialName = logical_volume.name
    print(logical_volume.material)
    #v.addSolid(solidVolume, colour = color)
    v.addLogicalVolume(logical_volume.solid, "G4_Air", logical_volume.name)
    #v.setMaterial(logical_volume.material)
    #v.setVolumeColor(logical_volume,color)
    
    v.buildPipelinesAppend()
    v.exportVTPScene(f"hcal_scene_part{i}.vtp")
    v.clear()
    print(i)
    i+=1
