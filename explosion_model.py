#This script creates a polygon of all the building area which is within a certain distance of an explosion point.
#Model runs without any input from the user.

import arcpy
from arcpy import env

#Set the workspace environment/
#This is the location that the script looks for and creates files in.
arcpy.env.workspace = "M:/Python_Advanced/albertsurface"

#Give names to the shapefiles that are created when the software is run.
#Name the intermediate buffer. This is a circle with a specified radius from the explosion point.
name1 = "house.shp"
#Name the shapefile that shows the buildings that are within the buffer zone.
name2 = "flatl.shp"

#If the name of the intermediate buffer already exists, write over it.
if arcpy.Exists(name1):
	arcpy.Delete_management(name1)
	
##If the name of the intersection polygon already exists, write over it.
if arcpy.Exists(name2):
	arcpy.Delete_management(name2)

#Open the toolbox used to run this function in such a manner that it does not fail if ther is an error.	
try:
    try:
	#Import the toolbox which contains the required model.
        arcpy.ImportToolbox("M:/Python_Advanced/albertsurface/Models.tbx","models")
    #If there is an error, catch it instead of failing to run.
    except arcpy.ExecuteError as e:
        #Print the error message.
        print("Import toolbox error", e)
    try:
        #Open up the model that we would like to run.
        #Include the parameters and file names that are to be used/created.
        arcpy.Explosion_models("explosion0/point","20 Meters",name1,"build0/polygon",name2)
    #Catch errors
    except arcpy.ExecuteError as e:
        #Print error message.
        print("Model run error", e)
#Catch all other errors.
except Exception as e:
    #Print the error message.
    print(e)