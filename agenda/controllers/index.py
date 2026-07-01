import web

render = web.template.render('templates/', base='layout')

class Index:
    def GET(self):
        return render.index()