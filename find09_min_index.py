def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i = 0
    mn = data[i]
    while i < len(data):

        if data[i] < mn:
            mn = data[i]
        i += 1

    return data.index(mn)