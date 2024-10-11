

# To generate the first numRows of Pascal’s triangle,
# we can build it row by row, using the property that each element in the triangle is the sum of the two elements directly
# above it from the previous row.
# Here’s how you can implement this in Python:

class Solution:
    def generate(self, numRows: int):
        # Initialize the triangle with the first row
        triangle = [[1]]

        # Generate each row from the second row to the numRows
        for i in range(1, numRows):
            row = [1]  # The first element is always 1
            # Fill in the middle elements based on the previous row
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # The last element is always 1
            triangle.append(row)

        return triangle

# --------------------- Explaination -----------------------
# 1.	Initialize the Triangle:
# 	•	Start by creating the first row of Pascal’s triangle: [[1]].
# 	2.	Iterate to Build Each Row:
# 	•	For each row i from 1 to numRows - 1, create a new row:
# 	•	The first element of each row is always 1.
# 	•	For the middle elements (if any), use the formula:
#
# \text{row}[j] = \text{triangle}[i-1][j-1] + \text{triangle}[i-1][j]
#
# This sums the two elements directly above the current position.
# 	•	The last element of each row is also 1.
# 	•	Append the row to the triangle.
# 	3.	Return the Triangle:
# 	•	After generating all the rows, return the entire triangle.

#
# --------------------- Complexity -----------------------

# 	•	Time Complexity: O(\text{numRows}^2)
# 	•	We build each row based on the previous one, and the number of operations for each row grows linearly with its length.
# 	•	Space Complexity: O(\text{numRows}^2)
# 	•	The space used by the triangle grows with the number of rows and the number of elements in each row.

solution = Solution()

# Example 1
print(solution.generate(5))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Example 2
print(solution.generate(1))
# Output: [[1]]
