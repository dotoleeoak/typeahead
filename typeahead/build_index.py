import re
import json
import time

from collections import Counter, defaultdict
from heapq import heappush, heappushpop


class BuildIndex:
    def __init__(self, dir_input, dir_output, version, heap_size, prefix_size):
        # localtime = time.localtime(time.time())
        # self.version = time.strftime("%c", localtime)
        self.version = 0
        self.dir_input = dir_input
        self.dir_output = dir_output
        self.heap_size = heap_size
        self.prefix_size = prefix_size
        self.typeahead = defaultdict(list)

    def tokenize(self):
        with open(self.filename, "r") as f:
            data = f.read()
            words_all = re.split(r"\W", data)
            words = filter(None, words_all)
            n_keys = Counter(words)
        with open("word-count.txt", "w") as f:
            json.dump(n_keys, f, indent=4, sort_keys=True)

    def build_index(self):
        with open("word-count.txt", "r") as f:
            data = json.load(f)
            items = data.items()
            index = defaultdict(list)
        for word, count in items:
            for i in range(5):
                if i == len(word):
                    break
                prefix = word[: i + 1]
                if len(index[prefix]) < self.heap_size:
                    heappush(index[prefix], (count, word))
                else:
                    heappushpop(index[prefix], (count, word))
        with open(, "w") as f:
            f.write(f"Index Version: {self.version}\n")
            f.write(f"PriorityQueue Size: {self.heap_size}\n")
            items = index.items()
            for prefix, heap in items:
                f.write("\n" + prefix + " ")
                heap.reverse()
                for ele in heap:
                    f.write(ele[1] + " ")

    def read_index(self):
        with open("index.txt", "r") as f:
            lines = f.readlines()[3:]
            for line in lines:
                words = line.split()
                prefix = words[0]
                self.typeahead[prefix] = words[1:]

    def search(self, prefix):
        return self.typeahead[prefix]

    def reload(self):
        pass

    def update(self, prefix, words):
        self.typeahead[prefix] = word
        with open(app.config["DIR_UPDATE"], "a") as f:
            self.version += 1
            f.write(self.version + " " + str({prefix: self.typeahead[prefix]}) + "\n")

    def delete(self, prefix, words):
        self.typeahead[prefix] = [
            word for word in self.typeahead[prefix] if word not in words
        ]
        with open(app.config["DIR_UPDATE"], "a") as f:
            self.version += 1
            f.write(self.version + " " + str({prefix: self.typeahead[prefix]}) + "\n")
