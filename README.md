# QGIS Automated Slope Analysis (PyQGIS)

An automated Python script designed for QGIS (PyQGIS) to calculate the exact average slope of a defined polygon area using drone-derived Elevation/Slope raster maps.

## Use Case
When analyzing drone photogrammetry data (e.g., for roof inspections, solar panel installation, or terrain leveling), manual slope estimation is prone to error. This script automates the **Zonal Statistics** process, extracting precise mathematical averages directly from raster pixel values bounded by a specific vector geometry.

## How it works
1. Fetches the active Vector Layer (e.g., `Property_Boundary`).
2. Fetches the targeted Raster Layer (e.g., `Prudnik_Slope_Final`).
3. Runs the QGIS `native:zonalstatisticsfb` algorithm in temporary memory.
4. Outputs a clean, automated report in the Python Console with the exact average slope in degrees.

## Tech Stack
* **GIS Software:** QGIS 3.x
* **Language:** Python 3 (PyQGIS API)
* **Data Input:** Drone mapping outputs (DEM / DSM / Slope Rasters)

---
*Developed by Igor Hajducki | Global Ortho Solutions*
