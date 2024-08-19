import pandas as pd
import sqlite3

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

# Reporte 2: Promedio de Precio y Cantidad de Reviews por País
resumen_pais = df.groupby('pais').agg({'precio': 'mean', 'descripcion': 'count'}).reset_index()
resumen_pais.rename(columns={'descripcion': 'cantidad_reviews'}, inplace=True)
resumen_pais.sort_values(by='precio', ascending=False).to_excel('resumen_pais.xlsx', index=False)

# Reporte 3: Vinos con Mejor Puntuación por Categoría de Precio
mejores_vinos_categoria = df.loc[df.groupby('categoria_precio')['puntos'].idxmax()]

# Guardar en SQLite
conn = sqlite3.connect('vinos.db')
mejores_vinos_categoria.to_sql('mejores_vinos_categoria', conn, index=False, if_exists='replace')
conn.close()

# Reporte 4: Estadísticas Descriptivas por Etiqueta de Reputación
estadisticas_reputacion = df.groupby('reputacion').agg({
    'precio': ['mean', 'median', 'std'],
    'puntos': ['mean', 'median', 'std']
}).reset_index()
estadisticas_reputacion.columns = ['_'.join(col).strip() for col in estadisticas_reputacion.columns.values]

# Exportar a JSON
estadisticas_reputacion.to_json('estadisticas_reputacion.json', orient='records', lines=True)

print("Reportes generados y exportados con éxito.")
