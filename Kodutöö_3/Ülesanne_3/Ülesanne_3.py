import math

def jump_search(arr, target):
    n = len(arr)
    step = 0
    prev = 0

    # Jump through the array to find the block
    while arr[min(step, n) - 1] < target:
        
        prev = step
        print("Eelnev hüppepunkt:",prev)
        step += int(math.sqrt(n))
        print("Hüppepunkt:", step)

        if prev >= n:
            return -1  # Element not present in the array

    # Linear search within the identified block
    while arr[prev] < target:
        prev += 1
        
        if prev == min(step, n):
            return -1  # Element not present in the array

    if arr[prev] == target:
        return prev  # Element found at index prev

    return -1  # Element not present in the array

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 6
result = jump_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")
