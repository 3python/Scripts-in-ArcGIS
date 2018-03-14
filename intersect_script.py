# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# intersect_script.py
# Created on: 2018-01-23 16:36:03.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: intersect_script <Input_Features> <Distance__value_or_field_> <Output_Feature_Class> <Layer> <Intersect1> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Input_Features = arcpy.GetParameterAsText(0)

Distance__value_or_field_ = arcpy.GetParameterAsText(1)

Output_Feature_Class = arcpy.GetParameterAsText(2)

Layer = arcpy.GetParameterAsText(3)

Intersect1 = arcpy.GetParameterAsText(4)
if Intersect1 == '#' or not Intersect1:
    Intersect1 = "\\\\ds.leeds.ac.uk\\student\\student19\\ear4keb\\ArcGIS\\Default.gdb\\Intersect1" # provide a default value if unspecified

# Local variables:

# Process: Buffer
arcpy.Buffer_analysis(Input_Features, Output_Feature_Class, Distance__value_or_field_, "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Intersect
arcpy.Intersect_analysis([Layer,Output_Feature_Class], Intersect1, "ALL", "", "INPUT")
