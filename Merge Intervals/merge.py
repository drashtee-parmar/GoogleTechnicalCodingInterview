#To solve the problem of merging overlapping intervals, we need to follow a systematic approach that involves sorting the intervals and merging them based on their overlap. Here’s a detailed explanation and implementation:

# ------------------------------ Approach -------------------------------
#
# 	1.	Sort the Intervals:
# 	•	First, we sort the intervals by their start time.
#   	This helps us efficiently merge overlapping intervals by ensuring that they are in a predictable order.
# 	2.	Iterate Through the Sorted Intervals:
# 	•	We start with the first interval as our initial “current interval” and compare it with the next interval.
# 	•	If the start of the next interval is less than or equal to the end of the current interval, they overlap.
#   	We merge them by updating the end of the current interval to be the maximum of the current interval’s end and the next interval’s end.
# 	•	If they do not overlap, we add the current interval to the result list and move to the next interval as the new “current interval”.
# 	3.	Add the Last Interval:
# 	•	Since the loop only adds intervals when a non-overlapping interval is found, we must add the final interval to the result after the loop.

class Solution(object):
    def merge(self, intervals):
        # Define a function to extract the start time for sorting
        def sort_key(interval):
            return interval[0]

        # Sort intervals using the custom function as the key
        intervals.sort(key=sort_key)

        # Initialize a list to hold merged intervals
        merged = []

        # Iterate through the intervals
        for interval in intervals:
            # If merged is empty or the current interval does not overlap with the previous, add it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # If they overlap, merge the intervals by updating the end of the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# ------------------------------ Explanation -------------------------------
#
# 	1.	Define a Sorting Key Function:
# 	•	We define a simple function called sort_key that takes an interval as input and returns its start value (interval[0]).
# 	2.	Sort Using the Function:
# 	•	We pass the sort_key function as the key argument to the sort method.
#   	This achieves the same effect as using a lambda function but is more explicit.
# 	3.	Rest of the Implementation:
# 	•	The rest of the implementation remains the same,
#   	where we iterate through the sorted intervals and merge overlapping intervals into the merged list.

# Complexity
#
# 	•	Time Complexity: O(n \log n), where n is the number of intervals. The sorting operation is the most time-consuming part of the algorithm.
# 	•	Space Complexity: O(n) for the merged list.


# -------------------- Testing ---------------------
solution = Solution()

# Example 1
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Output: [[1, 6], [8, 10], [15, 18]]

# Example 2
print(solution.merge([[1, 4], [4, 5]]))
# Output: [[1, 5]]
