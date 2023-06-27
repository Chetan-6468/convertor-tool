def convert_to_prefix(expression):
    # Implement the logic to convert infix to prefix here
    # Replace this placeholder code with your actual conversion logic
    return infix_to_prefix(expression) + ' (converted to prefix)'


def infix_to_prefix(expression):
    # Implement the logic to convert infix to prefix here
    # Replace this placeholder code with your actual conversion logic
    stack1 = expression[-1::-1]
    stack = []
    operator = []
    output = []
    dictionary = {')': 0, '+': 1, '-': 1, '/': 2, '*': 2, '^': 3}
    for i in stack1:
        if i == ')':
            operator.append(i)
        elif i == '(':
            while operator[-1] != ')':
                a = operator.pop()
                output.append(a)
            operator.pop()
        elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
            if len(operator) > 0:
                while dictionary[operator[-1]] > dictionary[i]:
                    b = operator.pop()
                    output.append(b)
                    if len(operator) == 0:
                        break
            operator.append(i)
        else:
            output.append(i)
    while len(operator) != 0:
        c = operator.pop()
        output.append(c)
    output.reverse()
    return ''.join(output)
