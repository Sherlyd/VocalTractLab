import subprocess
import sys

non_standard_libs = []  

def install_and_import(library):
    """
    Verifica si una biblioteca externa está instalada; la instala si no lo está.
    """
    try:
        __import__(library)
    except ImportError:
        print(f"Installing missing library: {library}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

for lib in non_standard_libs:
    install_and_import(lib)


import os
import sys
import ctypes
import platform
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

print("All required libraries are available. Proceeding with execution...")


"""version en español"""

# # Lista de vocales válidas definidas en el archivo .speaker utilizado por VTL (VocalTractLab)
# valid_shapes = ["a", "e", "i", "o", "u"]

# def create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename):
#     """
#     Crea un archivo .ges con la configuración gestual correspondiente a una vocal.
#     Este archivo se genera con la estructura requerida por la API de VTL.
#     """
    
#     # Validación: asegurar que la vocal esté entre las permitidas
#     if vowel_label not in valid_shapes:
#         raise ValueError(f"La vocal '{vowel_label}' no está definida en el archivo .speaker.")

#     # Elemento raíz del archivo XML
#     gestural_score = ET.Element('gestural_score')

#     # Definición de capas o secuencias de gestos con sus respectivos valores
#     tiers = [
#         ('vowel-gestures', vowel_label),            # Gesto de vocal (forma articulatoria)
#         ('glottal-shape-gestures', 'modal'),        # Gesto glotal (forma de fonación)
#         ('f0-gestures', f0_value),                  # Gesto de frecuencia fundamental
#         ('lung-pressure-gestures', lung_pressure_dpa)  # Gesto de presión pulmonar
#     ]

#     # Construcción de cada secuencia de gestos con parámetros comunes
#     for tier_type, value in tiers:
#         gesture_sequence = ET.SubElement(gestural_score, 'gesture_sequence', {'type': tier_type, 'unit': ''})
#         gesture_attribs = {
#             'value': str(value),
#             'slope': "0.000000",
#             'duration_s': f"{duration_s:.6f}",      # Duración del gesto en segundos (con 6 decimales)
#             'time_constant_s': "0.020000",          # Constante de tiempo estándar
#             'neutral': "0"                          # Indica si se trata de un gesto neutral
#         }
#         ET.SubElement(gesture_sequence, 'gesture', gesture_attribs)

#     # Formatear el XML para guardarlo de forma legible
#     pretty_xml = minidom.parseString(ET.tostring(gestural_score, encoding='unicode')).toprettyxml(indent="  ")

#     # Guardar el archivo .ges resultante
#     with open(output_filename, 'w', encoding='utf-8') as f:
#         f.write(pretty_xml)

#     print(f"Archivo .ges estructurado generado: {output_filename}")

# def generate_multiple_vowel_ges(duration_s, f0_value, lung_pressure_dpa):
#     """
#     Genera archivos .ges para todas las vocales válidas.
#     Ideal para automatizar pruebas o simulaciones con todas las vocales.
#     """
#     for vowel in valid_shapes:
#         output_filename = f"vocal_{vowel}.ges"
#         create_vowel_ges(vowel, duration_s, f0_value, lung_pressure_dpa, output_filename)

# def generate_single_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa):
#     """
#     Genera un único archivo .ges para una vocal específica.
#     """
#     if vowel_label not in valid_shapes:
#         raise ValueError(f"La vocal '{vowel_label}' no está definida en el archivo .speaker.")
    
#     output_filename = f"vocal_{vowel_label}.ges"
#     create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename)

# def modify_vocal_tract_position(ges_filename, jaw_height, lip_width, tongue_tip_x, tongue_tip_y):
#     """
#     Agrega modificaciones a la configuración del tracto vocal en un archivo .ges ya existente.
#     Permite especificar la posición de la mandíbula, labios y punta de lengua.
#     """
    
#     tree = ET.parse(ges_filename)
#     root = tree.getroot()

#     # Agregar secuencia para el gesto de la mandíbula
#     jaw_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'jaw-gestures', 'unit': ''})
#     ET.SubElement(jaw_sequence, 'gesture', {
#         'value': str(jaw_height),
#         'slope': "0.000000",
#         'duration_s': "0.600000",
#         'time_constant_s': "0.020000",
#         'neutral': "0"
#     })

#     # Agregar secuencia para el gesto de los labios
#     lip_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'lip-gestures', 'unit': ''})
#     ET.SubElement(lip_sequence, 'gesture', {
#         'value': str(lip_width),
#         'slope': "0.000000",
#         'duration_s': "0.600000",
#         'time_constant_s': "0.020000",
#         'neutral': "0"
#     })

#     # Agregar secuencia para el gesto de la punta de la lengua (coordenadas X, Y)
#     tongue_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'tongue-tip-gestures', 'unit': ''})
#     ET.SubElement(tongue_sequence, 'gesture', {
#         'value': f"{tongue_tip_x},{tongue_tip_y}",
#         'slope': "0.000000",
#         'duration_s': "0.600000",
#         'time_constant_s': "0.020000",
#         'neutral': "0"
#     })

#     # Guardar archivo modificado
#     tree.write(ges_filename)
#     print(f"Modificaciones aplicadas al archivo: {ges_filename}")

# # =======================
# # EJEMPLO DE USO
# # =======================
# if __name__ == "__main__":
#     # Definición de parámetros base
#     vowel_label = "u"
#     duration_s = 1
#     f0_value = "82"               # Frecuencia fundamental (Hz)
#     lung_pressure_dpa = "8000"    # Presión pulmonar en decaPascales

#     # Crear un archivo .ges básico para la vocal "u"
#     ges_filename = f"vocal_{vowel_label}.ges"
#     create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, ges_filename)

#     # Crear archivos .ges para todas las vocales
#     generate_multiple_vowel_ges(duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

#     # Crear un solo archivo .ges para la vocal "a"
#     generate_single_vowel_ges(vowel_label="a", duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

#     # Aplicar cambios a la configuración del tracto vocal en el archivo generado
#     modify_vocal_tract_position(
#         ges_filename, 
#         jaw_height="1.5000", 
#         lip_width="1.2000", 
#         tongue_tip_x="3.5000", 
#         tongue_tip_y="-1.0000"
#     )


"""English version"""


# Vowel shapes defined in the loaded .speaker file
valid_shapes = ["a", "e", "i", "o", "u"]

def create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename):
    """Creates a .ges file with the structure required by the VTL API."""
    
    if vowel_label not in valid_shapes:
        raise ValueError(f"The vowel '{vowel_label}' is not defined in the .speaker file.")

    # Create root element for the gestural score
    gestural_score = ET.Element('gestural_score')

    # List of gesture types and corresponding values
    tiers = [
        ('vowel-gestures', vowel_label),
        ('glottal-shape-gestures', 'modal'),
        ('f0-gestures', f0_value),
        ('lung-pressure-gestures', lung_pressure_dpa)
    ]

    # Add gesture sequences to the gestural score
    for tier_type, value in tiers:
        gesture_sequence = ET.SubElement(gestural_score, 'gesture_sequence', {'type': tier_type, 'unit': ''})
        gesture_attribs = {
            'value': str(value),
            'slope': "0.000000",
            'duration_s': f"{duration_s:.6f}",
            'time_constant_s': "0.020000",
            'neutral': "0"
        }
        ET.SubElement(gesture_sequence, 'gesture', gesture_attribs)

    # Generate a pretty-printed XML string and write it to a file
    pretty_xml = minidom.parseString(ET.tostring(gestural_score, encoding='unicode')).toprettyxml(indent="  ")
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)

    print(f"Structured .ges file generated: {output_filename}")

def generate_multiple_vowel_ges(duration_s, f0_value, lung_pressure_dpa):
    """Generates .ges files for all vowels defined in the .speaker file."""
    for vowel in valid_shapes:
        output_filename = f"vowel_{vowel}.ges"
        create_vowel_ges(vowel, duration_s, f0_value, lung_pressure_dpa, output_filename)

def generate_single_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa):
    """Generates a single .ges file for the specified vowel."""
    if vowel_label not in valid_shapes:
        raise ValueError(f"The vowel '{vowel_label}' is not defined in the .speaker file.")
    
    output_filename = f"vowel_{vowel_label}.ges"
    create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename)

def modify_vocal_tract_position(ges_filename, jaw_height, lip_width, tongue_tip_x, tongue_tip_y):
    """Modifies jaw, lip, and tongue tip position in an existing .ges file."""
    
    tree = ET.parse(ges_filename)
    root = tree.getroot()

    # Add jaw gesture
    jaw_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'jaw-gestures', 'unit': ''})
    ET.SubElement(jaw_sequence, 'gesture', {
        'value': str(jaw_height),
        'slope': "0.000000",
        'duration_s': "0.600000",
        'time_constant_s': "0.020000",
        'neutral': "0"
    })

    # Add lip gesture
    lip_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'lip-gestures', 'unit': ''})
    ET.SubElement(lip_sequence, 'gesture', {
        'value': str(lip_width),
        'slope': "0.000000",
        'duration_s': "0.600000",
        'time_constant_s': "0.020000",
        'neutral': "0"
    })

    # Add tongue tip gesture (x, y coordinates)
    tongue_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'tongue-tip-gestures', 'unit': ''})
    ET.SubElement(tongue_sequence, 'gesture', {
        'value': f"{tongue_tip_x},{tongue_tip_y}",
        'slope': "0.000000",
        'duration_s': "0.600000",
        'time_constant_s': "0.020000",
        'neutral': "0"
    })

    # Save modified .ges file
    tree.write(ges_filename)
    print(f"Modifications applied to file: {ges_filename}")

# =======================
# Example usage
# =======================
if __name__ == "__main__":
    vowel_label = "u"
    duration_s = 1
    f0_value = "82"
    lung_pressure_dpa = "8000"

    ges_filename = f"vowel_{vowel_label}.ges"
    create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, ges_filename)

    # Generate .ges files for all vowels
    generate_multiple_vowel_ges(duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

    # Generate .ges file for a specific vowel
    generate_single_vowel_ges(vowel_label="a", duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

    # Modify vocal tract positions in a .ges file
    modify_vocal_tract_position(
        ges_filename,
        jaw_height="1.5000",
        lip_width="1.2000",
        tongue_tip_x="3.5000",
        tongue_tip_y="-1.0000"
    )
