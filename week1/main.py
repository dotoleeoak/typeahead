from collections import defaultdict
from queue import PriorityQueue
from typing import List
import re
import json
import time

def tokenize():
    with open("1342-0.txt", 'r') as f:
        lines = f.readlines()
    n_keys = defaultdict(int)

    for line in lines:
        words_all = re.split('\W', line)
        words = filter(None, words_all)
        for word in words:
            n_keys[word.lower()] += 1

    with open("word-count.txt", 'w') as f:
        json.dump(n_keys, f, indent=4, sort_keys=True)
    
def build_index(pq_size: int):
    with open("word-count.txt", 'r') as f:
        data = json.load(f)
    items = data.items()
    index = defaultdict(PriorityQueue)

    for word, count in items:
        for i in range(5):
            if i == len(word):
                break
            prefix = word[:i+1]
            index[prefix].put((-count, word))

    localtime = time.localtime(time.time())
    version = time.strftime('%c', localtime)
    fw = open("index.txt", 'w')
    fw.write("Index Version: " + version + '\n')
    fw.write("PriorityQueue Size: " + str(pq_size) + '\n\n')

    items = index.items()
    for prefix, pq in items:
        fw.write(prefix + ' ')
        for i in range(pq_size):
            if pq.empty():
                break
            fw.write(pq.get()[1] + ' ')
        fw.write('\n')
    fw.close()

if __name__ == "__main__":
    tokenize()
    build_index(5)

    with open("index.txt", 'r') as f:
        lines = f.readlines()
    data = lines[3:]
    typeahead = defaultdict(List)

    for line in data:
        words = line.split()
        prefix = words[0]
        typeahead[prefix] = words[1:]

    p = re.compile('\w*')
    while True:
        prefix = input()
        if not p.match(prefix):
            break
        print(typeahead[prefix])
