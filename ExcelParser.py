# Libreria que se usara para permitir los colores en la terminal
import os
os.system("color")

# Colores para el texto
# Referencia:
# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
BLUE = '\033[94m'
NORMAL = '\033[0m'
GREEN = '\x1b[1;32;40m'
BLINK_CYAN = '\x1b[6;36;40m'

# Listas con los nombres de los archivos
# Nombres de los archivos de entrada
input_filenames = []
# Nombres de los archivos con las plantillas
template_filenames = []
# Nombres de los archivos de salida
output_filenames = []

# Se obtienen los nombres de los archivos con los datos de entrada, templates de salida y outputs
with open("config/files.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Quitamos el salto de linea de la linea leida
        l = line.strip()

        # Dependiendo del texto que se incluye, es a que lista se agrega
        if ("input" in l):
            input_filenames.append(l)
        elif ("template" in l):
            template_filenames.append(l)
        elif ("output" in l):
            output_filenames.append(l)


# Convierte los datos de los archivos de entrada a una lista de diccionarios
for index, ifn in enumerate(input_filenames):
    # Se abre el archivo con los datos de entrada
    with open(ifn, 'r') as file:
        headers = []
        values = []

        # Leemos todas las lineas del archivo
        lines = file.readlines()

        # Por cada linea...
        for i, line in enumerate(lines):
            # Si es la primer linea, obtenemos los headers
            if (i == 0):
                # Por cada token de la linea guardamos un header. Estos estan separados por tabs
                for h in line.strip().split("\t"):
                    # Al header se le cambian los espacios por guiones bajos y se convierte a minusculas
                    headers.append(h.replace(" ", "_").lower())
            # En cambio, si no es la primera, guardamos los datos en una lista de diccionarios
            else:
                # Se separa la linea por tabulaciones y quita el salto de linea 
                tokens = line.strip().split("\t")
                # Agregamos un diccionario vacio a la lista
                values.append({})
                # Por cada columna se guarda en el mismo registro de la lista, pero con una
                # diferente llave del diccionario. La llave es el header de la columna
                for i2, t in enumerate(tokens):
                    values[i-1][headers[i2]] = t
    
    # Se abre y guardan los templates en una lista
    with open(template_filenames[index], 'r') as file:
        template_queries = file.readlines()

    # Se abre para escribir cada uno de los archivos de salida
    with open(output_filenames[index], 'w') as file:
        # Por cada template se imprimen todos los datos obtenidos del input
        # con el formato del template
        for query in template_queries:
            print(BLUE + f"Escribiendo en {output_filenames[index]}:\n")
            print(NORMAL + query)
            for val in values:
                file.write(eval(query) + "\n")
            print(GREEN + "\nCompletado\n\n\n")

# Previene que se cierre la terminal hasta recibir input del usuario
input(BLINK_CYAN + "Presiona <Enter> para salir..." + NORMAL)