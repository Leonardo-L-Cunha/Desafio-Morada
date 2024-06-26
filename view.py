from flask import Flask, jsonify, make_response, request
from app import app

def calculate_banknotes(value):
    banknotes = [100, 50, 20, 10, 5, 2]

    result = {
        '100': 0,
        '50': 0,
        '20': 0,
        '10': 0,
        '5': 0,
        '2': 0,
    }

    for banknote in banknotes:
        if value >= banknote:
            result[str(banknote)] = value // banknote
            value %= banknote

    if value != 0:
        return None

    return result        


@app.route('/api/saque', methods=['POST'])
def atm():
    data = request.get_json()

    if 'valor' not in data:
        response = jsonify({"error": 'Missing input valor',})
        return make_response(response, 400)

    value = data['valor']

    if not isinstance(value, int) :
        response = jsonify({"error": 'Must be an integer'})
        return make_response(response, 400)
    
    result = calculate_banknotes(value)

    if result is None:
        response = jsonify({'Error': 'Amount cannot be withdrawn'})
        return make_response(response, 400)
    
    return jsonify(result)