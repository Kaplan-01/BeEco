import mysql.connector

class Alumnos():
# Conexion
        def connect(self):
            try:
                self.cnx = mysql.connector.connect(
                    # Usamos el nombre de nuestro usuario con la contrasena.
                    user='melanie', 
                    password='Agenda.2020',
                    host='127.0.0.1',
                    port=3309,
                    database='escuela'
                    )
                self.cursor = self.cnx.cursor()

            except Exception as e:
                print(e)


        # Realizamos una consulta de todos los datos existentes de todas las columnas y filas
        def select(self):
            try:
                self.connect()
                # Consulta
                query = ("SELECT * from alumnos;")
                self.cursor.execute(query)
                # Arreglo
                result = []
                for row in self.cursor:
                    # Diccionario para almacenamiento
                    r = {
                        'id_alumno':row[0],
                        'matricula':row[1],
                        'nombre':row[2],
                        'primer_apellido':row[3],
                        'segundo_apellido':row[4],
                        'edad':row[5],
                        'fecha_nacimiento':row[6],
                        'sexo':row[7],
                        'estado':row[8],
                    }
                    result.append(r)
                self.cursor.close()
                self.cnx.close()
                return result

            except Exception as e:
                print(e)
                # En caso de que haya problemas con el diccionario
                result = []
                return result
    # Insertar

        def insert(self, id_alumno, matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado):
            try:
                self.connect()
                query = ("INSERT INTO alumnos (matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado) values(%s, %s, %s, %s, %s, %s, %s, %s);")
                values = (matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False

    # Eliminar

        def delete(self, id_alumno, matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado):
            try:
                self.connect()
                query = ("DELETE FROM alumnos WHERE id_alumno=%s;")
                values = (id_alumno)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False

    # Actualizar

        def update(self, id_alumno, matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado):
            try:
                self.connect()
                query = ("UPDATE alumno SET matricula=%s, nombre=%s, primer_apellido=%s, segundo_apellido=%s, edad=%s, fecha_nacimiento=%s, sexo=%s, estado=%s;")
                values = (matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False


    # Vista

        def view(self, id_alumno):
            try:
                self.connect()
                query = ("SELECT * from alumnos where id_alumno = %s;")
                values = (id_alumno)
                self.cursor.execute(query, values)
                result = []
                for row in self.cursor:
                     r = {
                        'id_alumno':row[0],
                        'matricula':row[1],
                        'nombre':row[2],
                        'primer_apellido':row[3],
                        'segundo_apellido':row[4],
                        'edad':row[5],
                        'fecha_nacimiento':row[6],
                        'sexo':row[7],
                        'estado':row[8],
                    }
                result.append(r)
                self.cursor.close()
                self.cnx.close()
                return result
            except Exception as e:
                print(e)
                result = []
                return result


objeto = Alumnos()
objeto.connect()
for row in objeto.select():
    print(row)
    
    # En caso de requerir solo uno es como:
    # print(row['nombre'])