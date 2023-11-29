def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i = 0
    mn = data[i]
    while i < len(data):

        if data[i] < mn:
            mn = data[i]
        i += 1
    return data.count(mn)