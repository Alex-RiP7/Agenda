import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarContacto:
    
    def obtenerContacto(self, id_contacto):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
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
        try:
            data = web.input()
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            cursor.execute("""
                UPDATE contactos 
                SET nombre = ?, primer_apellido = ?, segundo_apellido = ?, 
                    email = ?, telefono = ?
                WHERE id_contacto = ?
            """, (
                data.nombre,
                data.primer_apellido,
                data.segundo_apellido,
                data.email,
                data.telefono,
                id_contacto
            ))
            
            conn.commit()
            conn.close()
            
            raise web.seeother('/lista_contactos')  # Redirigir después de guardar
        except Exception as e:
            print(f"ERROR al actualizar: {e}")
            return "Error al actualizar contacto"