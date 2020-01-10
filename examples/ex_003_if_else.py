################################################################################
print("### EXAMPLE 01 ###")
################################################################################
boolean = True

if boolean:
    print("True")
else:
    print("False")

# INLINE CONDITIONAL STATEMENT:
print("True") if boolean else print("False")
################################################################################
print("### EXAMPLE 02 ###")
################################################################################
a = 1
b = 2

if a > b:
    print(a, ">", b)
elif b > a:
    print(b, ">", a)
else:
    print(a, "==", b)

# INLINE CONDITIONAL STATEMENT:
print(a, ">", b) if a > b else print(b, ">", a) if b > a else print(a, "==", b)
################################################################################
print("### EXAMPLE 03 ###")
################################################################################
a = 3
b = 2
c = 1

if a > b and a > c:
    print(a, ">", b, "and", c)
else:
    print(a, "is not bigger than", b, "and", c)

# INLINE CONDITIONAL STATEMENT:
print(a, ">", b, "and", c) if a > b and a > c else \
print(a, "is not bigger than", b, "and", c)
################################################################################
print("### EXAMPLE 04 ###")
################################################################################
if "Hello" in "Hello World!":
    print(True)
else:
    print(False)

print(True) if "Hello" in "Hello World!" else print(False)

################################################################################
print("### EXAMPLE 05 ###")
################################################################################
hello_world_list = ["Hello", "World", "!"]
if "Hello" in hello_world_list:
    print("Hello found in:", hello_world_list)
else:
    print("Hello not found in:", hello_world_list)

# INLINE CONDITIONAL STATEMENT:
print("Hello found in:", hello_world_list) if "Hello" in hello_world_list else \
print("Hello not found in:", hello_world_list)
