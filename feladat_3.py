
print('\nFirst function')


def equator(eq_expression: str, **kwargs):

    '''

    This function will evaluate any mathematical expression containing variables.
    The value of the variables should be given as parameters.

    :param eq_expression: The equation in a string format.
    :param kwargs: The variables in the expression and their values
    :return: An integer which equates to the result of the given equation or an error message (str)

    '''

    for key, value in kwargs.items():
        eq_expression = eq_expression.replace(key, str(value))
        # replacing the variables in the expression with the corresponding values

    try:
        result = eval(eq_expression)
        # evaluating the expression
    except NameError:
        print("For at least one of the variables in the equation wasn't given a value!")
        return "For at least one of the variables in the equation wasn't given a value!"
        # if one of the variables present in the expression is not given, an error will be raised

    print(result)
    return result


# results of the first function
eq_one = equator(eq_expression='a+a+a+b', a=1, b=2)  # easy
eq_two_error = equator(eq_expression='a+a+a+b+c', a=1, b=2)  # missing variable value
eq_three = equator(eq_expression='a+b+a+a+c', a=1, b=2, c=5)
eq_four = equator(eq_expression='a+b+a+a-c', a=1, b=2, c=5)  # other than sum
eq_five = equator(eq_expression='a*b+a/a-c', a=2, b=3, c=9)

# second function
print('\nSecond function')
result = []
for i in range(1000, 1, -1):
    if i % 11 == 0 and not i % 2 == 0 and not i % 3 == 0:  # the number should meet this criteria
        print(i)
        result.append(i)  # the number is added to a list
        if len(result) == 4:  # if the list contains 4 numbers, the loop is stopped
            break

# unpacking result list
a, b, c, d = result

