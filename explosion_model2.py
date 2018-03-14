#Script to find areas of houses that are a certain distance from an explosion point.
#Allows the user to input different feature layers to run the model, such as different building or point location files.
#Allows the user to specify parameters.

import arcpy
from arcpy import env

#arcpy.env.workspace = "C:/Users/kate/Documents/python_uni/Python_Advanced/albertsurface"

#Set up the inputs the user has to enter and thier type.
explosion = arcpy.GetParameterAsText(0) # Feature layer
buildings = arcpy.GetParameterAsText(1)  # Feature layer
distance =  arcpy.GetParameterAsText(2) # Linear unit
name1 = arcpy.GetParameterAsText(3) # feature class
name2 = arcpy.GetParameterAsText(4) # feature class

#If the user wants to name the output shapefiles something that already exists, replace the old file with the new one.
if arcpy.Exists(name1):
    arcpy.Delete_management(name1)
if arcpy.Exists(name2):
    arcpy.Delete_management(name2)

#Catch errors that exist without crashing the program.	
try:
    try:
		#Import the arc toolbox that the script is located in.
        arcpy.ImportToolbox("C:/Users/kate/Documents/python_uni/Python_Advanced/albertsurface/Models.tbx","models")
		#Let the user know the progress of the script.
        arcpy.AddMessage("Toolbox is importing")
    #Inform user of any errors that occur.
	except arcpy.ExecuteError as e:
        print(arcpy.GetMessages())
        print("Import toolbox error", e)
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        arcpy.AddError(tbinfo)

    try:
    #Run the model with the parameters specified above.
	 arcpy.Explosion_models(explosion,distance,name1,buildings,name2)
		#Inform the user of the model progress.
        arcpy.AddMessage("Model is running")
    #Catch and print any error messages but continue running.
	except arcpy.ExecuteError as e:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        arcpy.AddError(tbinfo)
        print("Model run error", e)

#Catch and print any other errors that occur but continue running.
except Exception as e:
    print(e)