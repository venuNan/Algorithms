def binary_search(lst, element):
    """
    Search the whole list to find the element's index.

    Arguments:
        lst (list): An array of elements.
        element: The element whose index needs to be found.

    Returns:
        int: The index of the element if found, or None if the element is not in the list.
    """
    l = 0  # leftmost index
    r = len(lst) - 1  # rightmost index

    while l <= r:
        mid = (l + r) // 2  # middle index where we can find the element index in the list
        if lst[mid] == element:
            return mid  # if the element is found, return its index
        elif lst[mid] < element:
            l = mid + 1  # if the element in the middle index is less than the searching element,
                        # update leftmost index to mid + 1
        else:
            r = mid - 1  # if the element in the middle index is greater than the searching element,
                        # update rightmost index to mid - 1

    return None  # if the element is not found in the list, return None

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(lst, 6))
