"""Write a short recursive Python function that finds the minimum and maximum 
values in a sequence without using any loop"""

def find_min_max(sequence):
    if len(sequence) == 1:
        return sequence[0], sequence[0]  # Base case: Only one element in the sequence
    
    # Recursive case: Divide the sequence into two halves
    mid = len(sequence) // 2
    left_min, left_max = find_min_max(sequence[:mid])  # Recursively find min and max in the left half
    print(sequence[:mid])
    right_min, right_max = find_min_max(sequence[mid:])  # Recursively find min and max in the right half
    print(sequence[mid:])
    # Compare the minimum and maximum values from the left and right halves
    return min(left_min, right_min), max(left_max, right_max)

# Example usage
my_sequence = [5, 3, 9, 1, 7, 2, 6, 4, 8]
min_value, max_value = find_min_max(my_sequence)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
