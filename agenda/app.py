import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/ver_contacto/(.+)', 'controllers.ver_contacto.VerContacto',
    '/editar_contacto/(.+)', 'controllers.editar_contacto.EditarContacto',
    '/borrar_contacto/(.+)', 'controllers.borrar_contacto.BorrarContacto',
    '/insertar_contacto', 'controllers.insertar_contacto.InsertarContacto',  
)   

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()