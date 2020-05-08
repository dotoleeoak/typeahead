from collections import defaultdict
from queue import PriorityQueue
from typing import List
import re
import json
import time

def tokenize():
    fr = open("1342-0.txt", "r")
    fw = open("word-count.txt", "w")

    n_keys = defaultdict(int)
    lines = fr.readlines()

    for line in lines:
        words_all = re.split('\W', line)
        words = filter(None, words_all)
        for word in words:
            n_keys[word.lower()] += 1

    json.dump(n_keys, fw, indent=4, sort_keys=True)
    fr.close()
    fw.close()
    
def build_index(pq_size: int):
    fr = open("word-count.txt", 'r')
    fw = open("index.txt", 'w')

    index = defaultdict(PriorityQueue)
    data = json.load(fr)
    items = data.items()

    for word, count in items:
        for i in range(5):
            if i == len(word):
                break
            prefix = word[:i+1]
            index[prefix].put((-count, word))

    localtime = time.localtime(time.time())
    version = time.strftime('%c', localtime)
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

    fr.close()
    fw.close()

if __name__ == "__main__":
    tokenize()
    build_index()

    f = open("index.txt", 'r')
    lines = f.readlines()
    data = lines[3:]
    typeahead = defaultdict(List)

    for line in data:
        words = line.split()
        prefix = words[0]
        typeahead[prefix] = words[1:]

    prefix = input()
    print(typeahead[prefix])
    f.close()
