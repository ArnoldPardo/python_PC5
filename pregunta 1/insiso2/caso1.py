import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('airbnb.csv')

# Filtrar los alojamientos con más de 10 críticas y puntuación mayor a 4
filtered_df = df[(df['reviews'] > 10) & (df['overall_satisfaction'] > 4)]

# Ordenar por puntuación de mayor a menor y por número de críticas de mayor a menor
sorted_df = filtered_df.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])

# Seleccionar las primeras 3 alternativas
top_3_alternatives = sorted_df.head(3)

# Mostrar los resultados
print("Las 3 mejores alternativas para Alicia y su familia son:")
print(top_3_alternatives[['room_id', 'overall_satisfaction', 'reviews', 'neighborhood', 'room_type', 'price']])
