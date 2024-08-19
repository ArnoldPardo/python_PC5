import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('airbnb.csv')

# Seleccionar columnas relevantes para el agrupamiento
features = df[['price', 'reviews', 'overall_satisfaction', 'accommodates', 'bedrooms']]

# Eliminar filas con valores nulos y reiniciar el índice
features = features.dropna().reset_index(drop=True)
df = df.loc[features.index].reset_index(drop=True)  # Asegurarse de que el DataFrame original también esté alineado

# Normalizar los datos
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Aplicar K-Means
k = 5
kmeans = KMeans(n_clusters=k, random_state=0)
df['kmeans_cluster'] = kmeans.fit_predict(scaled_features)

# Verificar longitud
print(f"Longitud del DataFrame después de K-Means: {len(df)}")

# Graficar K-Means
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(df['price'], df['overall_satisfaction'], c=df['kmeans_cluster'], cmap='viridis')
plt.xlabel('Price')
plt.ylabel('Overall Satisfaction')
plt.title('K-Means Clustering')
plt.colorbar(label='Cluster')

# Aplicar Clustering Jerárquico
Z = linkage(scaled_features, method='ward')

# Graficar el dendrograma
plt.subplot(1, 2, 2)
dendrogram(Z)
plt.title('Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')

plt.tight_layout()
plt.show()

# Definir el número de clusters para el clustering jerárquico
num_clusters = 5
df['hierarchical_cluster'] = fcluster(Z, num_clusters, criterion='maxclust')

# Verificar longitud
print(f"Longitud del DataFrame después de Clustering Jerárquico: {len(df)}")

# Graficar Clustering Jerárquico
plt.figure(figsize=(12, 6))
plt.scatter(df['price'], df['overall_satisfaction'], c=df['hierarchical_cluster'], cmap='viridis')
plt.xlabel('Price')
plt.ylabel('Overall Satisfaction')
plt.title('Hierarchical Clustering')
plt.colorbar(label='Cluster')

plt.show()
