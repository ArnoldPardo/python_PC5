import pandas as pd

# Leer el archivo CSV
try:
    df = pd.read_csv('airbnb.csv')
except FileNotFoundError:
    print("El archivo 'airbnb.csv' no se encontró en la carpeta 'data'.")
    raise

# Identificadores de las propiedades de Roberto y Clara
roberto_id = 97503
clara_id = 90387

# Filtrar las propiedades de Roberto y Clara
roberto_clara_df = df[df['room_id'].isin([roberto_id, clara_id])]

# Verificar si se encontraron propiedades
if roberto_clara_df.empty:
    print("No se encontraron propiedades para los IDs proporcionados.")
else:
    # Crear el DataFrame con las propiedades seleccionadas
    roberto_clara_df = roberto_clara_df[['room_id', 'host_id', 'room_type', 'neighborhood', 'reviews', 'overall_satisfaction', 'accommodates', 'bedrooms', 'price']]

    # Guardar el DataFrame en un archivo Excel
    roberto_clara_df.to_excel('roberto.xlsx', index=False)

    print("El archivo 'roberto.xlsx' ha sido creado con las propiedades de Roberto y Clara.")
