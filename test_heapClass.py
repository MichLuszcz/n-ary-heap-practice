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

def test_add_to_a_heap_when_need_to_hapify_2():
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

def test_get_children_indicies_2():
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

def test_pop_from_heap_2():
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

# 5 arity heap tests

def test_add_to_a_heap_when_need_to_hapify_5():
    my_heap = Heap(5)
    my_heap.add(35)
    my_heap.add(24)
    my_heap.add(12)
    my_heap.add(20)
    my_heap.add(30)
    my_heap.add(11)
    my_heap.add(10)
    my_heap.add(49)
    my_heap.add(29)
    my_heap.add(36)
    assert my_heap.get_internal_tab() == [49, 36, 12, 20, 30, 11, 10, 24, 29, 35]

def test_get_children_indicies_5():
    my_heap = Heap(5)
    my_heap.add(35)
    my_heap.add(24)
    my_heap.add(12)
    my_heap.add(20)
    my_heap.add(30)
    my_heap.add(11)
    my_heap.add(10)
    my_heap.add(49)
    my_heap.add(29)
    my_heap.add(36)
    assert my_heap.get_children_indices(0) == [1, 2, 3, 4, 5]
    assert my_heap.get_children_indices(1) == [6, 7, 8, 9]
    assert my_heap.get_children_indices(2) == []
    assert my_heap.get_children_indices(3) == []

def test_pop_from_heap_5():
    my_heap = Heap(5)
    my_heap.add(35)
    my_heap.add(24)
    my_heap.add(12)
    my_heap.add(20)
    my_heap.add(30)
    my_heap.add(11)
    my_heap.add(10)
    my_heap.add(49)
    my_heap.add(29)
    my_heap.add(36)
    my_heap.pop()
    assert my_heap.get_internal_tab() == [36, 35, 12, 20, 30, 11, 10, 24, 29]

# 7 arity heap tests

def test_add_to_a_heap_when_need_to_hapify_7():
    my_heap = Heap(7)
    my_heap.add(35)
    my_heap.add(24)
    my_heap.add(12)
    my_heap.add(20)
    my_heap.add(30)
    my_heap.add(11)
    my_heap.add(10)
    my_heap.add(49)
    my_heap.add(29)
    my_heap.add(76)
    assert my_heap.get_internal_tab() == [76, 49, 12, 20, 30, 11, 10, 35, 24, 29]

def test_get_children_indicies_7():
    my_heap = Heap(7)
    my_heap.add(35)
    my_heap.add(24)
    my_heap.add(12)
    my_heap.add(20)
    my_heap.add(30)
    my_heap.add(11)
    my_heap.add(10)
    my_heap.add(49)
    my_heap.add(29)
    my_heap.add(76)
    assert my_heap.get_children_indices(0) == [1, 2, 3, 4, 5, 6, 7]
    assert my_heap.get_children_indices(1) == [8, 9]
    assert my_heap.get_children_indices(2) == []
    assert my_heap.get_children_indices(3) == []

def test_pop_from_heap_7():
    my_heap = Heap(7)
    my_heap.add(35)
    my_heap.add(24)
    my_heap.add(12)
    my_heap.add(20)
    my_heap.add(30)
    my_heap.add(11)
    my_heap.add(10)
    my_heap.add(49)
    my_heap.add(29)
    my_heap.add(76)
    my_heap.add(7)
    my_heap.pop()
    assert my_heap.get_internal_tab() == [49, 29, 12, 20, 30, 11, 10, 35, 24, 7]