def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0
    mx_odd = data[i]

    while i < len(data):

        if data[i] % 2 == 1 and mx_odd < data[i]:
            mx_odd = data[i]

        i += 1
    return mx_odd