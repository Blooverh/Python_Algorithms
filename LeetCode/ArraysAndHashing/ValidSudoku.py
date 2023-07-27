"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according 
to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res =[]
        for i in range(9):
            for j in range(9):
                element = board[i][j]

                if element != '.':
                    res += [(i, element) , (element, j), (i //3 , j//3, element)]
                
        return len(res) == len(set(res)) 
    
# Explanation
"""
- Initialize an empty list called res, which will be used to store all valid elements in the board
- loops trough each cell in the board using nested loops for iteration
    For each cell, it retrieves the value of the element in that cell and stores it in a variable element
- If the element is not "." it means it is a valid number, the method adds 3 tuples to the res list:
    . first tuple contains row index i and element
    . second tuple contains column index j and element 
    . third tuple contains floor division of the row index by 3 and column index by 3, and element itself
        This tuple represents the 3x3 subgrid that the current cell belongs to
- After processing all the cells, the method checks if the length of res is equal to the 
    length of the set of res

    Because different length on res and set(res) means that there are the same tuples in res.
    Moreover, we need to notice that tuples representing different groups are never equal 
    (since tuple for row is Tuple[int, str] type, tuple for column is Tuple[str, int] 
    and sub-box - Tuple[int, int, str]).
    So, any tuples' equality means there are 2 equal tuples from the same group. 
    And that means the same element in one row, in one column or in one sub-box respectively.
"""