"""
0/1 Knapsack Problem - Dynamic Programming Implementation
Author: Steven N
Description: Maximize value by selecting indivisible items subject to weight constraint
"""

def knapsack_01(items, capacity):
    """
    Solve 0/1 knapsack problem using 2D DP table
    
    Args:
        items: List of tuples (weight, value)
        capacity: Maximum weight capacity
    
    Returns:
        tuple: (maximum_value, list_of_items_taken)
    """
    n = len(items)
    
    print("=" * 60)
    print("0/1 KNAPSACK - 2D DP APPROACH")
    print("=" * 60)
    print(f"Number of items: {n}")
    print(f"Knapsack capacity: {capacity}")
    print("\nItems:")
    for i, (w, v) in enumerate(items):
        print(f"  Item {i+1}: weight={w}, value={v}")
    
    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    print("\nBuilding DP table...")
    
    # Build table bottom-up
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        print(f"\nProcessing Item {i} (w={weight}, v={value}):")
        
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weight] + value
                )
                if dp[i][w] == dp[i - 1][w - weight] + value:
                    decision = "TAKE"
                else:
                    decision = "skip"
            else:
                dp[i][w] = dp[i - 1][w]
                decision = "skip (too heavy)"
            
            print(f"  dp[{i}][{w}] = {dp[i][w]} ({decision})")
    
    # Backtrack to find items taken
    items_taken = []
    w = capacity
    
    print("\n" + "=" * 60)
    print("BACKTRACKING TO FIND ITEMS TAKEN")
    print("=" * 60)
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_taken.append(i - 1)
            print(f"✓ Item {i} was taken (weight={items[i-1][0]}, value={items[i-1][1]})")
            w -= items[i - 1][0]
        else:
            print(f"  Item {i} was not taken")
    
    items_taken.reverse()
    
    print("\n" + "=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)
    print(f"Maximum value: {dp[n][capacity]}")
    print(f"Items taken: {[i+1 for i in items_taken]}")
    print(f"Total weight: {sum(items[i][0] for i in items_taken)}")
    
    return dp[n][capacity], items_taken


def knapsack_01_space_optimized(items, capacity):
    """
    Space-optimized version using 1D DP array
    
    Args:
        items: List of tuples (weight, value)
        capacity: Maximum weight capacity
    
    Returns:
        int: Maximum value achievable
    """
    n = len(items)
    
    print("\n" + "=" * 60)
    print("0/1 KNAPSACK - SPACE OPTIMIZED 1D APPROACH")
    print("=" * 60)
    print(f"Number of items: {n}")
    print(f"Knapsack capacity: {capacity}")
    print("\nItems:")
    for i, (w, v) in enumerate(items):
        print(f"  Item {i+1}: weight={w}, value={v}")
    
    # Create 1D DP array
    dp = [0] * (capacity + 1)
    
    print("\nInitial DP array:", dp)
    print("\nProcessing items...")
    
    # Process items one by one
    for i in range(n):
        weight, value = items[i]
        print(f"\nItem {i+1} (w={weight}, v={value}):")
        print(f"  Before: {dp}")
        
        # Traverse backwards
        for w in range(capacity, weight - 1, -1):
            if dp[w - weight] + value > dp[w]:
                old = dp[w]
                dp[w] = dp[w - weight] + value
                print(f"  Updated dp[{w}] from {old} to {dp[w]} (taking item)")
        
        print(f"  After:  {dp}")
    
    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    print(f"Maximum value: {dp[capacity]}")
    
    return dp[capacity]


def knapsack_detailed(items, capacity):
    """
    Ultra-detailed version with step-by-step walkthrough
    """
    print("\n" + "=" * 60)
    print("0/1 KNAPSACK - DETAILED WALKTHROUGH")
    print("=" * 60)
    
    n = len(items)
    print(f"Problem: {n} items, capacity {capacity}")
    
    print("\nItem details:")
    print("-" * 30)
    print(f"{'Item':<6} {'Weight':<8} {'Value':<8}")
    print("-" * 30)
    for i, (w, v) in enumerate(items, 1):
        print(f"{i:<6} {w:<8} {v:<8}")
    
    print("\n" + "=" * 60)
    print("Step 1: Create DP table of size (n+1) × (W+1)")
    print("=" * 60)
    print(f"Table dimensions: {n+1} rows × {capacity+1} columns")
    print("Initialize all cells to 0")
    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    print("\nInitial table (row 0 = no items):")
    print("i\\w", end="\t")
    for w in range(capacity + 1):
        print(w, end="\t")
    print("\n" + "-" * (8 * (capacity + 2)))
    print("0", end="\t")
    for w in range(capacity + 1):
        print(dp[0][w], end="\t")
    print()
    
    print("\n" + "=" * 60)
    print("Step 2: Fill table row by row")
    print("=" * 60)
    
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        print(f"\n--- Processing Item {i} (weight={weight}, value={value}) ---")
        
        for w in range(capacity + 1):
            if weight <= w:
                not_take = dp[i - 1][w]
                take = dp[i - 1][w - weight] + value
                dp[i][w] = max(not_take, take)
                
                if take > not_take:
                    print(f"  w={w}: take item → value={take} (from dp[{i-1}][{w-weight}] + {value})")
                else:
                    print(f"  w={w}: skip item → value={not_take} (from dp[{i-1}][{w}])")
            else:
                dp[i][w] = dp[i - 1][w]
                print(f"  w={w}: item too heavy → value={dp[i][w]}")
    
    print("\n" + "=" * 60)
    print("Step 3: Final DP Table")
    print("=" * 60)
    
    # Print table header
    print("i\\w", end="\t")
    for w in range(capacity + 1):
        print(w, end="\t")
    print()
    print("-" * (8 * (capacity + 2)))
    
    # Print table rows
    for i in range(n + 1):
        print(i, end="\t")
        for w in range(capacity + 1):
            if i == n and w == capacity:
                print(f"\033[92m{dp[i][w]}\033[0m", end="\t")  # Green for optimal
            else:
                print(dp[i][w], end="\t")
        print()
    
    print("\n" + "=" * 60)
    print("Step 4: Backtrack to find items taken")
    print("=" * 60)
    
    items_taken = []
    w = capacity
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_taken.append(i)
            print(f"✓ Item {i} was taken (value contribution: {items[i-1][1]})")
            w -= items[i - 1][0]
        else:
            print(f"  Item {i} was not taken")
    
    items_taken.reverse()
    
    print("\n" + "=" * 60)
    print("FINAL SOLUTION")
    print("=" * 60)
    print(f"Maximum value: {dp[n][capacity]}")
    print(f"Items taken: {items_taken}")
    total_weight = sum(items[i-1][0] for i in items_taken)
    print(f"Total weight: {total_weight}/{capacity}")
    
    return dp[n][capacity], items_taken


# Example usage
if __name__ == "__main__":
    # Define items as (weight, value) pairs
    items = [(2, 12), (1, 10), (3, 20), (2, 15)]
    capacity = 5
    
    print("=" * 60)
    print("0/1 KNAPSACK PROBLEM")
    print("=" * 60)
    print("Items (weight, value):")
    for i, (w, v) in enumerate(items):
        print(f"  Item {i+1}: weight={w}, value={v}")
    print(f"Knapsack Capacity: {capacity}")
    
    # Run both approaches
    knapsack_01(items, capacity)
    knapsack_01_space_optimized(items, capacity)
    knapsack_detailed(items, capacity)
    
    # Test with different inputs
    print("\n" + "=" * 60)
    print("TESTING WITH DIFFERENT INPUTS")
    print("=" * 60)
    
    test_cases = [
        ([(1, 1), (2, 2), (3, 3)], 3),
        ([(5, 10), (4, 40), (6, 30), (3, 50)], 10),
        ([(2, 3), (3, 4), (4, 5), (5, 6)], 5)
    ]
    
    for i, (test_items, test_capacity) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        max_val, taken = knapsack_01(test_items, test_capacity)
        print(f"  Max value: {max_val}")
        print(f"  Items taken: {[t+1 for t in taken]}")
