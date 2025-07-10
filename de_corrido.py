import os
import sys
import ctypes
import xml.etree.ElementTree as ET
from xml.dom import minidom
import numpy as np
import pandas as pd

VTL_PATH = "C:/Users/sherl/Desktop/ya_el_fin/VocalTractLabApi.dll"
SPEAKER_PATH = "C:/Users/sherl/Desktop/ya_el_fin/JD2.speaker"

# Vocales válidas
valid_shapes = ["a", "E", "i", "O", "u",]

# Cargar biblioteca de VocalTractLab
VTL = ctypes.cdll.LoadLibrary(VTL_PATH)
if not VTL:
    raise RuntimeError("No se pudo cargar la biblioteca VTL.")

speaker_file_name = ctypes.c_char_p(SPEAKER_PATH.encode())

def generate_sequential_vowels_ges(duration_s, f0_value, lung_pressure_dpa, output_filename):
    gestural_score = ET.Element('gestural_score')
    
    # Crear una sola secuencia por tipo
    vowel_seq = ET.SubElement(gestural_score, 'gesture_sequence', {'type': 'vowel-gestures', 'unit': ''})
    glottal_seq = ET.SubElement(gestural_score, 'gesture_sequence', {'type': 'glottal-shape-gestures', 'unit': ''})
    f0_seq = ET.SubElement(gestural_score, 'gesture_sequence', {'type': 'f0-gestures', 'unit': ''})
    lung_seq = ET.SubElement(gestural_score, 'gesture_sequence', {'type': 'lung-pressure-gestures', 'unit': ''})

    time_cursor = 0.2

    for vowel in valid_shapes:
        # Vowel gesture
        ET.SubElement(vowel_seq, 'gesture', {
            'value': vowel,
            'slope': "0.000000",
            'duration_s': f"{duration_s:.6f}",
            'start_time_s': f"{time_cursor:.6f}",
            'time_constant_s': "0.020000",
            'neutral': "0"
        })

        # Glottal gesture
        ET.SubElement(glottal_seq, 'gesture', {
            'value': 'modal',
            'slope': "0.000000",
            'duration_s': f"{duration_s:.6f}",
            'start_time_s': f"{time_cursor:.6f}",
            'time_constant_s': "0.020000",
            'neutral': "0"
        })

        # F0 gesture
        ET.SubElement(f0_seq, 'gesture', {
            'value': str(f0_value),
            'slope': "0.000000",
            'duration_s': f"{duration_s:.6f}",
            'start_time_s': f"{time_cursor:.6f}",
            'time_constant_s': "0.020000",
            'neutral': "0"
        })

        # Lung pressure gesture
        ET.SubElement(lung_seq, 'gesture', {
            'value': str(lung_pressure_dpa),
            'slope': "0.000000",
            'duration_s': f"{duration_s:.6f}",
            'start_time_s': f"{time_cursor:.6f}",
            'time_constant_s': "0.020000",
            'neutral': "0"
        })

        time_cursor += duration_s  # Avanza al próximo gesto

    # Guardar archivo bonito
    pretty_xml = minidom.parseString(ET.tostring(gestural_score, encoding='unicode')).toprettyxml(indent="  ")
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f".ges secuencial generado correctamente: {output_filename}")
def generate_wav_and_csv_from_ges(gesture_file_name_str):
    gesture_file_name = ctypes.c_char_p(gesture_file_name_str.encode())

    base_name = os.path.splitext(os.path.basename(gesture_file_name_str))[0]
    wav_file_name_str = f"{base_name}.wav"
    misc_file_name_str = f"{base_name}.misc"
    csv_file_name_str = f"{base_name}.csv"

    wav_file_name = ctypes.c_char_p(wav_file_name_str.encode())
    misc_file_name = ctypes.c_char_p(misc_file_name_str.encode())
    numSamples = ctypes.c_int(0)
    audio = (ctypes.c_double * int(60 * 44100))()

    failure = VTL.vtlInitialize(speaker_file_name)
    if failure != 0:
        raise RuntimeError(f"vtlInitialize falló con código: {failure}")

    print(f"Generando audio desde: {gesture_file_name_str}")
    failure = VTL.vtlGesturalScoreToAudio(
        gesture_file_name,
        wav_file_name,
        misc_file_name,
        ctypes.byref(audio),
        ctypes.byref(numSamples),
        0,
        1
    )

    if failure != 0:
        VTL.vtlClose()
        raise RuntimeError(f"vtlGesturalScoreToAudio falló con código: {failure}")

    print(f"Generado:\n - {wav_file_name.value.decode()}\n - {misc_file_name.value.decode()}")
    VTL.vtlClose()
    convert_misc_to_csv(misc_file_name_str, csv_file_name_str)

def convert_misc_to_csv(misc_file, csv_file):
    if os.path.exists(misc_file):
        data = np.loadtxt(misc_file, skiprows=1)
        pd.DataFrame(data).to_csv(csv_file, index=False, header=False)
        print(f"Archivo CSV generado: {csv_file}")
    else:
        print("Archivo .misc no encontrado, no se pudo generar el .csv")

# Ejecutar
if __name__ == "__main__":
    duration_s = 2.0
    f0_value = "100"
    lung_pressure_dpa = "9000"
    ges_filename = "vowels_sequential.ges"

    generate_sequential_vowels_ges(duration_s=2.0, f0_value="100", lung_pressure_dpa="7000", output_filename="vowels_sequential.ges")
    generate_wav_and_csv_from_ges(os.path.abspath(ges_filename))