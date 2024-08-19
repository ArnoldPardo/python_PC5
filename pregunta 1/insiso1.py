import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('airbnb.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())

print("Forma del DataFrame (filas, columnas):", df.shape)
print("Nombres de las columnas:", df.columns)

# Mostrar las ultimas filas del DataFrame
print("Últimas 5 filas del DataFrame:")
print(df.tail())

print("Estadísticas descriptivas del DataFrame:")
print(df.describe())

print("Información del DataFrame:")
print(df.info())

