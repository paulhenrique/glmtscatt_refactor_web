
import json
import numpy as np


#a = np.array([[1, 2, 3], [4, 5, 6]])
a = [[1,2,3],[4,5,6]]
json_dump = json.dumps({'a': a, 'aa': [2, (2, 3, 4), a], 'bb': [2]})
#d = json.dumps(c)
print(json_dump) e