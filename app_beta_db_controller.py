import sqlite3

conexion = sqlite3.connect('app_beta_db.sqlite3')

cursor = conexion.cursor()

# Guardar (commit) los cambios
conexion.commit()

class controller():
    def __init__(self):
        
        self.insert()
        
    def insert(self):
        cursor.execute("INSERT INTO ")
# 5. Realizar una consulta
cursor.execute('SELECT * FROM usuarios')

# Obtener todos los resultados de la consulta
usuarios = cursor.fetchall()

# Mostrar los resultados
for usuario in usuarios:
    print(usuario)

# 6. Cerrar la conexión a la base de datos
conexion.close()