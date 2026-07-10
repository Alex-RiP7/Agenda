import web
import sqlite3

render = web.template.render('views', base='layout')

class InsertarContacto:
    
    def GET(self):
        # Muestra el formulario vacío
        return render.insertar_contacto()

    def POST(self):
        try:
            data = web.input()
            
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO contactos 
                (nombre, primer_apellido, segundo_apellido, email, telefono)
                VALUES (?, ?, ?, ?, ?)
            """, (
                data.nombre,
                data.primer_apellido,
                data.segundo_apellido,
                data.email,
                data.telefono
            ))
            
            conn.commit()
            conn.close()
            
            # Redirigir a la lista después de insertar
            raise web.seeother('/lista_contactos')
        except Exception as e:
            print(f"ERROR al insertar contacto: {e}")
            return "Error al guardar el nuevo contacto"