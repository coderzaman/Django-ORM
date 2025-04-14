# def get_input_length():
#     user_input = input("Enter something: ")
#     length = len(user_input)
#
#     if length > 0:
#         print(f'Your entered {length} characters.')
#
#

# We modify this code with walrus operator
def get_input_length():
    user_input = input("Enter something: ")

    if (length := len(user_input)) > 0:
        print(f'Your entered {length} characters.')


get_input_length()


# def loop_numbers():
#     numbers = [1, 2, 3, 4, 5]
#
#     length = len(numbers)
#
#     while length > 0:
#         print(f'List has {length} elements, popping one')
#         numbers.pop()
#         length = len(numbers)
#

# Modify this code with walrus operator
def loop_numbers():
    numbers = [1, 2, 3, 4, 5]

    while (length := len(numbers) ) > 0:
        print(f'List has {length} elements, popping one')
        numbers.pop()



loop_numbers()


# use within list comprehension
import json
def parse_json_safely(string):
    try:
        return json.loads(string)
    except:
        return  None


raw_data = ['{"name":"Alice"}', 'invalid', '{"age":30}','{bad json}']

parsed_item = [
    obj for string in raw_data if(obj:=parse_json_safely(string)) is not None
]

print(parsed_item)


import itertools
count = itertools.count()
print(next(count))
print(next(count))

