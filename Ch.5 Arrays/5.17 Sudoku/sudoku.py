#code
def check_line(A, row, col):
    temp = []
    for i in range(9):
        if row == -1:
            if A[i][col] in temp:
                return False
            if A[i][col] != 0:
                temp.append(A[i][col])
        else:
            if A[row][i] in temp:
                return False
            if A[row][i] != 0:
                temp.append(A[row][i])
    return True

def check_squares(A, i , j):
    temp = []
    for a in range(3*i,3*i+3):
        for b in range(3*j,3*j+3):
            if A[a][b] in temp:
                return False
            if A[a][b] != 0:
                temp.append(A[a][b])
    return True

def sudoku_is_valid(A):
    for i in range(9):
        if not check_line(A, i, -1):
            return False
        if not check_line(A, -1, i):
            return False

    for i in range(3):
        for j in range(3):
            if not check_squares(A, i, j):
                return False
    
    return True

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sudoku_is_valid([
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        ), True)
        self.assertEqual(sudoku_is_valid([
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,9,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        ), False)
        self.assertEqual(sudoku_is_valid([
            [5,3,0,0,7,0,6,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        ), False)

unittest.main()