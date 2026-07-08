import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarContacto:

    def actualizarContacto(self, contacto:dict)->bool:
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = """
                UPDATE contactos
                SET nombre = ?,
                primer_apellido = ?,
                segundo_apellido = ?,
                email = ?,
                telefono = ?
                WHERE id_contacto = ?;
            """
            datos = (
                contacto['nombre'], 
                contacto['primer_apellido'], 
                contacto['segundo_apellido'], 
                contacto['email'], 
                contacto['telefono'], 
                contacto['id_contacto'],
                )
            cursor.execute(query, datos)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"ERROR al actualizar contacto: {e}")
            return False
    
    def obtenerContacto(self, id_contacto):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = """"
                UPDATE contaactos
                SET nombre = ?
                primer_apellido = ?
                segundo_apellido = ?
                email = ?
                telefono = ?
                WHERE id_contacto = ?;
            """

            cursor.execute("SELECT * FROM contactos WHERE id_contacto = ?", (id_contacto,))
            row = cursor.fetchone()
            conn.close()
            
            if row:
                return {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
            return None
        except Exception as e:
            print(f"ERROR al obtener contacto: {e}")
            return None

    def GET(self, id_contacto):
        contacto = self.obtenerContacto(id_contacto)
        if contacto:
            return render.editar_contacto(contacto)
        else:
            return web.notfound("Contacto no encontrado")

    def POST(self, id_contacto):
        formulario = web.input()
        contacto = {
            "id_contacto": formulario['id_contacto'],
            "nombre" : formulario['nombre'],
            "primer_apellido" : formulario['primer_apellido'],
            "segundo_apellido" : formulario['segundo_apellido'],
            "email" : formulario['email'],
            "telefono" : formulario['telefono'],
        }
        resultado = self.actualizarContacto(contacto)
        return resultado