import xmlrpc.client

url = 'http://localhost:8069'
db = 'nombre_de_tu_base_de_datos'
username = 'tu_usuario'
password = 'tu_contraseña'

def connect_to_odoo():
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    return uid, models

def load_data_to_odoo(model_name, data, uid, models):
    record_id = models.execute_kw(db, uid, password, model_name, 'create', [data])
    return record_id
