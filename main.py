import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import send_from_directory
import time


print("Iniciando la aplicación...")
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "¡Bienvenido a mi aplicación Flask!"


@app.route('/favicon.ico')
def favicon():
    # Puedes devolver una imagen de favicon o simplemente un mensaje
    return jsonify({"message": "¡Favicon no encontrado!"})

@app.route('/commands/', methods=['GET'])
def comandas_data():
    connection= mysql.connector.connect(
        host="10.5.0.4", 
        user="DiegoAS", 
        password="ProyectoAS2324", 
        database="ProyectoAS2324Restaurante",
        port=3306)
    
    if connection:
        cursor = connection.cursor()
        cursor.execute("select table_name from INFORMATION_SCHEMA.tables where table_name = 'Comandas ' limit 50")
        exists = cursor.fetchone()
        if exists:
            connection.close()
            return jsonify({"message": "La tabla Comandas ya existe"})
        else:
            cursor.execute("CREATE TABLE Comandas (id INT NOT NULL AUTO_INCREMENT, primerPlato VARCHAR(255) NOT NULL, segundoPlato VARCHAR(255) NOT NULL, nMesa int, PRIMARY KEY (id))")
            cursor.execute("INSERT INTO Comandas (primerPlato, segundoPlato, nMesa) VALUES ('Paella de marisco', 'Ensalada mixta', 1)")
            cursor.execute("INSERT INTO Comandas (primerPlato, segundoPlato, nMesa) VALUES ('Arroz con bogavante' , 'Ensalada mixta', 3)")
            cursor.execute("INSERT INTO Comandas (primerPlato, segundoPlato, nMesa) VALUES ('Alubias pintas' , 'Chuleton a la brasa', 4)")
            cursor.execute("INSERT INTO Comandas (primerPlato, segundoPlato, nMesa) VALUES ('Tortilla de bacalado' , 'Lubina a la plancha', 2)")
            connection.commit()
            time.sleep(1)
            cursor.execute("SELECT * FROM Comandas")
            comandas = cursor.fetchall()
            connection.close()
            retorno = {"lComandas": []}
            for t in comandas:
                retorno["lComandas"].append({"id":t[0],"primerPlato": t[1], "segundoPlato": t[2], "nMesa": t[3]})
    
            return jsonify(retorno)
            
        

@app.route('/nuevacomanda', methods=['POST'])
def nuevaComanda():
    primerPlato = request.json['primerPlato']
    segundoPlato = request.json['segundoPlato']
    nMesa = request.json['nMesa']


    connection = mysql.connector.connect(
        host="10.5.0.4",
        user="DiegoAS",
        password="ProyectoAS2324",
        database="ProyectoAS2324Restaurante",
        port=3306)

    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Comandas (primerPlato, segundoPlato, nMesa) VALUES (%s, %s, %s)", (primerPlato, segundoPlato, nMesa))
        connection.commit()
        connection.close()
        return jsonify({"message": "Comanda creada con exito"})
    else:   
        return jsonify({"message": "No se pudo conectar con la base de datos"})
    


app.run(host='0.0.0.0', port=4201)