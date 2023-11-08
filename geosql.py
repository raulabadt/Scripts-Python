import geopandas as gpd
from sqlalchemy import create_engine

# Ruta al archivo GeoJSON de entrada
geojson_file = 'C:/Users/RaúlAbadTorralba/Desktop/geojson/recinto.sqlite.geojson'

# Convierte GeoJSON a GeoDataFrame
gdf = gpd.read_file(geojson_file)

# Especifica la conexión a la base de datos MySQL
# Asegúrate de reemplazar 'tu_contraseña' con la contraseña real de tu base de datos
database_url = 'mysql://root:@localhost:3306/prueba'

engine = create_engine(database_url)

# Guarda el GeoDataFrame en la base de datos MySQL
gdf.to_sql('prueba', engine, if_exists='replace', index=False)

print("Conversión completada. Datos guardados en la base de datos MySQL.")
