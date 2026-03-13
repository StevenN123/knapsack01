# knapsack01

An implementation of the 0/1 Knapsack problem using dynamic programming. This optimization problem shows optimal substructure and overlapping subproblems.

## 📋 Problem Description

Determine the maximum total value that can fit in a knapsack with capacity `W` given a set of `n` items, each with weight `wᵢ` and value `vᵢ`. You can either take an item (1) or leave it (0) because items are indivisible.


### Example
**Items:**
| Item | Weight | Value |
|------|--------|-------|
| 1    | 2      | 12    |
| 2    | 1      | 10    |
| 3    | 3      | 20    |
| 4    | 2      | 15    |

**Capacity:** W = 5  
**Solution:** Take items 1, 2, and 4 (weights: 2+1+2=5, value: 12+10+15=37)

##  Algorithm Analysis

### Time Complexity
- **2D DP Table:** O(n × W)
- **Space Optimized:** O(n × W) time, O(W) space

### Space Complexity
- **2D DP Table:** O(n × W)
- **Space Optimized:** O(W)

##  Complete Python Implementation

### Approach 1: 2D DP Table
```python
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
    
    # Create DP table with (n+1) rows and (capacity+1) columns
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build table bottom-up
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(
                    dp[i - 1][w],  # Don't take item
                    dp[i - 1][w - weight] + value  # Take item
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find which items were taken
    items_taken = []
    w = capacity
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_taken.append(i - 1)
            w -= items[i - 1][0]
    
    items_taken.reverse()
    
    return dp[n][capacity], items_taken
