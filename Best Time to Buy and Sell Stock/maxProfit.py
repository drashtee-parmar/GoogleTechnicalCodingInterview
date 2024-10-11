
# To solve the problem of finding the maximum profit from buying and selling stock on different days, we can use a single pass approach to keep track of the minimum price encountered so far and the maximum profit possible at each step. This approach is efficient with a time complexity of O(n) and a space complexity of O(1).
#
# Approach
#
# 	1.	Initialize Variables:
# 	•	min_price: This variable keeps track of the minimum price seen so far as we iterate through the array. We initialize it to a very high value (float('inf')).
# 	•	max_profit: This variable keeps track of the maximum profit possible as we iterate through the array. We initialize it to 0.
# 	2.	Iterate Through the Prices:
# 	•	For each price in the array:
# 	•	Update min_price to be the smaller of the current min_price or the current price. This keeps track of the lowest price before the current day.
# 	•	Calculate the potential profit if we were to sell at the current price (price - min_price).
# 	•	Update max_profit if this potential profit is greater than the current max_profit.
# 	3.	Return the Maximum Profit:
# 	•	If no profit can be made (i.e., prices are always decreasing), max_profit will remain 0.
class Solution(object):
    def maxProfit(self, prices):
        # Initialize variables
        min_price = float('inf')
        max_profit = 0

        # Iterate through each price
        for price in prices:
            # Update the min_price to be the smallest seen so far
            min_price = min(min_price, price)
            # Calculate the profit if selling at the current price
            profit = price - min_price
            # Update max_profit if the current profit is larger
            max_profit = max(max_profit, profit)

        return max_profit
#----------------------- Complexity -------------------
#
# 	•	Time Complexity: O(n), where n is the length of the prices array. We only iterate through the array once.
# 	•	Space Complexity: O(1), as we are only using a few variables (min_price and max_profit) for tracking the minimum price and maximum profit.

# ---------------------- Testing ----------------
solution = Solution()

# Example 1
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5 (Buy at 1, sell at 6)

# Example 2
print(solution.maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (No profit possible)
