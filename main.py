from flask import Flask, request, jsonify
from datetime import datetime
from classes import Registro
from banco_de_dados import registrar, pegar

app = Flask(__name__)

@app.post('/registrar_medicao')
def registrar_medicao():
  timestamp = int(datetime.timestamp(datetime.now()))
  medicao = Registro(timestamp, request.json)
  registrar(medicao)
  return jsonify({ 'success': True })

@app.get('/pegar_medicoes')
def pegar_medicoes():
  medicoes = pegar()
  return jsonify(medicoes)

app.run()