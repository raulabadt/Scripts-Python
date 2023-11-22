import json

# Nombre del archivo GeoJSON original y de la copia
original_geojson_filename = 'copia_tu_archivo.geojson'
sql_filename = 'insert_queries.sql'

# Campos que se desean conservar
campos_a_conservar = ['provincia', 'municipio', 'poligono', 'parcela', 'recinto', 'dn_surface', 'uso_sigpac']

# Abrir y cargar el archivo GeoJSON original
with open(original_geojson_filename, 'r') as original_geojson_file:
    geojson_data = json.load(original_geojson_file)

# Abrir el archivo SQL para escritura
with open(sql_filename, 'w') as sql_file:
    # Iterar sobre las entidades en el GeoJSON
    for feature in geojson_data['features']:
        # Asegurar que los campos tengan la cantidad de dígitos deseados
        municipio = str(feature['properties']['municipio']).zfill(3)
        poligono = str(feature['properties']['poligono']).zfill(3)
        parcela = str(feature['properties']['parcela']).zfill(4)

        # Crear el nuevo campo "referencia catastral"
        referencia_catastral = f"{feature['properties']['provincia']}{municipio}A{poligono}{parcela}.{feature['properties']['recinto']}"

        # Obtener las coordenadas sin corchetes
        coordinates_str = ', '.join(map(lambda x: f'{x[1]} {x[0]}', feature['geometry']['coordinates'][0]))

        # Escribir la consulta INSERT INTO en el archivo SQL
        sql_query = f"INSERT INTO dbo.NombreBBDD (PoligTexto, Refcatastral, Area) VALUES (geometry::STGeomFromText('POLYGON(({coordinates_str}))', 0), '{referencia_catastral}', {feature['properties']['dn_surface']});\n"

        # Escribir la consulta en el archivo
        sql_file.write(sql_query)

print(f"Las consultas han sido generadas y guardadas en {sql_filename}.")
