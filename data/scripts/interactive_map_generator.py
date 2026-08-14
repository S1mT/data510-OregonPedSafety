import pandas as pd
import folium

print("Loading hotspot data...")
profiles = pd.read_csv('data/processed/systemic_hotspots_profile.csv')
incidents = pd.read_csv('data/processed/systemic_hotspots_incidents.csv')

# 1. Center the map on Oregon (using the mean of our hotspots)
map_center = [profiles['Centroid_Latitude'].mean(), profiles['Centroid_Longitude'].mean()]

# Initialize the map with a dark theme so the bright colors pop
m = folium.Map(location=map_center, zoom_start=7, tiles='CartoDB Voyager')

# 2. Define a bright, distinct color palette for up to 20 clusters
colors = [
    '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', 
    '#FF8000', '#FF007F', '#80FF00', '#00FF80', '#007FFF', '#8000FF',
    '#FFBF00', '#BFFF00', '#00FFBF', '#00BFFF', '#BF00FF', '#FF00BF'
]

print(f"Plotting {len(profiles)} Danger Zones and {len(incidents)} Fatal Incidents...")

# 3. Draw the Danger Zones (Radii)
for i, row in profiles.iterrows():
    cluster_color = colors[i % len(colors)]
    
    # HTML tooltip text for the radius
    radius_tooltip = (
        f"<b>Hotspot #{row['Cluster_ID']}</b><br>"
        f"Unique Incidents: {row['Unique_Incidents']}<br>"
        f"Total Fatalities: {row['Total_Fatalities']}<br>"
        f"Years Active: {row['Years_Active']}<br>"
        f"Radius: {row['Radius_Meters']}m<br>"
        f"<i>Dominant Road: {row['Dominant_FUNC_SYSNAME']}</i>"
    )
    
    folium.Circle(
        location=[row['Centroid_Latitude'], row['Centroid_Longitude']],
        radius=row['Radius_Meters'],
        color=cluster_color,
        weight=2,
        fill=True,
        fill_color=cluster_color,
        fill_opacity=0.25, # 25% opacity so you can see the streets underneath
        tooltip=radius_tooltip
    ).add_to(m)

# 4. Plot the Individual Fatalities (Dots inside the radii)
for _, row in incidents.iterrows():
    # Match the dot color to its parent cluster's radius color
    cluster_idx = profiles[profiles['Cluster_ID'] == row['SPATIAL_CLUSTER']].index[0]
    dot_color = colors[cluster_idx % len(colors)]
    
    # HTML tooltip text for individual crashes
    incident_tooltip = (
        f"<b>Incident: ST_CASE {row['ST_CASE']}</b><br>"
        f"Year: {row['YEAR']}<br>"
        f"Speed Limit: {row['VSPD_LIMNAME']}<br>"
        f"Light: {row['LGT_CONDNAME']}<br>"
        f"Pedestrian Position: {row['PEDPOSNAME']}"
    )
    
    folium.CircleMarker(
        location=[row['LATITUDE'], row['LONGITUD']],
        radius=6, # Size of the dot
        color='white',
        weight=1.5,
        fill=True,
        fill_color=dot_color,
        fill_opacity=1.0,
        tooltip=incident_tooltip
    ).add_to(m)

# 5. Save the interactive map
output_path = 'data/processed/oregon_systemic_hotspots_map.html'
m.save(output_path)
print(f"\nSUCCESS! Interactive map saved to {output_path}")
print("Double-click the .html file in your file explorer to open it in your web browser.")