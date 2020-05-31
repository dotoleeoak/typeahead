from queue import PriorityQueue
import time

MIN = 0
MAX = 100_000_000
NUM_DATA = 1 << 20


def k_sort():
    with open("data.txt", "r") as fr:
        for i in range(1024):
            temp = []
            for j in range(1024):
                temp.append(int(fr.readline()))
            temp.sort()
            with open(f"part/temp{i}.txt", "w") as fa:
                fa.write("\n".join([str(num) for num in temp]))


def merge():
    f_list = []
    pq = PriorityQueue()
    for i in range(1024):
        fr = open(f"part/temp{i}.txt", "r")
        min_num = int(fr.readline())
        pq.put((min_num, i))
        f_list.append(fr)

    with open("result.txt", "w") as fw:
        while not pq.empty():
            min_num, idx = pq.get()
            fw.write(f"{min_num}\n")
            line = f_list[idx].readline()
            if line:
                pq.put((int(line), idx))


def check_sorted():
    with open("result.txt", "r") as f:
        num_prev = int(f.readline())
        for i in range(NUM_DATA - 1):
            num_cur = int(f.readline())
            if num_prev > num_cur:
                return False
            num_prev = num_cur
    return True


if __name__ == "__main__":
    start = time.time()
    k_sort()
    print(f"time - k_sort() : {round(time.time() - start, 2)} sec")

    start = time.time()
    merge()
    print(f"time - merge() : {round(time.time() - start, 2)} sec")

    is_sorted = check_sorted()
    if is_sorted:
        print("Sorting success")
    else:
        print("failed...")
