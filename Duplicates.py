def remove_duplicates(arr):
    if not arr:
        return []

    output = [arr[0]]  # Start with the first element
    prev = arr[0]  # Keep track of the previous element

    for i in range(1, len(arr)):
        if arr[i] != prev:  # If the current element is different from the previous one
            output.append(arr[i])  # Add it to the output array
            prev = arr[i]  # Update the previous element

    return output

# Test cases
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print(remove_duplicates(array1))  # Output: [2]
print(remove_duplicates(array2))  # Output: [1, 2, 3, 4, 5]
