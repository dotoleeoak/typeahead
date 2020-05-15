from collections import defaultdict
from heapq import heappush, heappushpop
import re
import json
import time

def tokenize(txt_file: str):
    with open(txt_file, 'r') as f:
        lines = f.readlines()
    n_keys = defaultdict(int)

    for line in lines:
        words_all = re.split(r'\W', line)
        words = filter(None, words_all)
        for word in words:
            n_keys[word.lower()] += 1

    with open("word-count.txt", 'w') as f:
        json.dump(n_keys, f, indent=4, sort_keys=True)
    
def build_index(pq_size: int):
    with open("word-count.txt", 'r') as f:
        data = json.load(f)
    items = data.items()
    index = defaultdict(list)

    for word, count in items:
        for i in range(5):
            if i == len(word):
                break
            prefix = word[:i+1]
            if len(index[prefix]) < pq_size:
                heappush(index[prefix], (count, word))
            else:
                heappushpop(index[prefix], (count, word))

    localtime = time.localtime(time.time())
    version = time.strftime('%c', localtime)
    fw = open("index.txt", 'w')
    fw.write("Index Version: " + version + '\n')
    fw.write("PriorityQueue Size: " + str(pq_size) + '\n\n')

    items = index.items()
    for prefix, pq in items:
        fw.write(prefix + ' ')
        pq.reverse()
        for i in pq:
            fw.write(i[1] + ' ')
        fw.write('\n')
    fw.close()

def main(command: str):
    with open("index.txt", 'r') as f:
        lines = f.readlines()
    data = lines[3:]
    typeahead = defaultdict(list)

    for line in data:
        words = line.split()
        prefix = words[0]
        typeahead[prefix] = words[1:]

    ret = []
    words = command.split()
    for prefix in words:
        ret.append(typeahead[prefix])
    return ret

if __name__ == "__main__":
    txt_file = input()
    tokenize(txt_file)
    build_index(5)
    command = input()
    result = main(command)
    for i in result:
        print(i)
