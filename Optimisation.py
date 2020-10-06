"""
Nikit Parakh
Optimisation
"""
from typing import List, Tuple


def Optimise(grid: List[List[int]], k: int) -> Tuple[int, int, int]:
    """
    Given an n x n 2D list of 0's and 1's and an integer k, determine the greatest number of 1's
    that can be covered by a square of size k x k. Return a tuple (a, b, c) where
        a = number of 1's this optimal k x k square covers
        b = the row of the top left corner of this square
        c = the col of the top left corner of this square
    :param grid: [list[list[int]]] a square 2D list of 0, 1 integers
    :param k: [int] the size of the square placed to cover 1's
    :return: [tuple[int, int, int]] a tuple (a, b, c) where
        a = number of 1's this optimal k x k square covers
        b = the row of the top left corner of this square
        c = the col of the top left corner of this square
    """
    # return number of 1s in entire grid if k is equal to the length of grid
    if k == len(grid):
        return(sum(i.count(1) for i in grid), 0, 0)
    # return 0, 0, 0 if k is 0
    if k == 0:
        return (0, 0, 0)
    # create dictionary to store index of top left element in k x k block and 1s in it
    counts = {}

    # number of 1s in first k x k block
    current = sum(i[:k].count(1) for i in grid[:k])
    # number of 1s in the top row of current block
    top = sum(grid[0][:k])
    # add first block to dictionary
    counts[(0, 0)] = current

    # Loop over the grid
    for j in range(len(grid)-k+1):
        for i in range(len(grid)-k+1):
            # skip first block as it is already added
            if i == 0 and j == 0:
                continue
            # if block is not on first row
            if i != 0:
                # calculate number of 1s using the count from the block just above
                # by removing the 1s from top and adding from the row right below
                # essentially shifting down the rows by 1.
                # The sum function here acts on a 1 x k block thus we get O[[n^2][k]]
                # and not O[[n^2][k^2]]
                counts[(i, j)] = current - top + sum(grid[i+k-1][j:j+k])
                # set new top and current values
                current = counts[(i, j)]
                top = sum(grid[i][j:j+k])
            # if block is on first row
            else:
                # calculate number of 1s using the count from the block just left
                # by removing the 1s in the first column and adding from the rightmost new column
                # essentially shifting right by 1 column
                # The sum function here acts on a k x 1 block thus we get O[[n^2][k]]
                # and not O[[n^2][k^2]]
                counts[(i, j)] = counts[(i, j-1)] - sum(f[j-1] for f in grid[:k]) \
                                 + sum(f[j+k-1] for f in grid[:k])
                # set new current and top values
                current = counts[(i, j)]
                top = sum(grid[i][j:j+k])

    # get indices with highest number of 1s and the number of 1s in that block
    (row_index, col_index) = max(counts, key=lambda x: counts[x])
    return(counts[(row_index, col_index)], row_index, col_index)
