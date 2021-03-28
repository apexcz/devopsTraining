def calculate(operation, first, second):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == 'x':
        return int(first) * second
    elif operation == '/':
        return first / second
    else:
        return 'Invalid operation'

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()

def process():
    lines = read_file('data.txt')
    for line in lines:
        calc, operation, first, second = line.split()
        if calc == 'calc':
            output = calculate(operation, int(first), int(second))
            #print('{0} {1} {2} {3}'.format(calc, operation, first, second))
            print(output)

def goto(line_number):
    lines = read_file('data.txt')
    line = lines[line_number-1]
    calc, operation, first, second = line.split()
    if calc == 'calc':
        output = calculate(operation, int(first), int(second))
        print(output)

def goto_calc(input):
    print(input)
        

goto(2)
