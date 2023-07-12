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
print( -5 // 2) 
print(int(5 / 2))

print_divider()
print("modulo 10 % 3")
print(10 % 3)
print("modulo -10 % 3")
print(-10 % 3)

import math

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
arr = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'October', 'Nov', 'Decemb']
arr.sort()
print(arr)
arr.sort(key=lambda x: len(x))
# arr.sort(key=len)
print(arr)

