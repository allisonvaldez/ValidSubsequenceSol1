# time: O(n) n represents the length of the array | space: O(1)


def test_valid_subsequence(array, sequent_array):
    """
    begin the code with first initializing the index for both the array and
    subsequence array
    """
    array_index = 0
    sequent_index = 0

    """
    create a while loop that traverses both arrays with incrementing the
    index of the subsequent array first when a match is found from the 
    original array (first array).
    """
    while array_index < len(array) and sequent_index < len(sequent_array):
        if array[array_index] == sequent_array[sequent_index]:
            sequent_index += 1
        """
        regardless if a match is found move forward in the first array 
        to continue to compare the arrays
        """
        array_index += 1

    """
    Returns true if we found all items in the original array that's equal to 
    the length of the sequent array (all items of the sequent array are found).
    """
    return sequent_index == len(sequent_array)


print(test_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
