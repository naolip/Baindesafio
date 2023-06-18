#Importação das bibliotecas necessárias 

from flask import Flask, render_template, request
from geopy import distance
import requests

app = Flask(__name__)
historico = []  # Lista para armazenar consultas

#rotas criadas
@app.route('/')
def home():
    return render_template('home.html')


#Cliente
@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

#Entregador
@app.route('/entregador')
def entregador():
    return render_template('entregador.html')

#calcudora de distancias 
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        #Verificação no formulário 
        origin = request.form.get('address_origin')
        destination = request.form.get('address_destination')
        #Dados incompletos
        if not origin or not destination:
            error_message = "Por favor, preencha todos os campos."
            return render_template('calculator.html', error_message=error_message)
        #Obter os dados
        origin_response = requests.get(
            f"https://nominatim.openstreetmap.org/search?q={origin}&format=json"
        )
        destination_response = requests.get(
            f"https://nominatim.openstreetmap.org/search?q={destination}&format=json"
        )
        #Verifica se o codigo de status 200 retorna convertendo em um json
        if origin_response.status_code == 200 and destination_response.status_code == 200:
            origin_data = origin_response.json()
            destination_data = destination_response.json()
            #Extração de Cordernadas passadas  ( foi utilizado GPT nesse trecho)
            if origin_data and destination_data:
                origin_geo = (float(origin_data[0]['lat']), float(origin_data[0]['lon']))
                destination_geo = (float(destination_data[0]['lat']), float(destination_data[0]['lon']))
                #Calcular distancia entre os dois endereços ( retirado da documentação )
                dist = distance.distance(origin_geo, destination_geo).km
                dist = round(dist, 2)
                #Adiciona a resosta da consulta alista vazia criada no inicio
                historico.append(f"A distância entre {origin} e {destination} é {dist} km")

                return render_template('calculator.html', origin=origin, destination=destination, distance=dist,
                                       consulta_realizada=True, historico=historico)
        #Uso do GPT para criação da mensagem de erro
        error_message = "Não foi possível realizar a consulta. Verifique os dados e tente novamente."
        return render_template('calculator.html', error_message=error_message)

    return render_template('calculator.html')


@app.route('/historico')
def historico_view():
    return render_template('history.html', historico=historico)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
