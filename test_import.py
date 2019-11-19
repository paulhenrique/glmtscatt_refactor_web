import json
#import numpy as np


#a = np.array([[1, 2, 3], [4, 5, 6]])
# a = [[1,2,3],[4,5,6]]
def test_json_array():
    a = []
    for i in range(0,100):
        #a.append(np.random.randint(1000))
        a.append(i)

    # json_dump = json.dumps({'a': a, 'aa': [2, (2, 3, 4), a], 'bb': [2]})
    b = {
        'conteudo':a
    }
    c = json.dumps(b)
    print(c)