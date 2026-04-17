"""
QGIS Zonal Statistics Automated Analyzer
Author: Igor Hajducki | Global Ortho Solutions
Description: Automated PyQGIS script to calculate the average slope of a defined 
polygon area using drone-derived DEM/Slope raster maps.
"""
import processing

# Fetch active layers
raster_layer = QgsProject.instance().mapLayersByName('Prudnik_Slope_Final')[0]
vector_layer = QgsProject.instance().mapLayersByName('Property_Boundary')[0] 

print("Initializing spatial analysis...")

# Define processing parameters
params = {
    'INPUT': vector_layer,
    'INPUT_RASTER': raster_layer,
    'RASTER_BAND': 1,
    'COLUMN_PREFIX': 'analysis_',
    'STATISTICS': [2], 
    'OUTPUT': 'TEMPORARY_OUTPUT'
}

# Execute zonal statistics
calculation_result = processing.run("native:zonalstatisticsfb", params)
result_layer = calculation_result['OUTPUT']

# Output results
for feature in result_layer.getFeatures():
    mean_result = feature['analysis_mean']
    print("\n" + "-"*50)
    print(f"AUTOMATED REPORT FOR: {vector_layer.name()}")
    print(f"Average surface slope: {round(mean_result, 2)} degrees")
    print("-"*50)
