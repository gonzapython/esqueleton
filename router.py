from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receta', methods=['GET', 'POST'])
def enviar_datos():
    if request.method == 'POST':
        data = request.json # pasa los datos del body a un diccionario python
        # result = receta.create(data) # receta.create es un metodo que hace cosas con el dato pasado
        result = data
        return jsonify(result) #SIEMPRE HAY QUE DEVOLVER ALGO
    
    if request.method == 'GET':
        data = request.args # args: los argumentos q he puesto en el postman -> http://localhost:5000/receta?contain=tomate&have=spagethi
        print(data)
        return jsonify(data)

@app.route('/options', methods=['GET', 'POST'])   # en postman poner: http://localhost:5000/options
def show_options():
    if request.method == 'GET':
        options = [{'crear_receta': '/recetas', 'metodo':'post'},
                    {'registrarse': '/user', 'metodo':'post'},
                    {'obtener_todas_recetas':'/recetas', 'metodo':'get'},
                    {'obtener_una_receta':'/receta', 'metodo':'get'}  # he añadido esta opcion yo, OJO
                    ]
        return jsonify(options)

if __name__ == "__main__":
    app.run()

