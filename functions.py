import arith

'''
Contains the implemented functions and their names. This dictionary
is referenced when checking whether or not a command entered is a valid
function. The dictionary contains of key: value pairs, where key is a string
containing the function name and value is a reference to the function that
was implemented.
In case a new function is added to the calculator, make sure to update this
dictionary.
'''
function_table = {
    'sub': arith.sub,
    'sum': arith.sum,
    'divide': arith.divide,
    'multiply': arith.multiply,
    'power': arith.power,
    'sqrt': arith.sqrt,
    'mod': arith.mod,
    'gcd': arith.gcd,
    'lcm': arith.lcm,
    'bin': arith.bin
}

arity_table = {
    'sub': 2,
    'sum': 2,
    'divide': 2,
    'multiply': 2,
    'power': 2,
    'sqrt': 1,
    'mod': 2,
    'gcd': 2,
    'lcm': 2,
    'bin': 1
}

types_table = {
    'sub': int,
    'sum': int,
    'divide': int,
    'multiply': int,
    'power': int,
    'sqrt': int,
    'mod': int,
    'gcd': int,
    'lcm': int,
    'bin': str
}


def list_only_type(typ,lis):
    for i in lis:
        if type(i) != typ:
            result = False
        else: 
            result = True
    return result

def turn_list_int(lis):
    for i in range(len(lis)):
        lis[i] = int(lis[i])

'''
Returns True if function_name provided is a valid function, else False.
'''
def is_function(function_name):
    return function_name in function_table

'''
Returns the function according to function_name.
'''
def get_function(function_name):
    return function_table[function_name]

'''
Returns the arity of the function according to function_name.
'''
def get_arity(function_name):
    return arity_table[function_name]

'''
Returns the type of _all_ parameters of the function according to function_name.
'''
def get_type(function_name):
    return types_table[function_name]

'''
Prints the available functions and their arity.
'''
def print_functions():
    print('supported functions:')
    for function_name in function_table.keys():
        print('"%s" arity: %i' % (function_name, arity_table[function_name]))

'''
Determine if string can be turned into a number
'''
def determine_fix(tokens):
    if tokens[0].isalpha():
        typ = "prefix"
    elif tokens[1].isalpha():
        typ = "infix"
    elif tokens[2].isalpha():
        typ = "postfix"
    else:
        typ = "prefix"
    return typ
'''
prefix path
'''
def prefix(tokens):
    while len(tokens) > 3:
        if tokens[-2] == "bin":
            tokens[-2] = prefix(tokens[-2:])
            del tokens[-1]
        else:
            tokens[-3] = prefix(tokens[-3:])
            del tokens[-1]
            del tokens[-1]
    else:
        f_name = tokens[0]
        operators = tokens[1:]
        
        if len(operators) == 2:
            operators[0] = int(operators[0])
            operators[1] = int(operators[1])
        elif len(operators) == 1:
            operators[0] = int(operators[0])

        if f_name == 'bin':
            operators[0] = str(operators[0])
        if not is_function(f_name):
            return("unknown token")
        elif get_arity(f_name) != len(operators):
            return("invalid number of operands")
        elif list_only_type(get_type(f_name), operators) != True:
            return("invalid operand type")
        else:  
            func = get_function(f_name)
            result = func(*operators)
            return(result)

def postfix(tokens):
    while len(tokens) > 3:
        if tokens[1] == "bin":
            tokens[0] = postfix(tokens[:2])
            del tokens[1]
        else:
            tokens[0] = postfix(tokens[:3])
            del tokens[1]
            del tokens[1]
    else:

        if tokens[1] == "bin":
            f_name = tokens[1]
            operators = tokens[0]
        else:
            f_name = tokens[2]
            operators = tokens[0:2]
        if len(operators) == 2:
            operators[0] = int(operators[0])
            operators[1] = int(operators[1])
        elif len(operators) == 1:
            operators[0] = int(operators[0])

        if f_name == 'bin':
            operators[0] = str(operators[0])
        if f_name == 'ans':
            return("invalid use of ans")
        elif not is_function(f_name):
            return("unknown token")
        elif get_arity(f_name) != len(operators):
            return("invalid number of operands")
        elif list_only_type(get_type(f_name), operators) != True:
            return("invalid operand type")
        else:  
            func = get_function(f_name)
            result = func(*operators)
            return(result)

def infix(tokens):
    while len(tokens) > 3:
        if len(tokens) > 3:
            temp_tokens = []
            i = 0
            while i < len(tokens):
                minus_i = i*(-1) -1
                if tokens[minus_i] == "power":
                    temp_tokens = [tokens[minus_i-1],tokens[minus_i],tokens[minus_i+1]]
                    tokens[minus_i -1] = infix(temp_tokens)
                    del tokens[minus_i]
                    del tokens[minus_i+1]
                    i = 0
                i += 1
        if len(tokens) > 3:
            temp_tokens = []
            i = 0
            while i < len(tokens):
                if tokens[i] == "mod":
                    temp_tokens = [tokens[i-1],tokens[i],tokens[i+1]]
                    tokens[i-1] = infix(temp_tokens)
                    del tokens[i]
                    del tokens[i]
                    i = 0
                i += 1
        if len(tokens) > 3:
        
            temp_tokens = []
            i = 0
            while i < len(tokens):
                if tokens[i] == "multiply" or tokens[i] == "divide":
                    temp_tokens = [tokens[i-1],tokens[i],tokens[i+1]]
                    tokens[i-1] = infix(temp_tokens)
                    del tokens[i]
                    del tokens[i]
                    i = 0
                i += 1
        if len(tokens) > 3:
            
            temp_tokens = []
            i = 0
            while i < len(tokens):
                if tokens[i] == "sum" or tokens[i] == "sub":
                    temp_tokens = [tokens[i-1],tokens[i],tokens[i+1]]
                    tokens[i-1] = infix(temp_tokens)
                    del tokens[i]
                    del tokens[i]
                    i = 0
                i += 1
    else:
        if len(tokens) == 3:
            f_name = tokens[1]
            operators = [tokens[0],tokens[2]]
            if len(operators) == 2:
                operators[0] = int(operators[0])
                operators[1] = int(operators[1])
            elif len(operators) == 1:
                operators[0] = int(operators[0])
            if f_name == 'bin':
                operators[0] = str(operators[0])
            if not is_function(f_name):
                return("unknown token")
            elif get_arity(f_name) != len(operators):
                return("invalid number of operands")
            elif list_only_type(get_type(f_name), operators) != True:
                return("invalid operand type")
            else:  
                func = get_function(f_name)
                result = func(*operators)
        else:
            result = tokens[0]
    
    
        return(result)

def process_line(inp):
    tokens = inp.split()
    if len(tokens) < 2:
        return("unknown token")
    else:
        type_fix = determine_fix(tokens)
        if type_fix == "prefix":
            return prefix(tokens)
        elif type_fix == "infix":
            return infix(tokens)
        elif type_fix == "postfix":
            return postfix(tokens)

    