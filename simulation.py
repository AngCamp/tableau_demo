# simulation.py
import numpy as np
import json
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class SimulationRun:
   """
   Class to store simulation parameters, data and metadata.
   
   Attributes:
       params (dict): Simulation parameters (e.g. n_points, mean, effect_size)
       data (dict): Generated data from simulation
       id (str, optional): Unique identifier for simulation run
       timestamp (str, optional): ISO format timestamp of simulation
   """
   params: dict
   data: dict
   id: str = None
   timestamp: str = None
   
   def __post_init__(self):
       if not self.id:
           self.id = f"sim_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
       if not self.timestamp:
           self.timestamp = datetime.now().isoformat()

class Simulator:
   """
   Class to run simulations and generate data.
   
   Attributes:
       seed (int, optional): Random seed for reproducibility
       rng (numpy.random.Generator): NumPy random number generator
   """
   def __init__(self, seed=None):
       self.seed = seed
       self.rng = np.random.default_rng(seed)
   
   def run_effect_sim(self, n_points=100, mean=0, effect_size=0):
       """
       Run simulation generating control and treatment groups.
       
       Args:
           n_points (int): Number of points per group
           mean (float): Mean of control group
           effect_size (float): Difference in means between groups
           
       Returns:
           SimulationRun: Object containing simulation parameters and results
       """
       params = {"n_points": n_points, "mean": mean, "effect_size": effect_size}
       control = self.rng.normal(mean, 1, n_points).tolist()
       treatment = self.rng.normal(mean + effect_size, 1, n_points).tolist()
       data = {"control": control, "treatment": treatment}
       return SimulationRun(params=params, data=data)

   def save_json(self, simulation: SimulationRun, filename: str):
       """
       Save simulation run to JSON file.
       
       Args:
           simulation (SimulationRun): Simulation to save
           filename (str): Output file path
       """
       with open(filename, 'w') as f:
           json.dump(asdict(simulation), f)