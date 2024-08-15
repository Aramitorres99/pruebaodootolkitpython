import pandas as pd
import os

def extract_data_from_excel(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"El archivo no se encuentra en la ruta: {file_path}")
    
    # Leer el archivo Excel
    df = pd.read_excel(file_path, engine='openpyxl')
    return df

# Ruta del archivo
file_path = r'C:\Users\borja\Desktop\toolkit con odoo\Hoja de cálculo sin título.xlsx'

# Imprimir la ruta del archivo
print(f"Ruta del archivo: {file_path}")

try:
    extracted_data = extract_data_from_excel(file_path)
    print(extracted_data)
except Exception as e:
    print(f"Ocurrió un error: {e}")
