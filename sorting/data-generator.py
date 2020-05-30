import random

MIN = 0
MAX = 100_000_000
NUM_DATA = 1 << 20

if __name__ == "__main__":
    with open("data.txt", "w") as f:
        for i in range(NUM_DATA):
            f.write(f"{random.randint(MIN, MAX)}\n")
