def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0
    list1 = []

    while i < len(data):

        if data[i] % 2 == 1:
            list1.append(data[i])
        i += 1
    
    k = 0
    mx_odd = list1[k]
    while i < len(list1):

        if mx_odd < list1[k]:
            mx_odd = list1[k]
        k += 1

    return mx_odd