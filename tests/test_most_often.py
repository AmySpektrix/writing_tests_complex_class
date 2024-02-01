from lib.most_often import *

"""
when we use add_new it adds multiple items or value to the starting list
"""

def test_add_multiple_new_items():
    test_list = [1,2,3,4,5,6,1]
    most_often_test = MostOften(test_list)
    most_often_test.add_new(2) 
    most_often_test.add_new("29")
    most_often_test.add_new(1) 
    most_often_test.add_new(-5.5)
    most_often_test.add_new(None) 
    assert most_often_test.starting_list == [1,2,3,4,5,6,1,2,"29",1,-5.5,None]

"""
when we use get_most_often when there is a clear winner it returns the item which appears most often in the list
"""
def test_most_often_clear_winner():
    test_list = [1,2,3,4,5,6,1,2,"29",1,-5.5,None]
    most_often_test = MostOften(test_list)
    assert most_often_test.get_most_often() == 1

"""
when we use get_most_often it returns the item which appears most often in the list
"""
def test_most_often_no_clear_winner():
    test_list = [1,2,3,4,5,6,1,2]
    most_often_test = MostOften(test_list)
    assert most_often_test.get_most_often() == "no clear winner"
