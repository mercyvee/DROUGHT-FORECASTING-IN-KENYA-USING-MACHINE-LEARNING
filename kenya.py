import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Weather station coordinates (latitude, longitude)
weather_stations = {
    'Lodwar': (3.1216, 35.6001),
    'Kakamega': (0.2833, 34.7500),
    'Kisumu': (-0.0917, 34.7680),
    'Narok': (-1.0410, 35.6090),
    'Nakuru': (-0.3031, 36.0800),
    'Dagoretti': (-1.2439, 36.8036),
    'Nyeri': (-0.4194, 36.9531),
    'Nyahururu': (-0.2856, 36.4286),
    'Meru': (-0.0477, 37.6490),
    'Madera': (-1.6673, 37.5000),
    'Wajir': (1.7500, 40.0700),
    'Marsabit': (2.3370, 37.9780),
    'Garissa': (-0.4594, 39.6500),
    'Moyale': (3.5200, 39.1000),
    'Makindu': (-2.2950, 37.6167),
    'Voi': (-3.3931, 38.5655),
    'Malindi': (-3.1603, 40.1213),
    'Mombasa': (-4.0435, 39.6682),
    'Lamu': (-2.2683, 40.5144)
}

# Convert weather stations to a GeoDataFrame
station_points = gpd.GeoDataFrame(
    list(weather_stations.keys()),
    geometry=[Point(lon, lat) for lat, lon in weather_stations.values()],
    columns=['Station']
)

# Load the shapefile (replace with the path to your zipped shapefile)
shapefile_zip = """C:/Users/Admin/Downloads/ken_adm_iebc_20191031_shp.zip"""
kenya_gdf = gpd.read_file(f"zip://{shapefile_zip}")

# Plot the map with weather stations
fig, ax = plt.subplots(figsize=(12, 12))
kenya_gdf.plot(ax=ax, color='lightblue', edgecolor='black')
station_points.plot(ax=ax, color='red', markersize=50, label='Weather Stations')

# Add labels for the weather stations
for station, coords in weather_stations.items():
    ax.text(coords[1], coords[0], station, fontsize=8, ha='right', color='black')

# Customize the plot
ax.set_title("Weather Stations in Kenya", fontsize=16)
ax.axis('off')  # Turn off the axis for better visualization
plt.legend()
plt.tight_layout()
plt.show()

# Save the figure
plt.savefig("kenya_weather_stations_map.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()