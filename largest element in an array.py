def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]
    for element in arr:
      if element > largest_element:
        largest_element = element
    return largest_element

array = []
result = find_largest_element(array)
print(result)

