import os
import re
import json
import time

from collections import Counter, defaultdict
from heapq import heappush, heappushpop
from typeahead.convert_unicode import convert


class BuildIndex:
    def __init__(self, dir_input, dir_output, version, heap_size, prefix_size):
        self.version = 0
        self.dir_input = dir_input
        self.dir_output = dir_output
        self.heap_size = heap_size
        self.prefix_size = prefix_size
        self.typeahead = defaultdict(list)
        if not os.path.exists(self.dir_output):
            os.mkdir(self.dir_output)

    def tokenize(self):
        with open(self.dir_input, "r") as f:
            data = f.read()
            words_all = re.split(r"\W", data)
            words = filter(None, words_all)
            words = [convert(word) for word in words]
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
        if not os.path.exists(self.dir_output):
            os.mkdir(self.dir_output)
        path = os.path.join(self.dir_output, str(self.version))
        if not os.path.exists(path):
            os.mkdir(path)
        path = os.path.join(path, "batch.txt")
        with open(path, "w") as f:
            f.write(f"Index Version: {self.version}\n")
            f.write(f"PriorityQueue Size: {self.heap_size}\n")
            items = index.items()
            for prefix, heap in items:
                f.write("\n" + prefix + " ")
                heap.reverse()
                for ele in heap:
                    f.write(ele[1] + " ")

    def read_index(self):
        path = os.path.join(self.dir_output, str(self.version), "batch.txt")
        if not os.path.exists(path):
            self.tokenize()
            self.build_index()
        with open(path, "r") as f:
            lines = f.readlines()[3:]
            for line in lines:
                words = line.split()
                prefix = words[0]
                self.typeahead[prefix] = words[1:]

    def search(self, prefix):
        return self.typeahead[convert(prefix)]

    def reload(self):
        path = os.path.join(self.dir_output, str(self.version + 1))
        path_update = os.path.join(path, "update.txt")
        path_delete = os.path.join(path, "delete.txt")
        path_batch = os.path.join(path, "batch.txt")
        if os.path.exists(path_update):
            with open(path_update, "r") as f:
                lines = f.readlines()
                for line in lines:
                    item = line.split()
                    self.typehead[item[0]] = item[1:]

        if os.path.exists(path_delete):
            with open(path_delete, "r") as f:
                lines = f.readlines()
                for line in lines:
                    item = line.split()
                    self.typeahead[item[0]] = item[1:]

        if os.path.exitst(path):
            self.version += 1
            with open(path_batch, "w") as f:
                f.write(f"Index Version: {self.version}\n")
                f.write(f"PriorityQueue Size: {self.heap_size}\n")
                for key, value in typeahead:
                    f.write("\n" + " ".join([key] + value))

    def update(self, prefix, words):
        self.typeahead[prefix] = words
        path = os.path.join(self.dir_output, str(self.version + 1))
        if not os.path.exists(path):
            os.mkdir(path)
        path = os.path.join(path, "update.txt")
        with open(path, "a") as f:
            f.write(" ".join([prefix] + self.typeahead[prefix]) + "\n")

    def delete(self, prefix, words):
        self.typeahead[prefix] = [
            word for word in self.typeahead[prefix] if word not in words
        ]
        path = os.path.join(self.dir_output, str(self.version + 1))
        if not os.path.exists(path):
            os.mkdir(path)
        path = os.path.join(path, "delete.txt")
        with open(path, "a") as f:
            f.write(" ".join([prefix] + self.typeahead[prefix]) + "\n")
