from heapClass import Heap


my_heap = Heap(3)
my_heap.add(5, 5)
my_heap.add(8, 8)
my_heap.add(10, 10)
my_heap.add(4, 4)
my_heap.add(2, 2)
my_heap.add(1, 1)
my_heap.add(3, 3)
my_heap.add(6, 6)
my_heap.add(7, 7)

print("---" * 15)
print(my_heap)

print(my_heap.pop())
print("---" * 15)
print(my_heap)
print(my_heap.pop())

print("---" * 15)
print(my_heap)
print(my_heap.pop())
print(my_heap.pop())

print("---" * 15)
print(my_heap)