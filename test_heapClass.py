from heapClass import Heap
import pytest
# 2 arity heaps tests

def test_add_elements_to_a_heap_basic():
    my_heap = Heap(2)
    my_heap.add(12)
    my_heap.add(11)
    my_heap.add(9)
    my_heap.add(8)
    my_heap.add(10)
    my_heap.add(6)
    my_heap.add(5)
    my_heap.add(6)
    my_heap.add(7)
    my_heap.add(9)
    my_heap.add(3)
    my_heap.add(5)
    my_heap.add(4)
    my_heap.add(3)
    assert my_heap.get_internal_tab() == [12, 11, 9, 8, 10, 6, 5, 6, 7, 9, 3, 5, 4, 3]

def test_add_to_a_heap_when_need_to_hapify():
    my_heap = Heap(2)
    my_heap.add(35)
    my_heap.add(24)
    my_heap.add(12)
    my_heap.add(20)
    my_heap.add(30) # element bigger than parent
    my_heap.add(11)
    my_heap.add(10)
    my_heap.add(49) # same
    my_heap.add(29)
    my_heap.add(36) # again
    assert my_heap.get_internal_tab() == [49, 36, 12, 30, 35, 11, 10, 20, 29, 24]

def test_get_children_indicies():
    my_heap = Heap(2)
    my_heap.add(12)
    my_heap.add(11)
    my_heap.add(9)
    my_heap.add(8)
    my_heap.add(10)
    my_heap.add(6)
    my_heap.add(5)
    my_heap.add(6)
    my_heap.add(7)
    my_heap.add(9)
    assert my_heap.get_children_indices(0) == [1, 2]
    assert my_heap.get_children_indices(1) == [3, 4]
    assert my_heap.get_children_indices(2) == [5, 6]
    assert my_heap.get_children_indices(3) == [7, 8]

def test_pop_from_heap():
    my_heap = Heap(2)
    my_heap.add(35)
    my_heap.add(24)
    my_heap.add(12)
    my_heap.add(20)
    my_heap.add(30) # element bigger than parent
    my_heap.add(11)
    my_heap.add(10)
    my_heap.add(49) # same
    my_heap.add(29)
    my_heap.add(36)
    my_heap.pop()
    assert my_heap.get_internal_tab() == [36, 35, 12, 30, 24, 11, 10, 20, 29]