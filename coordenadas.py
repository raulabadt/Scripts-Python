with open('C:/Users/RaúlAbadTorralba/Desktop/geojson/sintaxfix.sql', 'r') as f:
    for line in f:
        if 'POLYGON' in line:
            # Extrae las coordenadas del POLYGON
            start_index = line.find('((')
            end_index = line.find('))')
            coordinates_str = line[start_index + 2:end_index]
            
            # Divide las coordenadas en pares latitud-longitud
            coordinates = [pair.split() for pair in coordinates_str.split(',')]
           
            # Invierte el orden de las coordenadas
            reversed_coordinates = [' '.join(pair[::-1]) for pair in coordinates]

            # Reemplaza las coordenadas originales con las invertidas
            new_coordinates_str = ','.join(reversed_coordinates)
                      
            new_line = line.replace(coordinates_str, new_coordinates_str)
            print(new_line)
           
            with open('C:/Users/RaúlAbadTorralba/Desktop/geojson/archivo2.sql', 'a') as i:
                i.write(new_line)
        else:
            with open('C:/Users/RaúlAbadTorralba/Desktop/geojson/archivo2.sql', 'a') as i:
                i.write(line)

print('Proceso completado')

