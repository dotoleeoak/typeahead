import re
import json
import time

from collections import Counter, defaultdict
from heapq import heappush, heappushpop


class BuildIndex:
    def __init__(self, **kwargs):
        localtime = time.localtime(time.time())
        self.version = time.strftime('%c', localtime)
        self.filename = kwargs["filename"]
        self.heap_size = kwargs["heap_size"]
        self.prefix_size = kwargs["prefix_size"]
        self.typeahead = defaultdict(list)

    def tokenize(self):
        with open(self.filename, 'r') as f:
            data = f.read()
            words_all = re.split(r'\W', data)
            words = filter(None, words_all)
            n_keys = Counter(words)
        with open("word-count.txt", 'w') as f:
            json.dump(n_keys, f, indent=4, sort_keys=True)

    def build_index(self):
        with open("word-count.txt", 'r') as f:
            data = json.load(f)
            items = data.items()
            index = defaultdict(list)
        for word, count in items:
            for i in range(5):
                if i == len(word):
                    break
                prefix = word[:i+1]
                if len(index[prefix]) < self.heap_size:
                    heappush(index[prefix], (count, word))
                else:
                    heappushpop(index[prefix], (count, word))
        with open("index.txt", 'w') as f:
            f.write(f"Index Version: {self.version}\n")
            f.write(f"PriorityQueue Size: {self.heap_size}\n")
            items = index.items()
            for prefix, heap in items:
                f.write('\n' + prefix + ' ')
                heap.reverse()
                for ele in heap:
                    f.write(ele[1] + ' ')

    def read_index(self):
        with open("index.txt", 'r') as f:
            lines = f.readlines()[3:]
            for line in lines:
                words = line.split()
                prefix = words[0]
                self.typeahead[prefix] = words[1:]
