from typing import Any
from collections import defaultdict
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'shakespeare')
file_list = os.listdir(file_path)
data: str
pairs: list[Any] = list()
for i in file_list:
    file_string: str = 'shakespeare/'+str(i)
    new_file_path = os.path.join(base_dir, file_string)
    with open(new_file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        #Map phase: split into (word, 1) pairs
        localpairs = [(w, 1) for w in data.split()]
        pairs = pairs + localpairs


#Tiny MapReduce-style word count (map -< reduce), single-process demo
counts: Any = defaultdict(int)

for w,c in pairs:
    counts[w] += c

sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1]))

for w in sorted_dict:
    print(w, counts[w])
