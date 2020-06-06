import os
import re
import json
import time

from collections import Counter, defaultdict
from heapq import heappush, heappushpop


class BuildIndex:
    def __init__(self, dir_input, dir_output, version, heap_size, prefix_size):
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
        # TODO: fix dir_output
        with open(self.dir_output, "w") as f:
            f.write(f"Index Version: {self.version}\n")
            f.write(f"PriorityQueue Size: {self.heap_size}\n")
            items = index.items()
            for prefix, heap in items:
                f.write("\n" + prefix + " ")
                heap.reverse()
                for ele in heap:
                    f.write(ele[1] + " ")

    def read_index(self):
        # TODO: fix dir_output
        with open(self.dir_output, "r") as f:
            lines = f.readlines()[3:]
            for line in lines:
                words = line.split()
                prefix = words[0]
                self.typeahead[prefix] = words[1:]

    def search(self, prefix):
        return self.typeahead[prefix]

    def reload(self):
        path = os.path.join(self.dir_output, str(self.version + 1))
        # TODO: maybe update/delete.txt is better to make configuration
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
            with open(path_batch, "w") as f:
                # TODO: just one method to write typeahead
                f.write(f"Index Version: {self.version}\n")
                f.write(f"PriorityQueue Size: {self.heap_size}\n")
                for key, value in typeahead:
                    f.write("\n" + " ".join([key] + value))

    def update(self, prefix, words):
        self.typeahead[prefix] = words
        try:
            path = os.path.join(self.dir_output, str(self.version + 1))
            os.mkdir(path)
        except OSError:
            pass
        finally:
            path = os.path.join(path, "update.txt")
            with open(path, "a") as f:
                f.write(" ".join([prefix] + self.typeahead[prefix]) + "\n")

    def delete(self, prefix, words):
        self.typeahead[prefix] = [
            word for word in self.typeahead[prefix] if word not in words
        ]
        try:
            path = os.path.join(self.dir_output, str(self.version + 1))
            os.mkdir(path)
        except OSError:
            pass
        finally:
            path = os.path.join(path, "delete.txt")
            with open(path, "a") as f:
                f.write(" ".join([prefix] + self.typeahead[prefix]) + "\n")
