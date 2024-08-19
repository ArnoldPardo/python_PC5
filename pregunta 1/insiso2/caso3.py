import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('airbnb.csv')

# Definir el presupuesto y el número de noches
budget_per_night = 50
number_of_nights = 3
total_budget = budget_per_night * number_of_nights

# Filtrar las propiedades que están dentro del presupuesto
filtered_df = df[df['price'] <= total_budget]

# Separar las propiedades en 'Shared room' y otras
shared_rooms = filtered_df[filtered_df['room_type'] == 'Shared room']
other_rooms = filtered_df[filtered_df['room_type'] != 'Shared room']

# Ordenar las habitaciones compartidas por puntuación (de mayor a menor) y luego por precio (de menor a mayor)
shared_rooms_sorted = shared_rooms.sort_values(by=['overall_satisfaction', 'price'], ascending=[False, True])

# Ordenar las otras habitaciones solo por precio (de menor a mayor)
other_rooms_sorted = other_rooms.sort_values(by='price', ascending=True)

# Combinar ambos DataFrames, dando prioridad a las habitaciones compartidas
combined_sorted_df = pd.concat([shared_rooms_sorted, other_rooms_sorted])

# Seleccionar las primeras 10 propiedades más baratas
top_10_properties = combined_sorted_df.head(10)

# Mostrar los resultados
print("Las 10 propiedades más baratas para Diana, priorizando habitaciones compartidas con mejor puntuación son:")
print(top_10_properties[['room_id', 'room_type', 'price', 'overall_satisfaction', 'neighborhood']])
