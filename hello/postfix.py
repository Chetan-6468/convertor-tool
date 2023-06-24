def infix_to_postfix(expression):
    # Implement the logic to convert infix to postfix here
    # Replace this placeholder code with your actual conversion logic
    stack = expression
    operator = []
    output = []
    precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for i in stack:
        if i == '(':
            operator.append(i)
        elif i == ')':
            while operator[-1] != '(':
                a = operator.pop()
                output.append(a)
            operator.pop()
        elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
            if len(operator) > 0:
                while precedence[operator[-1]] >= precedence[i]:
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
    return ''.join(output)
