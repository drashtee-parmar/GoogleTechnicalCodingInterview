
# ------------------------------- Approaches ---------------------------
# To determine the minimum number of conference rooms required for a set of meeting intervals, we need to keep track of overlapping intervals efficiently.
# The key idea is to track the number of simultaneous meetings happening at any given time. Here’s how we can do this efficiently using sorting and two pointers:
#
# Approach
#
# 	1.	Separate Start and End Times:
# 	•	Extract the start times and end times from the intervals and store them in separate lists: start_times and end_times.
# 	2.	Sort Both Lists:
# 	•	Sort both start_times and end_times. This allows us to efficiently determine when meetings start and end as we iterate through the events.
# 	3.	Iterate Through the Start Times:
# 	•	Use two pointers: i for start_times and j for end_times.
# 	•	For each start time, check if it’s before the next end time:
# 	•	If it is, it means a new meeting is starting before the previous one has ended, so we need a new room.
#      	Increment the count of rooms and move the i pointer.
# 	•	If the start time is not before the next end time, it means a meeting has ended, and we can reuse that room.
#   	Move both pointers i and j (indicating that one room is freed up).
# 	4.	Track the Maximum Number of Rooms:
# 	•	Track the maximum number of rooms required during this process using a variable rooms.

class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        # Extract start and end times separately
        start_times = []
        end_times = []
        for interval in intervals:
            start_times.append(interval[0])
            end_times.append(interval[1])

        # Sort the start and end times separately
        start_times.sort()
        end_times.sort()

        # Initialize pointers for start and end times
        start_pointer = 0
        end_pointer = 0
        rooms = 0
        max_rooms = 0

        # Iterate through all start times
        while start_pointer < len(intervals):
            if start_times[start_pointer] < end_times[end_pointer]:
                # A new meeting starts before the previous one ends, need a new room
                rooms += 1
                start_pointer += 1
            else:
                # A meeting has ended, free up a room
                rooms -= 1
                end_pointer += 1

            # Update the maximum rooms needed
            max_rooms = max(max_rooms, rooms)

        return max_rooms
#     Explaination
# 1.	Extract Start and End Times:
# 	•	We use separate for loops to extract the start times and end times from each interval:
        # start_times = []
        # end_times = []
        # for interval in intervals:
        #     start_times.append(interval[0])
        #     end_times.append(interval[1])
# 2.	Sort Start and End Times:
# 	•	We sort the start_times and end_times separately using the sort() method:
        # start_times.sort()
        # end_times.sort()
# 3.	Two-Pointer Approach:
# 	•	We use two pointers, start_pointer and end_pointer, to iterate through the sorted start and end times.
# 	•	If the start time at start_pointer is less than the end time at end_pointer, it means a new meeting starts before the previous one ends, so we increment the room count.
# 	•	Otherwise, a meeting has ended, so we decrement the room count and move both pointers.
# 	4.	Track Maximum Rooms Needed:
# 	•	We update max_rooms during each iteration to keep track of the maximum number of rooms needed.

# ----------------------------- Complexity --------------------------------
# Complexity
#
# 	•	Time Complexity: O(n \log n) due to sorting the start_times and end_times arrays separately.
#   	The iteration through the intervals takes O(n), but the overall complexity remains O(n \log n).
# 	•	Space Complexity: O(n) for storing the start_times and end_times arrays.

#  --------------------------- Testing --------------------------
solution = Solution()

# Example 1
print(solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
# Output: 2

# Example 2
print(solution.minMeetingRooms([[7, 10], [2, 4]]))
# Output: 1
