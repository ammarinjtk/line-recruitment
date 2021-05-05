"""This script is expected to run by a command `python line_interview_test.py --input "5\n8 8 2 4 8"`."""

import argparse
import collections
import typing


def majorityElement(nums: typing.List[int]) -> int: 
    """
        Find majority of the given list of N elements.
        This solution used time complexity of O(n) and space complexity of O(n).
        :type nums: List[int]
        :rtype: int
    """
    
    freq = collections.defaultdict(int)

    # Count the occurances of each number using Default Dict   
    for n in nums:
        freq[n] += 1

        # For time efficiency, if we found the number whose (counter > len(nums)/2), return that number
        if freq[n] > len(nums)/2:
            return n

    # If any majority has not found, return -1
    return -1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Inputs for the LINE technical coding test - Majority element of an array")
    parser.add_argument("--input", dest="input", type=str, help="Input format of the number of elements N and the array of N elements, seperated by a new line")

    args = parser.parse_args()

    # Handle a new line in the input argument which is a escape character
    inputs = args.input.replace("\\n", "\n")
    
    # If the input format is invalid, raise an error to exit the program
    if len(inputs.split("\n")) != 2:
        raise argparse.ArgumentTypeError("The input is invalid, it should be 2 elements after seperated by a new line")
    
    _, arrays_str = inputs.split("\n")

    # Use strip() to handle any leading or trailing space
    arrays = arrays_str.strip().split(" ")
    output = majorityElement(arrays)

    # Print input and output to STDOUT
    print("-"*75)
    print(f"Inputs:\n\n{inputs}")
    print("-"*75)
    print(f"Output:\n\n{output}")
    print("-"*75)