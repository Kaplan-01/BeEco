import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/alumnos/")

class EstudioEco():
    
    def GET(self):
        try:
            return render.estudioEco() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.