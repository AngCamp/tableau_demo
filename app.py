# app.py
from flask import Flask, jsonify, request, send_file
from simulation import Simulator
import os

app = Flask(__name__)
simulator = Simulator()

@app.route('/simulate', methods=['POST'])
def run_simulation():
    params = request.get_json()
    result = simulator.run(**params)
    return jsonify(asdict(result))

@app.route('/save/<sim_id>', methods=['POST'])
def save_simulation():
    data = request.get_json()
    filename = f"simulations/{data['id']}.json"
    simulator.save_json(data, filename)
    return jsonify({"status": "saved"})

if __name__ == '__main__':
    app.run(debug=True)