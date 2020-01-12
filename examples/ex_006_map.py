################################################################################
print("### EXAMPLE 01 ####")
################################################################################
words = ["Python", "Bootcamp"]

# EXAMPLE WITH FOR LOOP
word_lists_for = []
for word in words:
    word_lists_for.append(list(word))

# EXAMPLE WITH MAP
word_lists_map = list(map(list, words))

print(word_lists_for)
print(word_lists_map)
################################################################################
print("### EXAMPLE 02 ####")
################################################################################
def random_math_function(nb):
    return int((nb + 1) * 2 / 3 + 100)

numbers = [10, 20, 30, 40, 50]

# EXAMPLE WITH FOR LOOP
number_list_for = []
for number in numbers:
    number_list_for.append(random_math_function(number))

# EXAMPLE WITH MAP
number_list_map = list(map(random_math_function, numbers))

print(number_list_for)
print(number_list_map)
################################################################################
