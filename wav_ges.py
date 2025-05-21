import subprocess
import sys

non_standard_libs = []  

def install_and_import(library):
    """
    Verifica si una biblioteca externa está instalada; la instala si no lo está.
    Checks if an external library is installed; installs it if it is not.
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
import numpy as np
import pandas as pd

"""version en español"""

# # Cargar la API de VocalTractLab según el sistema operativo
# if sys.platform == "win32":
#     VTL = ctypes.cdll.LoadLibrary("./VocalTractLabApi.dll")
# else:
#     VTL = ctypes.cdll.LoadLibrary("./VocalTractLabApi.so")

# if not VTL:
#     raise RuntimeError("Error al cargar la biblioteca VTL. Verifica la ruta del archivo .dll/.so.")

# # Archivo .speaker
# speaker_file_name = ctypes.c_char_p(b"./JD2.speaker")

# def generate_wav_and_csv_from_ges(gesture_file_name_str):
#     """Genera un archivo .wav y un archivo .misc y .csv desde un archivo .ges y .speaker"""
    
#     gesture_file_name = ctypes.c_char_p(gesture_file_name_str.encode())

#     # Extraer el nombre base del archivo .ges
#     base_name = os.path.basename(gesture_file_name_str).split("_")[-1].split(".")[0]
#     wav_file_name_str = f"{base_name}.wav"
#     misc_file_name_str = f"{base_name}.misc"  
#     csv_file_name_str = f"{base_name}.csv"    

#     wav_file_name = ctypes.c_char_p(wav_file_name_str.encode())
#     misc_file_name = ctypes.c_char_p(misc_file_name_str.encode())

#     numSamples = ctypes.c_int(0)
#     audio = (ctypes.c_double * int(10 * 44100))()  # Reserva memoria para el audio


#     failure = VTL.vtlInitialize(speaker_file_name)
#     if failure != 0:
#         raise RuntimeError(f"Error en vtlInitialize! Código de error: {failure}")


#     print(f"Generando archivos para {gesture_file_name_str}...")
#     failure = VTL.vtlGesturalScoreToAudio(
#         gesture_file_name,
#         wav_file_name,
#         misc_file_name,
#         ctypes.byref(audio),
#         ctypes.byref(numSamples),
#         0,  # No mostrar salida en consola
#         1   # Activa la generación de `.misc`
#     )

#     if failure != 0:
#         VTL.vtlClose()
#         raise RuntimeError(f"Error al generar archivos. Código de error: {failure}")

#     print(f"Archivos generados:\n - {wav_file_name.value.decode()} (audio)\n - {misc_file_name.value.decode()} (datos)")

#     VTL.vtlClose()

#     convert_misc_to_csv(misc_file_name_str, csv_file_name_str)

# def convert_misc_to_csv(misc_file, csv_file):
#     """Convierte el archivo .misc en un archivo .csv."""
#     if os.path.exists(misc_file):
#         data = np.loadtxt(misc_file, skiprows=1)
#         df = pd.DataFrame(data)

#         df.to_csv(csv_file, index=False, header=False)
#         print(f"Archivo CSV generado: {csv_file}")
#     else:
#         print("El archivo .misc no fue encontrado, no se generó el CSV.")

# def generate_wavs_and_csvs_from_multiple_ges(ges_folder):
#     """Genera archivos .wav y .csv para todos los archivos .ges dentro de una carpeta."""
    
#     if not os.path.exists(ges_folder):
#         raise ValueError(f"La carpeta {ges_folder} no existe.")

#     ges_files = [f for f in os.listdir(ges_folder) if f.endswith(".ges")]

#     if not ges_files:
#         print("No se encontraron archivos .ges en la carpeta.")
#         return

#     print(f"Procesando {len(ges_files)} archivos .ges en {ges_folder}...")

#     for ges_file in ges_files:
#         ges_path = os.path.join(ges_folder, ges_file)
#         generate_wav_and_csv_from_ges(ges_path)

# #########
# # uso
# #########
# if __name__ == "__main__":
#     #genera el wav, misc y csv desde un solo ges
#     generate_wav_and_csv_from_ges("./vowel_u.ges")
#     #genera la cantidad de wav, misc y csv como de archivos ges hay
#     generate_wavs_and_csvs_from_multiple_ges("direccion de la carpeta/")

"""english version"""
import subprocess
import sys

non_standard_libs = []  

def install_and_import(library):
    """
    Checks if an external library is installed; installs it if it is not.
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
import numpy as np
import pandas as pd


# Load the VocalTractLab API according to the operating system
if sys.platform == "win32":
    VTL = ctypes.cdll.LoadLibrary("./VocalTractLabApi.dll")
else:
    VTL = ctypes.cdll.LoadLibrary("./VocalTractLabApi.so")

if not VTL:
    raise RuntimeError("Error loading the VTL library. Check the path of the .dll/.so file.")

# Speaker file
speaker_file_name = ctypes.c_char_p(b"./JD2.speaker")

def generate_wav_and_csv_from_ges(gesture_file_name_str):
    """Generates a .wav file and a .misc and .csv file from a .ges and .speaker file."""
    
    gesture_file_name = ctypes.c_char_p(gesture_file_name_str.encode())

    # Extract the base name from the .ges file
    base_name = os.path.basename(gesture_file_name_str).split("_")[-1].split(".")[0]
    wav_file_name_str = f"{base_name}.wav"
    misc_file_name_str = f"{base_name}.misc"  
    csv_file_name_str = f"{base_name}.csv"    

    wav_file_name = ctypes.c_char_p(wav_file_name_str.encode())
    misc_file_name = ctypes.c_char_p(misc_file_name_str.encode())

    numSamples = ctypes.c_int(0)
    audio = (ctypes.c_double * int(10 * 44100))()  # Reserve memory for audio


    failure = VTL.vtlInitialize(speaker_file_name)
    if failure != 0:
        raise RuntimeError(f"Error in vtlInitialize! Error code: {failure}")


    print(f"Generating files for {gesture_file_name_str}...")
    failure = VTL.vtlGesturalScoreToAudio(
        gesture_file_name,
        wav_file_name,
        misc_file_name,
        ctypes.byref(audio),
        ctypes.byref(numSamples),
        0,  # Do not show output in console
        1   # Enable `.misc` generation
    )

    if failure != 0:
        VTL.vtlClose()
        raise RuntimeError(f"Error generating files. Error code: {failure}")

    print(f"Generated files:\n - {wav_file_name.value.decode()} (audio)\n - {misc_file_name.value.decode()} (data)")

    VTL.vtlClose()

    convert_misc_to_csv(misc_file_name_str, csv_file_name_str)

def convert_misc_to_csv(misc_file, csv_file):
    """Converts a .misc file into a .csv file."""
    if os.path.exists(misc_file):
        data = np.loadtxt(misc_file, skiprows=1)
        df = pd.DataFrame(data)

        df.to_csv(csv_file, index=False, header=False)
        print(f"CSV file generated: {csv_file}")
    else:
        print("The .misc file was not found, the CSV file was not generated.")

def generate_wavs_and_csvs_from_multiple_ges(ges_folder):
    """Generates .wav and .csv files for all .ges files inside a folder."""
    
    if not os.path.exists(ges_folder):
        raise ValueError(f"The folder {ges_folder} does not exist.")

    ges_files = [f for f in os.listdir(ges_folder) if f.endswith(".ges")]

    if not ges_files:
        print("No .ges files found in the folder.")
        return

    print(f"Processing {len(ges_files)} .ges files in {ges_folder}...")

    for ges_file in ges_files:
        ges_path = os.path.join(ges_folder, ges_file)
        generate_wav_and_csv_from_ges(ges_path)

#########
# Usage
#########
if __name__ == "__main__":
    # Generate wav, misc, and csv from a single ges file
    generate_wav_and_csv_from_ges("./vowel_u.ges")
    # Generate as many wav, misc, and csv files as there are ges files
    generate_wavs_and_csvs_from_multiple_ges("folder path/")