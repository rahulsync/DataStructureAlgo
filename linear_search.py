def linear_search(list, target):
    """
     :param list:
    :param target index we are looking for:
    :return the index positions and none if not found:
    """
    for index in range(0, len(list)):
        if list[index] == target:
            return f"target found with the value: {list[index]} at index: {index}"
    return "nah! no such thing."

