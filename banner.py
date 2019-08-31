# Given a string, input by the user, print that 
# string with a box around it. The box should stretch to the length of the string.

to_print = input("Text? ")

def border_message(msg):
    row = len(msg)
    h = ''.join(['*'] + ['*' * row] + ['*'])
    result = h + '\n'"*" + msg + "*"'\n' + h
    print(result)

border_message(to_print)