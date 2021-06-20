import pytest

list_one = [1,2,3,4] # Output should be [1,3,6,10]
list_two = [1,1,1,1,1] # Output should be [1,2,3,4,5]
list_three = [3,1,2,10,1] # Output should be [3,4,6,16,17]


# Incoming list is list_one. list_two and list_three
def solution(incomingList):
    ######################################################
    ######################################################
    ################# Your code here: ####################
    # example: print(incomingList)


    ######################################################
    ######################################################
    pass



def test_func():
    assert solution(list_one) == [1,3,6,10]
    assert solution(list_two) == [1,2,3,4,5]
    assert solution(list_three) == [3,4,6,16,17]
