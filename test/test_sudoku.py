import pytest
from src import sudoku as S
from collections import Counter

class Helpers():
    """
    a class that groups helper functions required for testing
    """
    @staticmethod
    def element_counter(matrix):
        """
        counts the frequency of an element in matrix

        Arguments:
            matrix {list of list} - sudoku matrix

        Returns:
            result_dict {dictionary} - with elements as keys and frequency as value
        """
        result_counter = Counter()
        for list_ in matrix:
            temp_dict = {x: list_.count(x) for x in list_}
            result_counter = result_counter + Counter(temp_dict)
        
        return dict(result_counter)


@pytest.fixture
def helpers():
    return Helpers


class TestSudoku():
    def test_sudoku_output(self):
        """
        taking inputs for which deterministic solution exists
        """
        input_ = [[8, 5, 0, 0, 0, 2, 4, 0, 0],
                  [7, 2, 0, 0, 0, 0, 0, 0, 9],
                  [0, 0, 4, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 7, 0, 0, 2], 
                  [3, 0, 5, 0, 0, 0, 9, 0, 0], 
                  [0, 4, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 8, 0, 0, 7, 0], 
                  [0, 1, 7, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 3, 6, 0, 4, 0]]
        expected_result = [[8, 5, 9, 6, 1, 2, 4, 3, 7], 
                           [7, 2, 3, 8, 5, 4, 1, 6, 9], 
                           [1, 6, 4, 3, 7, 9, 5, 2, 8], 
                           [9, 8, 6, 1, 4, 7, 3, 5, 2], 
                           [3, 7, 5, 2, 6, 8, 9, 1, 4], 
                           [2, 4, 1, 5, 9, 3, 7, 8, 6], 
                           [4, 3, 2, 9, 8, 1, 6, 7, 5], 
                           [6, 1, 7, 4, 2, 5, 8, 9, 3], 
                           [5, 9, 8, 7, 3, 6, 2, 4, 1]]

        sdk_obj = S.Sudoku(input_)
        result = sdk_obj.get_solution()
        assert result == expected_result

    
    def test_sudoku_count(self, helpers):
        """
        checking the basic rule that a number must not repeat itself,
        i.e. count of every number should be equal to 9
        """
        input_ = [[0, 0, 0, 0, 0, 6, 0, 0, 0], 
                  [0, 5, 9, 0, 0, 0, 0, 0, 8], 
                  [2, 0, 0, 0, 0, 8, 0, 0, 0], 
                  [0, 4, 5, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 3, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 6, 0, 0, 3, 0, 5, 4], 
                  [0, 0, 0, 3, 2, 5, 0, 0, 6],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        expected_dict = {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 9, 8: 9, 9: 9}
        sdk_obj = S.Sudoku(input_)
        result = sdk_obj.get_solution()
        result_dict = helpers.element_counter(result)
        assert result_dict == expected_dict