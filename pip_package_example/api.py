import json
import numpy as np

with open("pip_package_example/data/model.json", 'r') as f:
    model_data = json.load(f)

print(model_data["name"])
print(model_data["token"])
print(np.array([0]))