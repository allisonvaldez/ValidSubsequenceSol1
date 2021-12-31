# time: O(n) n represents the length of the array | space: O(1)


def test_valid_subsequence(array, sequence):
    """
    begin the code with first initializing the index for both the array and
    subsequence array
    """
    arrayIndex = 0
    sequenceIndex = 0

    """
    create a while loop that traverses both arrays with incrementing the
    indexes of both arrays when a match is found from each array.
    """
    while arrayIndex < len(array) and sequenceIndex < len(sequence):
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        arrayIndex += 1

    # return the sequence index at that particular length of the sequence
    return sequenceIndex == len(sequence)
