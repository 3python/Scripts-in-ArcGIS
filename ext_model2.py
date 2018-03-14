import arcpy
from arcpy import env

#Set the location files are searched for and created.
arcpy.env.workspace = "M:/Python_Advanced/albertsurface"

#Create names for the shapefiles that are created.
name1 = "house.shp"
name2 = "flatl.shp"

#Overwrite existing shapefiles if one is created with the same name.
if arcpy.Exists(name1):
	arcpy.Delete_management(name1)
	
if arcpy.Exists(name2):
	arcpy.Delete_management(name2)

#Run the model.	
try:
	#Import the toolbox that the model is located in.
    try:
        arcpy.ImportToolbox("M:/Python_Advanced/albertsurface/Models.tbx","models")
    #If it doesn't exist catch and print the error but continue running.
	except arcpy.ExecuteError as e:
        print("Import toolbox error", e)
    #Run the model.
	try:
        arcpy.Explosion_models("explosion0/point","20 Meters",name1,"build0/polygon",name2)
    #If the model doesn't exist, catch and print the error but continue running.
	except arcpy.ExecuteError as e:
        print("Model run error", e)
#Generally catch, continue and print errors found when trying to run this script.
except Exception as e:
    print(e)