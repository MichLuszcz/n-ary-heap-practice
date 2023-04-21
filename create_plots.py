from heapClass import Heap
from matplotlib import pyplot as plt
import time
import gc
import random

def create_heap(arity, collection_to_use:list):
    if arity == 2:
        my_heap = Heap(2)
        for number in(collection_to_use):
            my_heap.add(number)
    if arity == 5:
        my_heap = Heap(5)
        for number in(collection_to_use):
            my_heap.add(number)
    if arity == 7:
        my_heap = Heap(7)
        for number in(collection_to_use):
            my_heap.add(number)
    return my_heap


def delete_from_a_heap(heap:Heap, collection_to_use:list):
    for _ in collection_to_use:
        heap.pop()

def measure_time(arity, collection:list) -> tuple:
    if len(collection) == 0:
        return 0, 0
    creation_time = 0
    removal_time = 0
    gc_old = gc.isenabled()
    gc.disable()
    # measuring creation time
    start = time.process_time()
    heap_created = create_heap(arity, collection)
    stop = time.process_time()
    # save time
    creation_time += stop - start
    # measuring removal time
    start = time.process_time()
    delete_from_a_heap(heap_created, collection)
    stop = time.process_time()
    # save time
    removal_time += stop - start
    if gc_old:
        gc.enable()
    return creation_time, removal_time



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
        for n in range(0, 10001, 1000):
            n_tested.append(n)
            tested = entry_list[:n]
            heap_times = measure_time(c_arity, tested)
            if c_arity == 2:
                time_to_create_2_arity.append(heap_times[0])
                time_to_remove_2_arity.append(heap_times[1])
            if c_arity == 5:
                time_to_create_5_arity.append(heap_times[0])
                time_to_remove_5_arity.append(heap_times[1])
            if c_arity == 7:
                time_to_create_7_arity.append(heap_times[0])
                time_to_remove_7_arity.append(heap_times[1])

    # 2 arity heap plot
    plt.plot(n_tested[:11], time_to_create_2_arity, color = 'g', label = 'creation')
    plt.plot(n_tested[:11], time_to_remove_2_arity, color = 'r', label = 'removing')
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("2 Heap time")
    plt.clf()

    # 5 arity heap plot
    plt.plot(n_tested[11:22], time_to_create_5_arity, color = 'g', label = 'creation')
    plt.plot(n_tested[11:22], time_to_remove_5_arity, color = 'r', label = 'removing')
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("5 Heap time")
    plt.clf()

    # 7 arity heap plot
    plt.plot(n_tested[22:], time_to_create_7_arity, color = 'g', label = 'creation')
    plt.plot(n_tested[22:], time_to_remove_7_arity, color = 'r', label = 'removing')
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("7 Heap time")
    plt.clf()



if __name__ == "__main__":
    random_numbers = random.sample(range(1, 30000), 10000)
    create_heap_figures(random_numbers)