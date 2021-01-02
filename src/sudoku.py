class Sudoku(object):
    def __init__(self, sdk_arr):
        self.sdk_arr = sdk_arr


    def get_solution(self):
        """
        returns the Sudoku matrix
        """
        self.solution(self.sdk_arr)
        return self.sdk_arr

    
    def find_empty_cells(self, sdk_arr):
        """
        finds and returns the indices of the empty cells

        :args: sdk_arr
        :returns: indices (returns (-1, -1) when sudoku is solved)
        """
        for i in range(9):
            for j in range(9):
                if sdk_arr[i][j] == 0:
                    return i, j
        return -1, -1

    
    def is_valid(self, sdk_arr, i, j, entry):
        """
        checks whether a particular entry is valid or not

        :args: sdk_arr,
               i,j,
               entry
        :returns: Bool
        """
        row_valid = all([entry != sdk_arr[i][ii] for ii in range(9)])
        if row_valid:
            column_valid = all([entry != sdk_arr[jj][j] for jj in range(9)])
            if column_valid:
                # check the validity in the block
                block_i = 3*(i//3)
                block_j = 3*(j//3)
                for bi in range(block_i, block_i + 3):
                    for bj in range(block_j, block_j + 3):
                        if sdk_arr[bi][bj] == entry:
                            return False
                return True
        return False


    def solution(self, sdk_arr, i = 0, j = 0):
        """
        solves given sudoku puzzle

        :args: sdk_arr,
                i, j
        :returns: nothing
        """
        # base case: makes sure we have empty cells in the Sudoko
        i, j = self.find_empty_cells(sdk_arr)
        if i == -1:
            return True
        
        for num in range(1, 10):
            if self.is_valid(sdk_arr, i, j, num):
                sdk_arr[i][j] = num
                if self.solution(sdk_arr, i, j):
                    return True
                sdk_arr[i][j] = 0
        return False


    @staticmethod
    def boundry_condition(a):
        """
        checks the block boundry condition

        returns: Bool
        """
        if a%3 == 0 and a != 0:
            return True


    @staticmethod
    def print_sudoku(sdk_arr):
        """
        prints the sudoku in a block form
        """
        print()
        for i in range(9):
            row = ""
            if Sudoku.boundry_condition(i):
                print("---------------------")
            for j in range(9):
                if Sudoku.boundry_condition(j):
                    row += "|"
                row += str(sdk_arr[i][j]) + " "
            print(row)



if __name__=="__main__":
    sudoku_sample =    [[0, 6, 8, 0, 0, 0, 0, 0, 0], 
                        [7, 0, 0, 8, 0, 3, 0, 0, 5], 
                        [1, 3, 0, 0, 0, 0, 2, 4, 0], 
                        [4, 0, 0, 0, 2, 0, 0, 3, 0], 
                        [0, 0, 9, 3, 7, 4, 8, 0, 0], 
                        [0, 8, 0, 0, 9, 0, 0, 0, 7], 
                        [0, 4, 2, 0, 0, 0, 0, 8, 6], 
                        [8, 0, 0, 6, 0, 7, 0, 0, 4], 
                        [0, 0, 0, 0, 0, 0, 5, 1, 0]]

    sdk_obj = Sudoku(sudoku_sample)
    print("Unsolved:->", end = "")
    sdk_obj.print_sudoku(sudoku_sample)

    print("\nSolved:->", end = "")
    result = sdk_obj.get_solution()
    sdk_obj.print_sudoku(result)