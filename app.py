import web
import json

render = web.template.render('views/')
        
urls = (
    '/','index',
    '/acercaDe', 'acercaDe',
    '/Datos(.*)','datos'
)

class datos:        
    def GET(self, data):
        data = []
        with open('datosM.json','r') as file:
            data = json.load(file)
        return render.datos(data['results'])

class acercaDe:        
    def GET(self):
        return render.acercaDe()

class index:        
    def GET(self):
        return render.index()


if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()

