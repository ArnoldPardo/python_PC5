import requests
import zipfile
import os
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar URLs y rutas de archivos
url = "https://netsg.cs.sfu.ca/youtubedata/0302.zip"
zip_file_path = "0302.zip"
extract_folder = "youtube_data"

# Paso 1: Descargar el archivo .zip
response = requests.get(url)
if response.status_code == 200:
    with open(zip_file_path, 'wb') as file:
        file.write(response.content)
    print("Archivo .zip descargado.")
else:
    print("Error al descargar el archivo:", response.status_code)
    exit()

# Paso 2: Verificar y descomprimir el archivo
if not zipfile.is_zipfile(zip_file_path):
    print("El archivo descargado no es un archivo zip válido.")
    exit()

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Listar archivos dentro del ZIP
    zip_files = zip_ref.namelist()
    print("Archivos en el ZIP:")
    for file in zip_files:
        print(file)
    
    # Extraer todos los archivos
    zip_ref.extractall(extract_folder)
print("Archivo descomprimido en la carpeta:", extract_folder)

# Paso 3: Leer el archivo correcto
file_name = '0302/0.txt'  # Ajusta esto según sea necesario
file_path = os.path.join(extract_folder, file_name)

if not os.path.isfile(file_path):
    print(f"El archivo {file_path} no existe.")
    exit()

# Leer una muestra del archivo para verificar el delimitador
with open(file_path, 'r') as file:
    lines = [file.readline() for _ in range(10)]
print("Primeras 10 líneas del archivo:")
for line in lines:
    print(line)

# Leer el archivo con pandas, ajustando el delimitador según lo que hayas observado
try:
    df = pd.read_csv(file_path, delimiter='\t', header=None, engine='python', error_bad_lines=False)
    print("Datos cargados correctamente.")
except pd.errors.ParserError as e:
    print("Error al leer el archivo:", e)
    exit()

# Asignar nombres a las columnas
df.columns = ['VideoID', 'edad', 'categoria', 'views', 'rate']
print("Primeras filas con nombres de columna:")
print(df.head())

# Paso 4: Seleccionar las columnas deseadas y filtrar los datos
df = df[['VideoID', 'edad', 'categoria', 'views', 'rate']]
categorias_deseadas = ['Music', 'Education']
df_filtered = df[df['categoria'].isin(categorias_deseadas)]
print("Datos filtrados:")
print(df_filtered.head())

# Paso 5: Exportar los datos a MongoDB
client = MongoClient('mongodb+srv://arnolmcgiberth0:Mcgiberth1@cluster0.pwaie.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['youtube_data']
collection = db['videos']

# Convertir el DataFrame a un diccionario y exportar a MongoDB
data_dict = df_filtered.to_dict(orient='records')
collection.insert_many(data_dict)
print("Datos exportados a MongoDB.")

# Paso 6: Crear y guardar gráficos
# Gráfico 1: Distribución de Vistas por Categoría
plt.figure(figsize=(10, 6))
sns.barplot(x='categoria', y='views', data=df_filtered)
plt.title('Distribución de Vistas por Categoría')
plt.xticks(rotation=45)
plt.xlabel('Categoría')
plt.ylabel('Vistas')
plt.tight_layout()
plt.savefig('vistas_por_categoria.png')
plt.show()

# Gráfico 2: Tasa Media de Valoración por Categoría
plt.figure(figsize=(10, 6))
sns.barplot(x='categoria', y='rate', data=df_filtered, ci=None)
plt.title('Tasa Media de Valoración por Categoría')
plt.xticks(rotation=45)
plt.xlabel('Categoría')
plt.ylabel('Tasa Media de Valoración')
plt.tight_layout()
plt.savefig('tasa_media_por_categoria.png')
plt.show()
