def knapsack(items, weights, values, capacity):
    # Create a 2D array to store the solutions of subproblems
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    # Fill the first row and col with zeros
    for i in range(capacity + 1):
        dp[0][i] = 0

    for j in range(len(items) + 1):
        dp[j][0] = 0

    # Dynamic programming logic
    for i in range(1, len(items) + 1):
        for w in range(1, capacity + 1):
            # If weight of item is more than the knapsack capacity
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            # If weight of item is less than equal to the knapsack capacity
            else:
                # We will add the item and the profit
                add_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Not adding the item
                dont_add_item = dp[i - 1][w]

                # Choose max
                dp[i][w] = max(add_item, dont_add_item)

    return dp[len(items)][capacity]

# Example usage:
items = [3, 4, 8, 5]  # Item's weight
values = [10, 40, 30, 50]  # Item's value
capacity = 50  # Knapsack capacity
print(knapsack(items, values, capacity))