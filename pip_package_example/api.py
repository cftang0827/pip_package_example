import json
import numpy as np
import os

with open(os.path.join(os.path.dirname(__file__), "data/model.json"),
          'r') as f:
    model_data = json.load(f)

print(model_data["name"])
print(model_data["token"])
print(np.array([0]))
print("Read model success")