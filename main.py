from binary_search import binary_search

# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 8

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")