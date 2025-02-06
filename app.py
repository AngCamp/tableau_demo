from flask import Flask, jsonify, request
from simulation import Simulator
from dataclasses import asdict
import os

app = Flask(__name__)
simulator = Simulator()

@app.route('/simulate', methods=['POST'])
def run_simulation():
    params = request.get_json()
    result = simulator.run_effect_sim(**params)
    return jsonify(asdict(result))

@app.route('/save/<sim_id>', methods=['POST'])
def save_simulation():
    data = request.get_json()
    os.makedirs('simulations', exist_ok=True)
    filename = f"simulations/{data['id']}.json"
    simulator.save_json(data, filename)
    return jsonify({"status": "saved"})

if __name__ == '__main__':
    app.run(debug=True)