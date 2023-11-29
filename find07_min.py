def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    i = 0
    mn = data[i]
    while i < len(data):

        if mn > data[i]:
            mn = data[i]
        i += 1
    return mn