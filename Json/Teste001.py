import json

carros = {"marca": "honda", "modelo": "HRV", "cor": "prata"}

carros_json = json.dumps(carros)

print(carros_json)

