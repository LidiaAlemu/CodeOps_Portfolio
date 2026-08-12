import time
from collections import deque


# 1. Name the Big-O for each snippet (write as comments)

# (a) Accessing a list by index
first = [10, 20, 30][0]          # O(1) – constant time

# (b) Single loop over n items
for item in range(100):          # O(n) – linear in n
    pass

# (c) Nested loop over n items
for a in range(100):             # O(n^2) – nested loops
    for b in range(100):
        pass

# (d) Dictionary lookup
d = {"key": "value"}
x = d["key"]                     # O(1) – constant time (average)

# (e) Binary search on sorted list
# O(log n)

print("1. Big-O analysis: see comments above")
print("-" * 30)



# 2. List vs. dict lookup timing

print("2. List vs dict lookup timing (100,000 items)")
SIZE = 100_000
target = f"ACC-{SIZE - 5}"

nums_list = [f"ACC-{i}" for i in range(SIZE)]
nums_dict = {f"ACC-{i}": i for i in range(SIZE)}


start = time.time()
found_list = target in nums_list
print(f"List search: {time.time() - start:.6f} seconds, found={found_list}")


start = time.time()
found_dict = target in nums_dict
print(f"Dict lookup: {time.time() - start:.6f} seconds, found={found_dict}")
print("-" * 30)



# 3. Build a Stack class and reverse a list of names

print("3. Stack class (LIFO)")

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            return None
        return self._items.pop()

    def peek(self):
        if not self._items:
            return None
        return self._items[-1]

    def __bool__(self):
        return len(self._items) > 0

names = ["Almaz", "Dawit", "Tigist", "Hanna"]
s = Stack()
for name in names:
    s.push(name)

reversed_names = []
while s:
    reversed_names.append(s.pop())

print(f"Original: {names}")
print(f"Reversed: {reversed_names}")
print("-" * 30)



# 4. Bank service line with deque (queue)

print("4. Queue (FIFO) – bank line")
queue = deque()
customers = ["Almaz", "Dawit", "Tigist", "Samuel", "Meron"]

for c in customers:
    queue.append(c)
    print(f"Customer {c} joins the queue")

print("\nServing customers:")
while queue:
    served = queue.popleft()
    print(f"Serving {served}")
print("-" * 30)



# 5. Singly linked list

print("5. Singly Linked List")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values) if values else "(empty)")

ll = LinkedList()
ll.push_front("First")
ll.push_front("Second")
ll.push_front("Third")
ll.print_all()          