from heapClass import Heap
import pytest
# 2 arity heaps tests

def test_add_elements_to_a_heap_basic():
    my_heap = Heap(2)
    my_heap.add(12, 12)
    my_heap.add(11, 11)
    my_heap.add(9, 9)
    my_heap.add(8, 8)
    my_heap.add(10, 10)
    my_heap.add(6, 6)
    my_heap.add(5, 5)
    my_heap.add(6, 6)
    my_heap.add(7, 7)
    my_heap.add(9, 9)
    my_heap.add(3, 3)
    my_heap.add(5, 5)
    my_heap.add(4, 4)
    my_heap.add(3, 3)

    assert my_heap.get_internal_tab() == [(12, 12), (11, 11), (9, 9), (8, 8), (10, 10), (6, 6), (5, 5), (6, 6), (7, 7), (9, 9), (3, 3), (5, 5), (4, 4), (3, 3)]

def test_add_to_a_heap_when_need_to_hapify_2():
    my_heap = Heap(2)
    my_heap.add(35, 35)
    my_heap.add(24, 24)
    my_heap.add(12, 12)
    my_heap.add(20, 20)
    my_heap.add(30, 30) # element bigger than parent
    my_heap.add(11, 11)
    my_heap.add(10, 10)
    my_heap.add(49, 49) # same
    my_heap.add(29, 29)
    my_heap.add(36, 36) # again

    assert my_heap.get_internal_tab() == [(49, 49), (36, 36), (12, 12), (30, 30), (35, 35), (11, 11), (10, 10), (20, 20), (29, 29), (24, 24)]

def test_get_children_indicies_2():
    my_heap = Heap(2)
    my_heap.add(12, 12)
    my_heap.add(11, 11)
    my_heap.add(9, 9)
    my_heap.add(8, 8)
    my_heap.add(10, 10)
    my_heap.add(6, 6)
    my_heap.add(5, 5)
    my_heap.add(6, 6)
    my_heap.add(7, 7)
    my_heap.add(9, 9)

    assert my_heap.get_children_indices(0) == [1, 2]
    assert my_heap.get_children_indices(1) == [3, 4]
    assert my_heap.get_children_indices(2) == [5, 6]
    assert my_heap.get_children_indices(3) == [7, 8]

def test_pop_from_heap_2():
    my_heap = Heap(2)
    my_heap.add(35, 35)
    my_heap.add(24, 24)
    my_heap.add(12, 12)
    my_heap.add(20, 20)
    my_heap.add(30, 30) # element bigger than parent
    my_heap.add(11, 11)
    my_heap.add(10, 10)
    my_heap.add(49, 49) # same
    my_heap.add(29, 29)
    my_heap.add(36, 36)


    my_heap.pop()

    assert my_heap.get_internal_tab() == [(36, 36), (35, 35), (12, 12), (30, 30), (24, 24), (11, 11), (10, 10), (20, 20), (29, 29)]

# 5 arity heap tests

def test_add_to_a_heap_when_need_to_hapify_5():
    my_heap = Heap(5)
    my_heap.add(35, 35)
    my_heap.add(24, 24)
    my_heap.add(12, 12)
    my_heap.add(20, 20)
    my_heap.add(30, 30)
    my_heap.add(11, 11)
    my_heap.add(10, 10)
    my_heap.add(49, 49)
    my_heap.add(29, 29)
    my_heap.add(36, 36)
    assert my_heap.get_internal_tab() == [(49, 49), (36, 36), (12, 12), (20, 20), (30, 30), (11, 11), (10, 10), (24, 24), (29, 29), (35, 35)]

def test_get_children_indicies_5():
    my_heap = Heap(5)
    my_heap.add(35, 35)
    my_heap.add(24, 24)
    my_heap.add(12, 12)
    my_heap.add(20, 20)
    my_heap.add(30, 30)
    my_heap.add(11, 11)
    my_heap.add(10, 10)
    my_heap.add(49, 49)
    my_heap.add(29, 29)
    my_heap.add(36, 36)
    #
    assert my_heap.get_children_indices(0) == [1, 2, 3, 4, 5]
    assert my_heap.get_children_indices(1) == [6, 7, 8, 9]
    assert my_heap.get_children_indices(2) == []
    assert my_heap.get_children_indices(3) == []

def test_pop_from_heap_5():
    my_heap = Heap(5)

    my_heap.add(35, 35)
    my_heap.add(24, 24)
    my_heap.add(12, 12)
    my_heap.add(20, 20)
    my_heap.add(30, 30)
    my_heap.add(11, 11)
    my_heap.add(10, 10)
    my_heap.add(49, 49)
    my_heap.add(29, 29)
    my_heap.add(36, 36)
    my_heap.pop()

    assert my_heap.get_internal_tab() == [(36, 36), (35, 35), (12, 12), (20, 20), (30, 30), (11, 11), (10, 10), (24, 24), (29, 29)]

# 7 arity heap tests

def test_add_to_a_heap_when_need_to_hapify_7():
    my_heap = Heap(7)
    my_heap.add(35, 35)
    my_heap.add(24, 24)
    my_heap.add(12, 12)
    my_heap.add(20, 20)
    my_heap.add(30, 30)
    my_heap.add(11, 11)
    my_heap.add(10, 10)
    my_heap.add(49, 49)
    my_heap.add(29, 29)
    my_heap.add(76, 76)

    assert my_heap.get_internal_tab() == [(76, 76), (49, 49), (12, 12), (20, 20), (30, 30), (11, 11), (10, 10), (35, 35), (24, 24), (29, 29)]

def test_get_children_indicies_7():
    my_heap = Heap(7)

    my_heap.add(35, 35)
    my_heap.add(24, 24)
    my_heap.add(12, 12)
    my_heap.add(20, 20)
    my_heap.add(30, 30)
    my_heap.add(11, 11)
    my_heap.add(10, 10)
    my_heap.add(49, 49)
    my_heap.add(29, 29)
    my_heap.add(76, 76)


    assert my_heap.get_children_indices(0) == [1, 2, 3, 4, 5, 6, 7]
    assert my_heap.get_children_indices(1) == [8, 9]
    assert my_heap.get_children_indices(2) == []
    assert my_heap.get_children_indices(3) == []

def test_pop_from_heap_7():
    my_heap = Heap(7)
    my_heap.add(35, 35)
    my_heap.add(24, 24)
    my_heap.add(12,  12)
    my_heap.add(20, 20)
    my_heap.add(30,  30)
    my_heap.add(11,   11)
    my_heap.add(10,  10)
    my_heap.add(49,  49)
    my_heap.add(29, 29)
    my_heap.add(76, 76)
    my_heap.add(7, 7)
    my_heap.pop()
    assert my_heap.get_internal_tab() == [(49,  49), (29, 29), (12,  12),
                                          (20, 20), (30,  30), (11,   11),
                                          (10,  10), (35, 35), (24, 24), (7, 7)]