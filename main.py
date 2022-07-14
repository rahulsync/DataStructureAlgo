from binary_search_rec import binary_search_rec

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call


result = binary_search_rec(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
