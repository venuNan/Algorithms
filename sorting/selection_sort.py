def selection_sort(arr):
  """
  Purpose : sorts an array by using selection sorting technique

  Parameters : An array

  Returns : a sorted array

  """
  for i in range(len(arr) - 1):
    min_index = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_index] :
        min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr


a = [10, 9, 8, 7, 6, 5, 6, 4, 5, 4, 8, 7, 4, 5, 4, 3, 2, 1]
res = selection_sort(a)
print(res)

