import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/ver_contacto/(.+)', 'controllers.ver_contacto.VerContacto',
    '/editar_contacto/(.+)', 'controllers.editar_contacto.EditarContacto',  # ← Esta es la que faltaba
    # '/insertar_contacto', 'controllers.insertar_contacto.InsertarContacto',  # descomenta cuando lo tengas
    # '/borrar_contacto/(.+)', 'controllers.borrar_contacto.BorrarContacto',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()