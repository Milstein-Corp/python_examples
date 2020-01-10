place = "World"

# 01 - print string
print("Hello World!")

# 02 - print with variable and string concatenation
print("Hello " + place + "!")

# 03 - print with variable and comma
print("Hello ", place, "!", sep='')

# 04 - print with format
print("Hello {}!".format(place))

# 05 - print with format
print(f"Hello {place}!")

# 06 - print with reversed
print('!dlroW olleH'[::-1])

# 07 - print with replace
print("Hello " + "Kevin!".replace("Kevin", "World"))

# 08 - print with translate / maketrans
print("Hello " + "Kevin!".translate(str.maketrans("Kevin", "World")))

# 09 - print with join from string
print(''.join(c for c in 'Hello World!'))

# 10 - print with join from array
print(''.join(["H","e","l","l","o", " ", "W", "o", "r", "l", "d", "!"]))

# 11 - print with join from int array and ascii convert function
print(''.join([chr(c) for c in [72,101,108,108,111,32,87,111,114,108,100,33]]))

# 12 - print with join from binary numbers string
bin_str = '''
    01001000
    01100101
    01101100
    01101100
    01101111
    00100000
    01010111
    01101111
    01110010
    01101100
    01100100
    00100001
'''

print(''.join(chr(int(l.strip(), 2)) for l in bin_str.split('\n') if l))

# 13 - print from hex number
print("\u0048\u0065\u006C\u006C\u006F\u0020\u0057\u006F\u0072\u006C\u0064\u0021")
