import arcpy

#Set the workspace environment.
arcpy.env.workspace = "M:/Python_Advanced/albertsurface"
#Import the model toolbox.
arcpy.ImportToolbox("M:/Python_Advanced/albertsurface/Models.tbx","models")
#Run the explosion model.
arcpy.Explosion_models("explosion0/point","20 Meters","mickey.shp","build0/polygon","mouse.shp")
