### EXAMPLE 01: CREATE FUNCTION WITH IF / ELSE STATEMENT
def switch_operations_if_else(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y

### EXAMPLE 02: USING FUNCTION IN DICTIONARY
def switch_operations_functions(operator, x, y):
    return {
        'add': add(x, y),
        'sub': sub(x, y),
        'mul': mul(x, y),
        'div': div(x, y)
    }.get(operator, None)

### EXAMPLE 03: USING LAMBDA IN DICTIONARY
def switch_operations_lambda(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }.get(operator, lambda: None)()

switch_operations_if_else('mul', 5, 5)                  # return : 25
switch_operations_functions('mul', 5, 5)                # return : 25
switch_operations_lambda('mul', 5, 5)                   # return : 25

switch_operations_if_else('bad_value', 5, 5)            # return : None
switch_operations_functions('bad_value', 5, 5)          # return : None
switch_operations_lambda('bad_value', 5, 5)             # return : None
