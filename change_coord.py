import json

# Nombre del archivo GeoJSON original y de la copia
original_geojson_filename = 'recinto082023.geojson'
copia_geojson_filename = 'copia_tu_archivo.geojson'

# Campos que se desean conservar
campos_a_conservar = ['dn_surface', 'uso_sigpac']

# Abrir y cargar el archivo GeoJSON original
with open(original_geojson_filename, 'r') as original_geojson_file:
    geojson_data = json.load(original_geojson_file)

# Crear una copia del GeoJSON original para realizar modificaciones
geojson_data_modificado = {'type': 'FeatureCollection', 'features': []}

# Invertir las coordenadas y seleccionar campos específicos para cada entidad en el GeoJSON original
for feature in geojson_data['features']:
    # Asegurar que los campos "municipio", "poligono" y "parcela" tengan la cantidad de dígitos deseados
    municipio = str(feature['properties']['municipio']).zfill(3)
    poligono = str(feature['properties']['poligono']).zfill(3)
    parcela = str(feature['properties']['parcela']).zfill(4)

    # Crear el nuevo campo "referencia catastral"
    referencia_catastral = f"{feature['properties']['provincia']}{municipio}A{poligono}{parcela}.{feature['properties']['recinto']}"

    # Seleccionar campos adicionales a conservar
    properties_modificadas = {
        'referencia_catastral': referencia_catastral,
        'dn_surface': feature['properties']['dn_surface'],
        'uso_sigpac': feature['properties']['uso_sigpac'],
        'coef_regadio': feature['properties']['coef_regadio']
    }

    # Modificar la geometría
    geometry_modificada = {
        'type': feature['geometry']['type'],
        # 'coordinates': [list(reversed(coord)) for coord in feature['geometry']['coordinates'][0]]
        'coordinates': [list(map(lambda x: f'{x[1]} {x[0]}', feature['geometry']['coordinates'][0]))]
    }

    # Crear la entidad modificada
    feature_modificada = {
        'type': 'Feature',
        'properties': properties_modificadas,
        'geometry': geometry_modificada
    }

    # Agregar la entidad al GeoJSON modificado
    geojson_data_modificado['features'].append(feature_modificada)

# Guardar el GeoJSON modificado en un nuevo archivo
with open(copia_geojson_filename, 'w') as copia_geojson_file:
    json.dump(geojson_data_modificado, copia_geojson_file, indent=2)

print(f"Las coordenadas han sido invertidas y el GeoJSON modificado ha sido guardado en {copia_geojson_filename} conservando los campos especificados y creando el campo 'referencia_catastral'.")
