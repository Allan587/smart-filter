import sqlite3

conexion = sqlite3.connect('app_beta_db.sqlite3')

cursor = conexion.cursor()

# Guardar (commit) los cambios
conexion.commit()

class controller():
    def __init__(self):
        
        self.insert()
        
    def insert(self):
        sql = '''INSERT INTO usuarios (id_product, product_name, product_brand, product_type, stock)
            VALUES (%s, %s, %s, %s, %s)'''
        values = ()
# 5. Realizar una consulta
cursor.execute('SELECT * FROM usuarios')

# Obtener todos los resultados de la consulta
usuarios = cursor.fetchall()

# Mostrar los resultados
for usuario in usuarios:
    print(usuario)

# 6. Cerrar la conexión a la base de datos
conexion.close()