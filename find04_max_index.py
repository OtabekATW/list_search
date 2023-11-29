def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i = 0
    mx = data[i]
    while i < len(data):

        if mx < data[i]:
            mx = data[i]
        i += 1
    return data.index(mx)