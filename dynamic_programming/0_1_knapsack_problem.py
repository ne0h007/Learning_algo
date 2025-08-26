# brute force technique

def knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0  # To track the maximum value found
    total_subsets = 2 ** n  # There are 2^n possible subsets

    for subset in range(total_subsets):  # Iterate over all subsets
        total_weight = 0
        total_value = 0

        for i in range(n):  # Check if item i is included in the subset
            if (subset & (1 << i)) != 0:  # If the i-th bit of subset is set
                total_weight += weights[i]
                total_value += values[i]

        # Check if the total weight is within the knapsack's capacity
        if total_weight <= capacity:
            max_value = max(max_value, total_value)  # Update maximum value if needed

    return max_value

# another brute force 

# Returns the maximum value that
# can be put in a knapsack of capacity W
def knapsackRec(W, val, wt, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    pick = 0

    # Pick nth item if it does not exceed the capacity of knapsack
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1)
    
    # Don't pick the nth item
    notPick = knapsackRec(W, val, wt, n - 1)
     
    return max(pick, notPick)

def knapsack(W, val, wt):
    n = len(val)
    return knapsackRec(W, val, wt, n)

if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapsack(W, val, wt))
