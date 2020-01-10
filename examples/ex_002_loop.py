################################################################################
print("### EXAMPLE 01 ###") # print "Hello World!" 3 times without ITERATOR:
################################################################################

# FOR LOOP
for _ in range(3):
    print("Hello World!")

# LIST COMPREHENSION
[print("Hello World!") for _ in range(3)]

################################################################################
print("### EXAMPLE 02 ###") # print "Hello World!" 3 times:
################################################################################

# FOR LOOP
for i in range(3):
    print("Hello World!", i)

# LIST COMPREHENSION:
[print("Hello World!", i) for i in range(3)]

################################################################################
print("### EXAMPLE 03 ###") # print all characters from string:
################################################################################

# FOR LOOP:
for char in "Hello":
    print(char)

# LIST COMPREHENSION:
[print(char) for char in "Hello"]

################################################################################
print("### EXAMPLE 04 ###") # print all elements from list:
################################################################################

# FOR LOOP:
for word in ["Hello", "World", "!"]:
    print(word)

# LIST COMPREHENSION:
[print(word) for word in ["Hello", "World", "!"]]

################################################################################
print("### EXAMPLE 05 ###") # print sum from integer array:
################################################################################
# FOR LOOP:
total = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    total += number
print(total)

# LIST COMPREHENSION:
print(sum([number for number in numbers]))
################################################################################
print("### EXAMPLE 06 ###") # print sum from EVEN number ONLY from integer array
################################################################################
# FOR LOOP:
total = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        total += number
print(total)

# LIST COMPREHENSION:
print(sum([number for number in numbers if number % 2 == 0]))
################################################################################
