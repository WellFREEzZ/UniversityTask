import os
import pandas as pd

set_path = os.path.join(os.path.dirname(__file__), 'set')
ext = '.txt'

fst_iter = True
for f in os.listdir(set_path):
    if os.path.isfile(os.path.join(set_path, f)) and ext in str(f):
        file = os.path.join(set_path, f)
    else:
        continue
    with open(file, 'r') as fl:
        if fst_iter:
            result = pd.read_csv(fl)
            fst_iter = False
            continue
        else:
            nxt = pd.read_csv(fl)
    result = result.append(nxt, ignore_index=True)

    print(len(result.index))

with open('out.csv', 'w') as f:
    result.to_csv(f)
