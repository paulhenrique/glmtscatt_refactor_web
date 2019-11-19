import json
import numpy as np

vet = []
for i in range(0,1000):
    vet.append(np.random.randint(200))

a = {
    'a': vet
}

print(json.dumps(a))