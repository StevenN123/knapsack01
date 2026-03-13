"""
Quick Sort - Divide & Conquer Algorithm Implementation
Author: Steven N
Description: In-place sorting algorithm using pivot-based partitioning
"""

# Import the random module to generate random numbers for pivot selection
# This helps avoid worst-case O(n²) performance on already sorted arrays
import random

# Import the time module to measure execution time for performance
# We'll use this to compare different versions of quick sort
import time

def quick_sort(arr):
    """
    Functional version of quick sort - returns new sorted list
    
    This version creates new lists and is easier to understand but uses more memory.
    
    Args:
        arr: Input list to sort
    
    Returns:
        Sorted list (new list, original unchanged)
    """
    # Base case: if the array has 0 or 1 element, it's already sorted
    # This is the termination condition for the recursion
    if len(arr) <= 1:
        # Return the array as-is since it's already sorted
        return arr
    
    # Choose a random element from the array to be the pivot
    # random.choice() selects a random element from the list
    # Random pivot selection helps avoid the O(n²) worst-case on sorted arrays
    pivot = random.choice(arr)
    
    # Create a new list that has all elements less than the pivot
    # List comprehension: [x for x in arr if condition]
    # This goes through each element x in arr and includes it if x < pivot
    left = [x for x in arr if x < pivot]
    
    # Create a new list containing all elements equal to the pivot
    # This handles duplicate values efficiently
    # All equal elements are grouped together in the middle
    middle = [x for x in arr if x == pivot]
    
    # Create a new list containing all elements greater than the pivot
    # These elements will go to the right of the pivot
    right = [x for x in arr if x > pivot]
    
    # Performs a sorting of the left and right lists, then combine with middle
    # The + operator links the three lists in order
    # This builds the final sorted array: [sorted left] + [all pivots] + [sorted right]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place version of quick sort (modifies original array)
    This version is more memory-efficient as it doesn't create new lists.
    
    Args:
        arr: Input list to sort (will be modified)
        low: Starting index of subarray to sort
        high: Ending index of subarray to sort
    
    Returns:
        Sorted list (same reference as input)
    """
    # Check if this is the first call (when high is None)
    # The default parameter high is None allows us to call with just the array
    if high is None:
        # Set high to the last index of the array
        # This defines the full range to sort
        high = len(arr) - 1
    
    # Only proceed if the subarray has at least two elements
    # If low >= high, the subarray has 0 or 1 element and is already sorted
    if low < high:
        # Separate the array and get the final position of the pivot
        # partition() rearranges elements and returns the pivot's index
        pivot_index = partition(arr, low, high)
        
        # Performs a sort the left subarray (elements before the pivot)
        # This subarray ranges from low to pivot_index - 1
        quick_sort_inplace(arr, low, pivot_index - 1)
        
        # Recursively sort the right subarray (elements after the pivot)
        # This subarray ranges from pivot_index + 1 to high
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    # Return the sorted array (same reference that was passed in)
    # This allows for method chaining if needed
    return arr


def partition(arr, low, high):
    """
    Partition array around pivot for in-place quick sort
    
    This function rearranges elements so that all elements less than pivot
    come before it, and all greater elements come after it.
    
    Args:
        arr: Array to partition
        low: Starting index of partition range
        high: Ending index of partition range
    
    Returns:
        Final position of pivot after partitioning
    """
    # Choose a random index between low and high (inclusive) as the pivot
    # random.randint(a, b) returns a random integer N such that a <= N <= b
    random_index = random.randint(low, high)
    
    # Swap the randomly chosen pivot with the last element
    # This moves the pivot to the end temporarily
    # Tuple (collection of elements) unpacking performs the swap in one line
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    # Now the pivot value is at the high index
    pivot = arr[high]
    
    # Initialize i to track the position where elements <= pivot will go
    # i starts before the first element (low-1)
    # i will always point to the last element that is <= pivot
    i = low - 1
    
    # Run through all elements except the pivot (which is at high)
    # j goes from low to high-1 (inclusive)
    for j in range(low, high):
        # If the current element is less than or equal to the pivot
        # Using <= ensures stability (though quick sort isn't typically stable)
        if arr[j] <= pivot:
            # Increment i to get the next position for a smaller element
            i += 1
            # Swap the element at i with the element at j
            # This moves the smaller element to the left section
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in its correct position (right after all smaller elements)
    # i+1 is the position where the pivot belongs
    # Swap the pivot (at high) with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the final index of the pivot
    # All elements before this index are <= pivot
    # All elements after this index are >= pivot
    return i + 1


def quick_sort_detailed(arr, low=0, high=None, depth=0):
    """
    Detailed version with step-by-step output for learning
    This helps visualize the recursive divide-and-conquer process.
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
        depth: Recursion depth for indentation
    
    Returns:
        Sorted array
    """
    # Check if this is the first call (when high is None)
    if high is None:
        # Set high to the last index
        high = len(arr) - 1
        # Print the initial header for the detailed walkthrough
        print("\n" + "=" * 60)
        print("QUICK SORT - DETAILED WALKTHROUGH")
        print("=" * 60)
        # Print the initial array state
        print(f"Initial array: {arr}")
    
    # Create indentation string based on recursion depth
    # Each level of recursion gets two more spaces of indentation
    # This makes the recursion tree visually clear
    indent = "  " * depth
    
    # Check if we have at least two elements to sort
    if low < high:
        # Print the current subarray being processed
        # arr[low:high+1] slices the array to show only the current subarray
        print(f"\n{indent}Sorting subarray {arr[low:high+1]} (indices {low}-{high})")
        
        # Choose a random pivot index
        pivot_idx = random.randint(low, high)
        # Get the actual pivot value
        pivot_value = arr[pivot_idx]
        # Print the chosen pivot
        print(f"{indent}Chosen pivot: {pivot_value} at index {pivot_idx}")
        
        # Perform partition and print detailed steps
        print(f"{indent}Partitioning...")
        # Call detailed partition function that prints each step
        pivot_final = partition_detailed(arr, low, high, depth)
        
        # Print the array after partitioning
        print(f"{indent}After partition: {arr[low:high+1]}")
        # Print where the pivot ended up
        print(f"{indent}Pivot {pivot_value} is now at index {pivot_final}")
        
        # Recursively sort the left subarray (before pivot)
        # Increase depth by 1 for proper indentation
        quick_sort_detailed(arr, low, pivot_final - 1, depth + 1)
        
        # Recursively sort the right subarray (after pivot)
        quick_sort_detailed(arr, pivot_final + 1, high, depth + 1)
    else:
        # Base case: single element or empty subarray
        if low == high:
            # Print that we've reached a single element
            print(f"{indent}Base case: single element [{arr[low]}]")
    
    # Return the sorted array
    return arr


def partition_detailed(arr, low, high, depth=0):
    """
    Detailed partition with step-by-step output for learning
    Shows each comparison and swap during the partition process.
    """
    # Create indentation based on recursion depth plus 1 extra level
    # This makes partition details indented under the current recursion level
    indent = "  " * depth
    
    # Choose random pivot index
    random_index = random.randint(low, high)
    # Get the pivot value
    pivot_value = arr[random_index]
    
    # Print that we're moving the pivot to the end
    print(f"{indent}  Moving pivot {pivot_value} from index {random_index} to the end")
    # Swap the pivot with the last element
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    # Now pivot is at the high index
    pivot = arr[high]
    
    # Initialize i to track boundary of elements <= pivot
    i = low - 1
    
    # Print initial i value
    print(f"{indent}  i = {i} (index of last element < pivot)")
    
    # Iterate through all elements except the pivot
    for j in range(low, high):
        # Check if current element should be on left side
        if arr[j] <= pivot:
            # Move boundary and increment i
            i += 1
            # Check if we need to swap (different indices)
            if i != j:
                # Print the swap details
                print(f"{indent}  j={j}: arr[{j}]={arr[j]} ≤ pivot → swap with arr[{i}]={arr[i]}")
                # Perform the swap
                arr[i], arr[j] = arr[j], arr[i]
                # Show array after swap
                print(f"{indent}    Array now: {arr[low:high+1]}")
            else:
                # i and j are same, no swap needed
                print(f"{indent}  j={j}: arr[{j}]={arr[j]} ≤ pivot, i={i} (same index, no swap)")
        else:
            # Element is greater than pivot, no swap
            print(f"{indent}  j={j}: arr[{j}]={arr[j]} > pivot → no swap")
    
    # Place pivot in its final position
    print(f"{indent}  Placing pivot at index {i+1}")
    # Swap pivot (at high) with element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Show final partitioned section
    print(f"{indent}  Final partitioned section: {arr[low:high+1]}")
    
    # Return final pivot index
    return i + 1


def quick_sort_optimized(arr, low=0, high=None, threshold=10):
    """
    Optimized quick sort with insertion sort for small subarrays
    This hybrid approach improves performance by avoiding recursive calls for tiny arrays.
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
        threshold: Size threshold for using insertion sort
    
    Returns:
        Sorted array
    """
    # Check if this is the first call
    if high is None:
        # Set high to the last index
        high = len(arr) - 1
    
    # Check if subarray size is below threshold
    # If the subarray has fewer than 'threshold' elements
    if high - low < threshold:
        # Use insertion sort for small subarrays
        # Insertion sort is more efficient for very small arrays
        insertion_sort(arr, low, high)
        # Return early since we're done with this subarray
        return arr
    
    # For larger arrays, use quick sort
    if low < high:
        # Partition using median-of-three pivot selection
        # This chooses a better pivot than random selection
        pivot_index = partition_median_of_three(arr, low, high)
        
        # Recursively sort the left subarray
        # Lower threshold value
        quick_sort_optimized(arr, low, pivot_index - 1, threshold)
        
        # Recursively sort the right subarray
        quick_sort_optimized(arr, pivot_index + 1, high, threshold)
    
    # Return the sorted array
    return arr


def partition_median_of_three(arr, low, high):
    """
    Partition using median-of-three pivot selection
    This chooses a better pivot by taking the median of first, middle, and last elements.
    This approach reduces the probability of worst-case behavior.
    """
    # Calculate the middle index
    mid = (low + high) // 2
    
    # Sort low, mid, and high to find the median
    # These three if statements put the median at the mid index
    
    # If mid element is less than low element, swap them
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    
    # If high element is less than low element, swap them
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    
    # If high element is less than mid element, swap them
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Now arr[mid] is the median value
    # Move the median to high-1 (second last position)
    # This puts it in a convenient spot for partitioning
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    
    # Use the median as the pivot
    pivot = arr[high - 1]
    
    # Initialize i to track the boundary of elements <= pivot
    i = low
    
    # Partition using all elements except low and high-1 (where pivot is)
    # We exclude high because that's the original high element
    # We exclude high-1 because that's where we put the pivot
    for j in range(low, high - 1):
        # If current element is less than or equal to pivot
        if arr[j] <= pivot:
            # Swap with element at boundary
            arr[i], arr[j] = arr[j], arr[i]
            # Move boundary forward
            i += 1
    
    # Place pivot in its final position
    arr[i], arr[high - 1] = arr[high - 1], arr[i]
    
    # Return final pivot index
    return i


def insertion_sort(arr, low, high):
    """Insertion sort for small subarrays - efficient for nearly-sorted arrays"""
    # Repeat through each element starting from the second element in the range
    # i goes from low+1 to high (inclusive)
    for i in range(low + 1, high + 1):
        # Store the current element as the key
        # This is the element we'll insert into the sorted portion
        key = arr[i]
        
        # Initialize j to point to the element before i
        j = i - 1
        
        # Shift elements greater than key to the right
        # Continue while we haven't reached the beginning and current element > key
        while j >= low and arr[j] > key:
            # Move the larger element one position right
            arr[j + 1] = arr[j]
            # Move j left to check the next element
            j -= 1
        
        # Place the key in its correct position
        # j+1 is where the key belongs (after all larger elements are shifted)
        arr[j + 1] = key


def quick_sort_iterative(arr):
    """
    Iterative version of quick sort using explicit stack
    This avoids recursion depth issues for very large arrays.
    
    Args:
        arr: Array to sort
    
    Returns:
        Sorted array
    """
    # Set up a stack with the entire array range
    # Stack is a list of tuples, each tuple is (low, high) for a subarray
    stack = [(0, len(arr) - 1)]
    
    # Continue while there are subarrays to process
    while stack:
        # Pop the next subarray range from the stack
        # pop() removes and returns the last element (LIFO)
        low, high = stack.pop()
        
        # Check if this subarray has at least two elements
        if low < high:
            # Partition the subarray and get the pivot index
            pivot_index = partition(arr, low, high)
            
            # Push subarrays onto the stack
            # To minimize stack size, we push the larger subarray first
            # Compare the sizes of left and right subarrays
            if pivot_index - low < high - pivot_index:
                # Right subarray is larger, push it first
                # Push right subarray (pivot_index+1 to high)
                stack.append((pivot_index + 1, high))
                # Then push left subarray (low to pivot_index-1)
                stack.append((low, pivot_index - 1))
            else:
                # Left subarray is larger or equal, push it first
                # Push left subarray (low to pivot_index-1)
                stack.append((low, pivot_index - 1))
                # Then push right subarray (pivot_index+1 to high)
                stack.append((pivot_index + 1, high))
    
    # Return the sorted array
    return arr


def three_way_partition(arr, low, high):
    """
    Three-way partition for handling duplicates (Dutch National Flag)
    This partitions the array into three sections: < pivot, = pivot, > pivot
    
    Returns:
        Tuple of (lt, gt) indices where:
        - lt is the last index of < pivot section
        - gt is the first index of > pivot section
    """
    # Choose the first element as the pivot
    pivot = arr[low]
    
    # Initialize three pointers:
    # lt (less than) - points to the last element < pivot
    lt = low
    
    # gt (greater than) - points to the first element > pivot
    gt = high
    
    # i - current element being examined
    i = low + 1
    
    # Continue until we've processed all elements
    while i <= gt:
        # Case 1: current element is less than pivot
        if arr[i] < pivot:
            # Swap with element at lt boundary
            arr[lt], arr[i] = arr[i], arr[lt]
            # Move lt boundary right (expand < section)
            lt += 1
            # Move to next element
            i += 1
        
        # Case 2: current element is greater than pivot
        elif arr[i] > pivot:
            # Swap with element at gt boundary
            arr[i], arr[gt] = arr[gt], arr[i]
            # Move gt boundary left (expand > section)
            gt -= 1
            # Don't increment i - need to examine the swapped element
        
        # Case 3: current element equals pivot
        else:
            # Just move to next element (stays in middle section)
            i += 1
    
    # Return the boundaries of < and > sections
    return lt, gt


def quick_sort_3way(arr, low=0, high=None):
    """
    Quick sort with three-way partitioning for arrays with many duplicates
    This version handles duplicates efficiently by grouping them together.
    """
    # Check if this is the first call
    if high is None:
        # Set high to the last index
        high = len(arr) - 1
    
    # Check if we have at least two elements
    if low < high:
        # Perform three-way partition
        # lt and gt are the boundaries of the equal-to-pivot section
        lt, gt = three_way_partition(arr, low, high)
        
        # Recursively sort elements less than pivot
        # This subarray is from low to lt-1
        quick_sort_3way(arr, low, lt - 1)
        
        # Recursively sort elements greater than pivot
        # This subarray is from gt+1 to high
        quick_sort_3way(arr, gt + 1, high)
    
    # Return the sorted array
    return arr


def analyze_sorting_algorithm(arr, func, name):
    """Analyze performance of a sorting algorithm"""
    # Create a copy of the array to avoid modifying the original
    # This makes sure each algorithm works on same input
    arr_copy = arr.copy()
    
    # Record the start time using high-precision timer
    start = time.time()
    
    # Execute the sorting function on the array copy
    result = func(arr_copy)
    
    # Record the end time
    end = time.time()
    
    # Print the analysis header with algorithm name
    print(f"\n{name}:")
    
    # Calculate and print elapsed time in milliseconds
    # Multiply by 1000 to convert seconds to milliseconds
    # Format to 4 decimal places for precision
    print(f"  Time: {(end - start) * 1000:.4f} ms")
    
    # Print the sorted result (or first 10 elements if too long)
    if len(result) > 10:
        # Show only first 10 elements for large arrays
        print(f"  Result: {result[:10]}...")
    else:
        # Show full array for small arrays
        print(f"  Result: {result}")
    
    # Return the sorted result (though we don't use it further)
    return result


def generate_test_arrays():
    """Generate test arrays for performance analysis"""
    # Return a dictionary of different array types for comprehensive testing
    return {
        # Random array: typical case with random values
        "Random": [random.randint(1, 1000) for _ in range(100)],
        
        # Already sorted array: tests pivot selection (worst case for naive quick sort)
        "Sorted": list(range(100)),
        
        # Reverse sorted array: also worst case for naive quick sort
        "Reverse Sorted": list(range(100, 0, -1)),
        
        # Array with many duplicates: tests three-way partitioning efficiency
        "Many Duplicates": [random.randint(1, 10) for _ in range(100)],
        
        # Small fixed array: for demonstration purposes
        "Small": [5, 2, 8, 1, 9, 3, 7, 4, 6]
    }


# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Print the main header for the demonstration
    print("=" * 60)
    print("QUICK SORT ALGORITHM DEMONSTRATION")
    print("=" * 60)
    
    # Create a basic example array for original demonstration
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {arr}")
    
    # Test the functional version (returns new sorted array)
    # This doesn't change the original array
    sorted_arr = quick_sort(arr)
    print(f"Sorted (functional): {sorted_arr}")
    
    # Test the in-place version (modifies the array)
    # Create a copy first to keep the original for other tests
    arr_copy = arr.copy()
    quick_sort_inplace(arr_copy)
    print(f"Sorted (in-place): {arr_copy}")
    
    # Run the detailed walkthrough for educational purposes
    print("\n" + "=" * 60)
    print("DETAILED WALKTHROUGH")
    print("=" * 60)
    # Create another copy for the detailed walkthrough
    test_arr = [64, 34, 25, 12, 22, 11, 90].copy()
    quick_sort_detailed(test_arr)
    
    # Test different pivot strategies and optimizations
    print("\n" + "=" * 60)
    print("PIVOT STRATEGY COMPARISON")
    print("=" * 60)
    
    # Generate all test arrays
    test_arrays = generate_test_arrays()
    
    # Test each array type with different algorithms
    for arr_name, test_arr in test_arrays.items():
        print(f"\n{arr_name} Array (size: {len(test_arr)}):")
        
        # Test standard functional version with random pivot
        analyze_sorting_algorithm(test_arr, quick_sort, "Standard (functional)")
        
        # Test in-place version with random pivot
        analyze_sorting_algorithm(test_arr, quick_sort_inplace, "In-place (random pivot)")
        
        # Make a function to finish the faster version
        # This is necessary because quick_sort_optimized has extra parameters
        def opt_wrapper(a):
            # Call optimized version with threshold of 10
            # Use a.copy() to avoid changes to the original test array
            return quick_sort_optimized(a.copy(), threshold=10)
        
        # Test the version with insertion sort for small subarrays
        analyze_sorting_algorithm(test_arr, opt_wrapper, "Optimized (with insertion sort)")
    
    # Demonstrate three-way partitioning for arrays with many duplicates
    print("\n" + "=" * 60)
    print("THREE-WAY PARTITIONING FOR DUPLICATES")
    print("=" * 60)
    
    # Create an array with many duplicate values
    dup_arr = [3, 7, 3, 1, 3, 9, 3, 2, 3, 5]
    print(f"Original with duplicates: {dup_arr}")
    
    # Sort using three-way partitioning
    sorted_dup = quick_sort_3way(dup_arr.copy())
    print(f"Sorted (3-way): {sorted_dup}")
    
    # Compare with standard quick sort
    std_sorted = quick_sort(dup_arr)
    print(f"Sorted (standard): {std_sorted}")
    
    # Print key insights about quick sort
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)
    print("""
    1. Pivot selection is crucial: random pivot avoids worst-case O(n²)
    2. In-place version uses O(log n) space for recursion stack
    3. Three-way partitioning handles duplicates efficiently
    4. Hybrid with insertion sort for small subarrays improves performance
    5. Iterative version avoids recursion depth issues
    """)
