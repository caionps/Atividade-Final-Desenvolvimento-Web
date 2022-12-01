from flask import request, Flask

app = Flask(__name__)

@app.route('/reserva', methods = ['POST'])
def reserva():
    data = 'Reserva Realizada!'
    return data

@app.route('/procura-reserva', methods = ['GET'])
def busca_reserva():
    data = 'A sua reserva já foi realizada!'
    return data

@app.route('/altera-reserva', methods = ['PUT'])
def altera_reserva():
    data = 'A sua Reserva foi alterada!'
    return data

@app.route('/deleta-reserva', methods = ['DELETE'])
def deleta_reserva():
    data = 'A sua reserva foi cancelada!'
    return data


if __name__ == '__main__':
    app.run(debug = True)
