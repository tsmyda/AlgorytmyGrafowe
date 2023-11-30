from dimacs import *
import os
from queue import PriorityQueue
from collections import deque
import time


def run_tests(function, graph_dir, to_continue = None):
    print(f"Testing {function.__name__} function")
    print("=========================================")
    test_counter = 0
    errors = 0
    START = time.time()
    for path in os.listdir(graph_dir):
        if to_continue is not None and path in to_continue: 
            print(f"Graph {path} - skipped")
            continue
        file_path = os.path.join(graph_dir, path)
        if os.path.isfile(file_path):
            test_counter+=1
            try:
                with open(file_path, 'r') as file:
                    line = file.readline()
                    expected_answer = int(line.split()[-1])
                    start_local = time.time()
                    answer = function(file_path)
                    stop_local = time.time()
                    diff = round(stop_local-start_local,3)
                    if answer != expected_answer:
                        result = f"Wrong answer - expected: {expected_answer}, found: {answer}. Time: {diff} s"
                        errors+=1
                    else:
                        result = f"Correct answer: {answer}. Time: {diff} s"
            except:
                result = "Execute error or no answer"
                errors+=1
            print(f"Graph {path} - {result}")
    END = time.time()
    print("=========================================")
    print(f"Score: {test_counter-errors}/{test_counter}")
    print(f"Total time: {round(END-START,3)} s")
    print("\n\n")
    