import pytest

list_one = [1,2,3,4] # Output should be [1,3,6,10]
list_two = [1,1,1,1,1] # Output should be [1,2,3,4,5]
list_three = [3,1,2,10,1] # Output should be [3,4,6,16,17]

def solution(incomingList):
    ######################################################
    ######################################################
    ################# Your code here: ####################

    for i in range(1, len(incomingList)):
        incomingList[i] += incomingList[i - 1]
    return incomingList


    ######################################################
    ######################################################



def test_func():
    assert solution(list_one) == [1,3,6,10]
    assert solution(list_two) == [1,2,3,4,5]
    assert solution(list_three) == [3,4,6,16,17]
