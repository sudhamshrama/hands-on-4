import heapq

def merge_sorted_arrays(arrays):
    merged = []
    heap = [(arr[0], i, 0) for i, arr in enumerate(arrays) if arr]
    heapq.heapify(heap)
    while heap:
        val, arr_idx, ele_idx = heapq.heappop(heap)
        merged.append(val)
        if ele_idx + 1 < len(arrays[arr_idx]):
            next_tuple = (arrays[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1)
            heapq.heappush(heap, next_tuple)
    return merged

# Example usage:
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]
arrays = [array1, array2, array3]
print(merge_sorted_arrays(arrays))
