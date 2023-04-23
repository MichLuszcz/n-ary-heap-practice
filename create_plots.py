from heapClass import Heap
from matplotlib import pyplot as plt
import time
import gc
import random

def create_heap(arity, collection_to_use:list):
    if arity == 2:
        my_heap = Heap(2)
        for index, number in enumerate(collection_to_use):
            my_heap.add(number, index)
    if arity == 5:
        my_heap = Heap(5)
        for index, number in enumerate(collection_to_use):
            my_heap.add(number, index)
    if arity == 7:
        my_heap = Heap(7)
        for index, number in enumerate(collection_to_use):
            my_heap.add(number, index)
    return my_heap


def measure_removal_time(heap:Heap, n_of_pops:int) -> list:
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for _ in range(n_of_pops + 1):
        heap.pop()
    stop = time.process_time()
    if gc_old:
        gc.enable()
    removal_time = stop - start
    return removal_time

def measure_creation_time(arity, collection:list) -> int:
    if len(collection) == 0:
        return 0
    creation_time = 0
    gc_old = gc.isenabled()
    gc.disable()
    # measuring creation time
    start = time.process_time()
    heap_created = create_heap(arity, collection)
    stop = time.process_time()
    # save time
    creation_time += stop - start
    if gc_old:
        gc.enable()
    return creation_time



def create_heap_figures(entry_list:list):
    n_tested = []
    time_to_create_2_arity = []
    time_to_remove_2_arity = []
    time_to_create_5_arity = []
    time_to_remove_5_arity = []
    time_to_create_7_arity = []
    time_to_remove_7_arity = []
    arity_list = [2, 5, 7]
    for c_arity in arity_list:
        for n in range(0, 100001, 10000):
            n_tested.append(n)
            tested = entry_list[:n]
            heap_times = measure_creation_time(c_arity, tested)
            if c_arity == 2:
                time_to_create_2_arity.append(heap_times)
            if c_arity == 5:
                time_to_create_5_arity.append(heap_times)
            if c_arity == 7:
                time_to_create_7_arity.append(heap_times)

    for n in range(0, 100001, 10000):
        if n == 0:
            time_to_remove_2_arity.append(0)
        else:
            my_heap = create_heap(2, entry_list)
            time_to_remove_2_arity.append(measure_removal_time(my_heap, n))
    for n in range(0, 100001, 10000):
        if n == 0:
            time_to_remove_5_arity.append(0)
        else:
            my_heap = create_heap(5, entry_list)
            time_to_remove_5_arity.append(measure_removal_time(my_heap, n))
    for n in range(0, 100001, 10000):
        if n == 0:
            time_to_remove_7_arity.append(0)
        else:
            my_heap = create_heap(7, entry_list)
            time_to_remove_7_arity.append(measure_removal_time(my_heap, n))

    # creation plots
    plt.plot(n_tested[:11], time_to_create_2_arity, color = 'g', label = "2 arity")
    plt.plot(n_tested[11:22], time_to_create_5_arity, color = 'r', label = "5 arity")
    plt.plot(n_tested[22:], time_to_create_7_arity, color = 'b', label = "7 arity")
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("Heaps creation times")
    plt.clf()

    # removing from big plots
    plt.plot(n_tested[:11], time_to_remove_2_arity, color = 'g', label = "2 arity")
    plt.plot(n_tested[11:22], time_to_remove_5_arity, color = 'r', label = "5 arity")
    plt.plot(n_tested[22:], time_to_remove_7_arity, color = 'b', label = "7 arity")
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("Heaps removal times")
    plt.clf()


if __name__ == "__main__":
    random_numbers = random.sample(range(1, 300000), 100000)
    create_heap_figures(random_numbers)