def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    mx_even = data[i]

    while i < len(data):

        if data[i] % 2 == 0 and mx_even < data[i]:
            mx_even = data[i]

        i += 1

    return mx_even