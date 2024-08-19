import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('winemag-data-130k-v2.csv')

# Verificar nombres de las columnas
print("Nombres de las columnas iniciales:")
print(df.columns)

# Ver las primeras filas para entender el contenido
print("\nPrimeras filas del DataFrame:")
print(df.head())
