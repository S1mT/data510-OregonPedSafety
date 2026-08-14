import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN

# 1. Load the original Master Dataset (which still has LATITUDE and LONGITUD)
df = pd.read_csv('data/processed/FARSinfrastructure.csv')

# 2. Filter out missing coordinates
# FARS sometimes uses 99.9999 or 88.8888 for unknown GPS points
df_clean = df[(df['LATITUDE'] < 50) & (df['LONGITUD'] < 0)].copy()

# 3. Convert Degrees to Radians (Required for Haversine)
# Scikit-learn expects coordinates in [Latitude, Longitude] order, in radians
coords = np.radians(df_clean[['LATITUDE', 'LONGITUD']])

# 4. Set your Spatial Parameters
miles_per_radian = 3958.8  # Radius of the Earth in miles
epsilon_miles = 0.1
epsilon_radians = epsilon_miles / miles_per_radian
min_deaths = 3

# 5. Run Spatial DBSCAN
db = DBSCAN(eps=epsilon_radians, min_samples=min_deaths, metric='haversine', algorithm='ball_tree')
df_clean['SPATIAL_CLUSTER'] = db.fit_predict(coords)

# 6. Analyze the Results
print(f"Spatial Parameters: {epsilon_miles} miles, {min_deaths}+ deaths")
print("-" * 40)

# Count how many clusters were found (ignoring -1, which is unclustered noise)
n_clusters = len(set(df_clean['SPATIAL_CLUSTER'])) - (1 if -1 in df_clean['SPATIAL_CLUSTER'].values else 0)
print(f"Total High-Injury Clusters Found: {n_clusters}")

# Print the size of each cluster
cluster_counts = df_clean[df_clean['SPATIAL_CLUSTER'] != -1]['SPATIAL_CLUSTER'].value_counts()
for cluster_id, count in cluster_counts.items():
    print(f"Cluster {cluster_id}: {count} Fatalities")

# Save the clustered data so you can map it
df_clean.to_csv('data/processed/FARSclusters.csv', index=False)