import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('winemag-data-130k-v2.csv')

# Explorar el DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

print("\nInformación del DataFrame:")
print(df.info())

print("\nResumen estadístico del DataFrame:")
print(df.describe())

print("\nNombres de las columnas:")
print(df.columns)

# Renombrar columnas
df.rename(columns={
    'country': 'pais',
    'description': 'descripcion',
    'points': 'puntos',
    'price': 'precio',
    'title': 'titulo'
}, inplace=True)

# Crear nuevas columnas

# 1. Categoría de Precio
def categorize_price(price):
    if pd.isna(price):
        return 'Desconocido'
    elif price < 20:
        return 'Económico'
    elif price < 50:
        return 'Moderado'
    else:
        return 'Carísimo'

df['categoria_precio'] = df['precio'].apply(categorize_price)

# 2. Precio por Punto
df['precio_por_punto'] = df['precio'] / df['puntos']

# 3. Longitud de Descripción
df['longitud_descripcion'] = df['descripcion'].apply(lambda x: len(x) if pd.notna(x) else 0)

# 4. Etiqueta de Reputación (Basado en puntos)
def reputacion(puntos):
    if puntos >= 90:
        return 'Excelente'
    elif puntos >= 80:
        return 'Muy Bueno'
    elif puntos >= 70:
        return 'Bueno'
    else:
        return 'Regular'

df['reputacion'] = df['puntos'].apply(reputacion)

print("\nNuevas columnas:")
print(df.columns)
print(df.head())
