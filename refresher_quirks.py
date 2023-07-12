import heapq
from collections import deque
import math
print("Hello World!")

def print_divider():
    print("----------")

if False:
    print("Hello If!")
elif True:
    print("Hello ElIf!")
else:
    print("Else")

# while
print_divider()
print("while")
n = 0
while n < 10:
    print(n)
    n += 1

print_divider()
print("for range")
for i in range(3):
    print(i)

print("for range from 3 and UPTO 6")
for i in range(3, 6):
    print(i)

print("for range from 7 DOWNTO 3 with step -2")
for i in range(7, 3, -2):
    print(i)

print_divider()
print("division 5 / 2 and 5 // 2 and int divis")
print(5 / 2)
print(5 // 2)
print(-5 // 2)
print(int(5 / 2))

print_divider()
print("modulo 10 % 3")
print(10 % 3)
print("modulo -10 % 3")
print(-10 % 3)


print_divider()
print("math.fmod(-10, 3)")
print(math.fmod(-10, 3))

print(math.floor(5 / 2))
print(math.ceil(5 / 2))
print(math.sqrt(9))
print(math.pow(2, 3))


print(float("inf") < 99999)

# ==================ARRAYS=====================
print_divider()
print("arrays")
a = [1, 2, 3]
a.append(4)
print(a)

print(a.pop())
a.insert(1, 'insert at index bigO(n)')
print(a)

# === Unpacking ===
print_divider()
print("unpacking")
a, b, c = [1, 2, 3]
print(a, b, c)

# ====== Loops ======
print_divider()
print("loops")
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

print('enumerate')
for i, num in enumerate(nums):
    print(i, num)


print_divider()
print('zip')
letters = ['a', 'b', 'c', 'd', 'e']
for letter, num in zip(letters, nums):
    print(letter, num)

print_divider()
print('sort')
arr = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun',
       'Jul', 'Aug', 'Sep', 'October', 'Nov', 'Decemb']
arr.sort()
print(arr)
arr.sort(key=lambda x: len(x))
# arr.sort(key=len)
print(arr)

print_divider()
print('list comprehension')
nums = [1, 2, 3, 4, 5]
squares = [x * x for x in nums]
print(squares)

print_divider()
print('2D list')
two_d_array = [[0] * 4 for x in range(4)]
print(two_d_array)
# do not do this
# two_d_array = [[0] * 4] * 4
print('two_d_array[0][0] = x - will change all 0s to x')
le_bad_array = [[0] * 4] * 4
le_bad_array[0][0] = 'x'
print(le_bad_array)

# ==================STRINGS=====================
print_divider()
s = "Hello World!"
print('Strings - are immputable')
print(s[5:])
print(s[3:-1])

s += "- appending will create a NEW string resulting in O(n) time"
print(s)

print(int("1") + 1)
print(ord("A"))

deez = ['dee', 'z', 'nuts', 'thanks', 'chat', 'gpt']
print(' '.join(deez))


# ==== QUEUE ====
print_divider()
# queues are DOUBLE ENDED queues


queue = deque()

queue.append('a')
queue.append('b')
queue.append(0)
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# popping from left in O(1) time
print('popping from left in O(1) time')
print(queue.popleft())
print(queue.pop())

queue.appendleft('z')
queue.append('tail')
print(queue)

# ==== HASH SET ====
print_divider()
# hash sets are implemented as dictionaries

hash_set = set()
hash_set.add(1)
hash_set.add(2)
hash_set.add(2)
print(hash_set)
print(len(hash_set))
print(1 in hash_set)
print(3 in hash_set)

hash_set.remove(1)
print(1 in hash_set)

print(set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
loop_init_hash_set = {i for i in range(7)}
print(loop_init_hash_set)

# ==== HASH MAP ====
# sameas Ruby

hash_map = {
    'a': 1,
    'b': 2,
    'no rocket input': 3
}
print(hash_map)

# ==== HASH Comprehension ====

my_hash_map = {str(i): i * i for i in range(7)}
print(my_hash_map)

for value in my_hash_map.values():
    print(value)

for key, value in my_hash_map.items():
    print(key, value)

# ==== TUPLES ====

print_divider()
print('Tuples - are immutable')
t = (1, 2, 3)
print(t)
print(t[0])
print(t[1:])
print(t + (4, 5))
print(t * 3)
print(t)


print('tuples can be used as keys in hash maps unlike lists')

# ==== HEAP ====
# under the hood, heaps are implemented as arrays
# by default, they are MIN heaps, for MAX heaps, multiply by -1 when pushing and popping
print_divider()


min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 3)

print(min_heap[0])

while min_heap:
    print(heapq.heappop(min_heap))


print_divider()
print('max heap workaround')
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -3)

print(-max_heap[0])


print_divider()
print('heapify')
arr = [5, 2, 3, 1, 4]
heapq.heapify(arr)
print(arr)
print(arr[0])

# ==== FUNCTIONS ====
print_divider()
print('functions')


def add(x, y):
    return x + y


def classy_func(arr, var):
    c = 'cccc'

    def inner_func():
        # variables in the outer scope can be accessed in the inner scope
        arr[0] = 'changed'
        print('inner func')
        print(c)
        print(arr)

        # nonlocal keyword allows you to modify variables in the outer scope
        nonlocal var
        var *= 2
        print(var)

    inner_func()


classy_func([1, 2, 3], 7)

# ==== CLASSES ====

print_divider()
print('classes')


class Dog:
    # self is the instance of the class
    def __init__(self, name):
        self.name = name
        self.tricks = []

    # always pass self as the first argument
    def add_trick(self, trick):
        self.tricks.append(trick)

    def add_default_tricks(self):
        self.add_trick('slurp')


doggo = Dog('Fido')
doggo.add_default_tricks()
print(doggo.tricks)
doggo.add_trick('roll over')
doggo.add_trick('pass my computer science challenge')

print(doggo.name)
print(doggo.tricks)
