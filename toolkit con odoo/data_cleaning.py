from datetime import datetime
import pandas as pd

def validate_date(date_str, date_format='%Y-%m-%d'):
    if pd.isna(date_str) or date_str == '':
        return None
    if isinstance(date_str, pd.Timestamp):
        date_str = date_str.strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        current_date = datetime.now()
        return current_date.strftime(date_format)  # Fecha por defecto (fecha actual)

def validate_price(price):
    try:
        price = float(price)
        return max(price, 0)  # Si el precio es negativo, se corrige a 0
    except ValueError:
        return 0.0  # Precio por defecto

def validate_reference(reference):
    try:
        return int(reference)  # Convertir a entero
    except (ValueError, TypeError):
        return 0  # Valor por defecto

def validate_product_name(name):
    return name.strip() if isinstance(name, str) and name.strip() != '' else 'Producto Desconocido'  # Nombre por defecto

def validate_quantity(quantity):
    try:
        quantity = int(quantity)
        return max(quantity, 1)  # Si la cantidad es menor que 1, se corrige a 1
    except ValueError:
        return 1  # Cantidad por defecto

def validate_total(total):
    try:
        return float(total) if total >= 0 else 0.0  # Asegurarse de que el total sea positivo
    except ValueError:
        return 0.0  # Total por defecto

def validate_tax(tax):
    try:
        return float(tax) if tax >= 0 else 0.0  # Asegurarse de que el impuesto sea positivo
    except ValueError:
        return 0.0  # Impuesto por defecto

def clean_data(data):
    df = pd.DataFrame(data)
    
    # Aplicar validaciones con correcciones automáticas
    df['fecha limite de pedido'] = df['fecha limite de pedido'].apply(lambda x: validate_date(x, '%Y-%m-%d'))
    df['fecha de recepcion'] = df['fecha de recepcion'].apply(lambda x: validate_date(x, '%Y-%m-%d'))
    df['precio unitario'] = df['precio unitario'].apply(validate_price)
    df['referencia de proveedor'] = df['referencia de proveedor'].apply(validate_reference)
    df['producto'] = df['producto'].apply(validate_product_name)
    df['cantidad'] = df['cantidad'].apply(validate_quantity)
    df['total'] = df['total'].apply(validate_total)
    df['impuesto'] = df['impuesto'].apply(validate_tax)

    return df.to_dict(orient='records')

def main(file_path):
    df = pd.read_excel(file_path)
    print("Nombres de las columnas en el archivo Excel:")
    print(df.columns.tolist())

    cleaned_data = clean_data(df.to_dict(orient='records'))

    print("Datos corregidos:")
    for item in cleaned_data:
        print(item)

if __name__ == '__main__':
    file_path = r'C:\Users\borja\Desktop\toolkit con odoo\prueba2.xlsx'
    main(file_path)
