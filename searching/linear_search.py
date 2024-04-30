def linear_search(list,element):
    """
        Purpose: this method searches the list linearly for the element provided

        Arguments:
                 list    : An array of elements
                 element : The element whose index needs to be found

        Returns : An integer related to the index if the elements presented in the list otherwise None
    """
    for i in range(len(list)):
        if list[i] == element:
            return i
    return None

arr = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(arr,6)
print(result)

#output: 5