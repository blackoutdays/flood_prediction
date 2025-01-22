import folium

# Locations and coordinates of major cities in Kazakhstan
stations = {
    "Almaty": [43.238949, 76.889709],
    "Nur-Sultan": [51.169392, 71.449074],
    "Shymkent": [42.3417, 69.5901],
    "Kokshetau": [53.2833, 69.4167],
    "Karaganda": [49.8333, 73.1667],
}

# Data for each city: water levels, temperature, rainfall, and pressure
flood_data = {
    "Almaty": {"Water Level": 4.5, "Temperature": 30.1, "Rainfall": 12, "Pressure": 950},
    "Nur-Sultan": {"Water Level": 3.0, "Temperature": 25.3, "Rainfall": 5, "Pressure": 960},
    "Shymkent": {"Water Level": 5.8, "Temperature": 33.2, "Rainfall": 20, "Pressure": 945},
    "Kokshetau": {"Water Level": 2.1, "Temperature": 20.8, "Rainfall": 8, "Pressure": 970},
    "Karaganda": {"Water Level": 3.5, "Temperature": 22.5, "Rainfall": 10, "Pressure": 955},
}

# Create the base map centered on Kazakhstan
map_floods = folium.Map(location=[48.0196, 66.9237], zoom_start=5)

# Add city data to the map with circle markers
for city, coords in stations.items():
    data = flood_data[city]
    water_level = data["Water Level"]
    rainfall = data["Rainfall"]

    # Color-coding based on water level
    if water_level < 3:
        color = "green"
        icon = "info-sign"
    elif 3 <= water_level <= 5:
        color = "orange"
        icon = "warning-sign"
    else:
        color = "red"
        icon = "exclamation-sign"

    # Marker size increases with rainfall
    size = 5 + rainfall

    # Add detailed popup information for each city
    popup_info = (
        f"<b>{city}</b><br>"
        f"Water Level: {water_level} m<br>"
        f"Temperature: {data['Temperature']} °C<br>"
        f"Rainfall: {rainfall} mm<br>"
        f"Pressure: {data['Pressure']} hPa"
    )

    # Add a circle marker with the calculated size and color
    folium.CircleMarker(
        location=coords,
        radius=size,
        popup=folium.Popup(popup_info, max_width=250),
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
    ).add_to(map_floods)

# Save the map
map_floods.save("kazakhstan_flood_map_with_markers.html")
print("City-level circle marker map saved as 'kazakhstan_flood_map_with_markers.html'.")


from folium.plugins import HeatMap

# Stations with coordinates
stations = {
    "Almaty": [43.238949, 76.889709],
    "Nur-Sultan": [51.169392, 71.449074],
    "Shymkent": [42.3417, 69.5901],
    "Kokshetau": [53.2833, 69.4167],
    "Karaganda": [49.8333, 73.1667],
}

# Values for the heatmap
values = {
    "Almaty": 30.1,
    "Nur-Sultan": 25.3,
    "Shymkent": 33.2,
    "Kokshetau": 20.8,
    "Karaganda": 22.5,
}

# Create a base map
heatmap_map = folium.Map(location=[48.0196, 66.9237], zoom_start=5)

# Prepare data for the heatmap
heat_data = [[coords[0], coords[1], values[city]] for city, coords in stations.items()]

# Add the heatmap layer
HeatMap(heat_data, radius=15).add_to(heatmap_map)

# Save the heatmap
heatmap_map.save("kazakhstan_heatmap.html")
print("Geographic heatmap saved as 'kazakhstan_heatmap.html'.")

