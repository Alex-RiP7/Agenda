import web
import sqlite3

render = web.template.render('views', base='layout')


class VerContacto:
    
    def buscarContacto(self, id_contacto):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            
            row = cursor.fetchone()
            
           
            if row is None:
                return None  
                
            contacto = {
                'id_contacto': row[0],
                'nombre': row[1],
                'primer_apellido': row[2],
                'segundo_apellido': row[3],
                'email': row[4],
                'telefono': row[5]
            }

            return contacto
            
        except sqlite3.Error as error:
            print(f"ERROR verContactos 100: {error}")
            return None
        except Exception as error:
            print(f"ERROR verContactos 101: {error}")
            return None
        finally:
            if 'conn' in locals():
                conn.close()


    def GET(self, id_contacto):
        print(f"ID CONTACTO recibido: {id_contacto}")
        
        try:
            id_contacto = int(id_contacto)
        except ValueError:
            print("ID inválido")
            return web.notfound("ID de contacto inválido")
        
        contacto = self.buscarContacto(id_contacto)
        print("Contacto encontrado:", contacto)
        
        # Renderizamos la plantilla
        if contacto:
            return render.ver_contacto(contacto=contacto)
        else:
            return web.notfound("Contacto no encontrado")


urls = (
    '/ver/(\d+)', 'VerContacto',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()