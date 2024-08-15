from data_extraccion import extract_data_from_excel
from data_cleaning import clean_data
from odoo_conexion import connect_to_odoo, load_data_to_odoo

if __name__ == '__main__':
    # Paso 1: Extraer datos
    file_path = 'ruta_a_tu_archivo.xlsx'
    raw_data = extract_data_from_excel(file_path)

    # Paso 2: Limpiar y validar datos
    cleaned_data = clean_data(raw_data)

    # Paso 3: Conectar y cargar datos en Odoo
    uid, models = connect_to_odoo()

    for record in cleaned_data:
        record_id = load_data_to_odoo('tu_modelo_odoo', record, uid, models)
        print(f'Datos cargados en Odoo con ID: {record_id}')
