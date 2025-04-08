def substitute(equation, **kwargs):
    for elem in equation:
        if(elem in kwargs.keys()):
            equation = equation.replace(elem, str(kwargs[elem]))
    return equation

print(substitute("x + y = 5", x = 1, y = 4))