import sqlite3
import app_beta
from app_beta import *

class controller():
    def __init__(self):
        self.conexion = sqlite3.connect('app_beta_db.sqlite3')

        self.cursor = self.conexion.cursor()
        self.conexion.commit()
        
        self.insert()
        
    def insert(self):
        self.sql = '''INSERT INTO inventory (id_product, product_name, product_brand, product_type, stock)
            VALUES (?, ?, ?, ?, ?)'''
        self.values = ()
        
# 5. Realizar una consulta
cursor.execute('SELECT * FROM usuarios')

# Obtener todos los resultados de la consulta
usuarios = cursor.fetchall()

# Mostrar los resultados
for usuario in usuarios:
    print(usuario)

# 6. Cerrar la conexión a la base de datos
conexion.close()