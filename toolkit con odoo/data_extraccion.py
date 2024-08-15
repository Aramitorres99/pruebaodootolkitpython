import pandas as pd


def extract_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

