from src import sudoku as S

def test_sudoku():
    input_1 = [[8, 5, 0, 0, 0, 2, 4, 0, 0],
               [7, 2, 0, 0, 0, 0, 0, 0, 9],
               [0, 0, 4, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 7, 0, 0, 2], 
               [3, 0, 5, 0, 0, 0, 9, 0, 0], 
               [0, 4, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 8, 0, 0, 7, 0], 
               [0, 1, 7, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 3, 6, 0, 4, 0]]
    output_1 = [[8, 5, 9, 6, 1, 2, 4, 3, 7], 
                [7, 2, 3, 8, 5, 4, 1, 6, 9], 
                [1, 6, 4, 3, 7, 9, 5, 2, 8], 
                [9, 8, 6, 1, 4, 7, 3, 5, 2], 
                [3, 7, 5, 2, 6, 8, 9, 1, 4], 
                [2, 4, 1, 5, 9, 3, 7, 8, 6], 
                [4, 3, 2, 9, 8, 1, 6, 7, 5], 
                [6, 1, 7, 4, 2, 5, 8, 9, 3], 
                [5, 9, 8, 7, 3, 6, 2, 4, 1]]

    input_2 = [[0, 0, 0, 0, 0, 6, 0, 0, 0], 
               [0, 5, 9, 0, 0, 0, 0, 0, 8], 
               [2, 0, 0, 0, 0, 8, 0, 0, 0], 
               [0, 4, 5, 0, 0, 0, 0, 0, 0], 
               [0, 0, 3, 0, 0, 0, 0, 0, 0], 
               [0, 0, 6, 0, 0, 3, 0, 5, 4], 
               [0, 0, 0, 3, 2, 5, 0, 0, 6],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    sdk_obj_1 = S.Sudoku(input_1)
    result_1 = sdk_obj_1.get_solution()
    assert result_1 == output_1

    # because multiple solutions are possible, test basic output rules
    sdk_obj_2 = S.Sudoku(input_2)
    result_2 = sdk_obj_2.get_solution()
        