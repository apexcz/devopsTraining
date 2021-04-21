print('Hello world')

def price_item(name, price_in_pennies):
    return price_in_pennies/100

result = price_item('Milk', 80)
print(result)

sq_odd = [x*x for x in range(20) if x%2!=0]
print(sq_odd)

print(((not False) and False) or (not (1 == 0)))

def format_string(msg, postfix, prefix = 'string: ') -> int:
    print(prefix + msg + postfix)

format_string('hello', postfix='.')

list = ['fourteen', 'fifteen', 16, 'seventeen']

for item in list:
    try:
        msg = 'processing ' + item
        print(msg)
        continue
    except TypeError:
        print('something went wrong!')
        break
    finally:
        print('finally block')
    print('next item please!')


class MyClass:
    myClassVariable = ["Hello"]

    def __init__(self):
        self.myInstanceVariable = [1,2,3]

objectOne = MyClass()
objectTwo = MyClass()

MyClass.myClassVariable = ["Hello", "World"]

objectOne.myInstanceVariable.append(4)
print('Before block')
print(objectOne.myInstanceVariable)
print(objectTwo.myInstanceVariable)
print('After block')
print(objectOne.myClassVariable)
print(objectTwo.myClassVariable)
print(MyClass.myClassVariable)


def run_apple_guessing_game(target):
    while True:
        guess = int(input('Guess How Many Apples I Have!'))
        if guess < target:
            print('Too Few!')
            continue
        elif guess > target:
            print('Too Many!')
            continue
        else:
            print('You\'re Right!')
            return

run_apple_guessing_game(5)

while True:
    username = input('What is your username?')
    if username != 'admin':
        continue
    password = input('What is your password?')
    if password == 'topsecret':
        break

print('Authorised')