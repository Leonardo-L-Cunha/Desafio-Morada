from flask import Flask, jsonify, make_response, request
from app import app


@app.route('/api/saque', methods=['POST'])
def atm():
    data = request.get_json()

    if 'valor' not in data:
        response = jsonify('Input invalid')
        return make_response(response, 401)
    
    return jsonify('ok')