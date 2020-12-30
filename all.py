#!/usr/bin/env python3
from importlib import import_module
import time
import sys
import pickle

if __name__ == "__main__":
    times = []
    for d in range(1,26):
        with open(f"day{d}.txt") as f:
            problem = list(map(lambda line: line.strip(), f.readlines()))
        day = import_module(f"day{d}")
        start = time.perf_counter()
        print(f"Running day{d} part1: {day.part1(problem)}")
        middle = time.perf_counter()
        print(f"Running day{d} part2: {day.part2(problem)}")
        end = time.perf_counter()
        times.append(middle-start)
        times.append(end-middle)
    with open(f"times_{sys.executable.split('/')[-1]}.pkl", "wb") as f:
        pickle.dump(times, f)
