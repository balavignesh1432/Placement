def maxProfit(self, prices):
    # profit = 0
        
    # Brute - TC = O(N*2), SC - O(1) 
    for i in range(len(prices)):
        for j in range(i+1 , len(prices)):
            if prices[j] - prices[i] > profit:
                maxi = prices[j] - prices[i]
    return profit

    # Using precomputation, Storing minimum to the left
    # TC = O(N), SC = O(N)
    prefixMin = [prices[0]]
    for i in range(1, len(prices)):
        if prices[i] < prefixMin[-1]:
            prefixMin.append(prices[i]) # If any less, then add it as last
        else:
            prefixMin.append(prefixMin[-1]) # If not less, then add prev as last again
    
    for i in range(1, len(prices)):
        if prices[i] - prefixMin[i-1] > profit:
            profit = prices[i] - prefixMin[i-1]
    return profit

    # Since only iteration in one direction and minimum towards left is needed
    # No need to store minimum so far for each index
    # Just one variable can keep track of minimum so far
    # And Max profit can be calculated based on it
    # TC = O(N), SC = O(1)
    mini = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] - mini > profit:
            profit = prices[i] - mini
        if prices[i] < mini:
            mini = prices[i]
    return profit

    # TC = O(N), SC = O(1)
    # Sliding Window. Left of sliding window will always be at lowest seen so far.
    # No need to worry about moving left pointer if seeing something low than it,
    # Because if something high appears at right, then profit will be even more,
    # If left moved to lower value seen so far.
    # Right side will always increase by 1
    # Keep calculating profit, and find max
    l = 0   # Window starts from left with size two
    r = 1
    profit = 0
    while r < len(prices):
        profit = max(profit, prices[r] - prices[l]) # Compute Max Profit at each stage
        if prices[l] >= prices[r]:  # If right is at low, update left at low for next iteration
            l = r 
        r += 1  # Update right each iteration
    return profit
        