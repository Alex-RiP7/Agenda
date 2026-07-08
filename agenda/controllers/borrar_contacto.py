import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:
    
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
            return render.borrar_contacto(contacto)
        else:
            return web.notfound("Contacto no encontrado")

   