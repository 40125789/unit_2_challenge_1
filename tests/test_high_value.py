from lib.high_value import HighValue

#Test for initialisation
def test_initial_values_are_set():
    hv = HighValue(10, 20)
    assert hv.value_first == 10
    assert hv.value_second == 20

#Test for highest value for first value
def test_first_highest_value():
    hv = HighValue(8, 5)
    assert hv.get_highest() == "First value is higher"
    
    
#Test for highest value for second value
def test_second_highest_value():
    hv = HighValue(5, 8)
    assert hv.get_highest() == "Second value is higher"
    
#Test for highest value for equal values
def test_equal_values():
    hv = HighValue(8, 8)
    assert hv.get_highest() == "Values are equal"
    
#Test add function for first value
def test_add_increases_first_value():
    hv = HighValue(3, 10)
    hv.add(3, "first")
    assert hv.value_first == 6
    assert hv.value_second == 10
    

#Test add function for second value
def test_add_increases_second_value():
    hv = HighValue(3, 10)
    hv.add(3, "second")
    assert hv.value_first == 3
    assert hv.value_second == 13

#Test add function where adding changes highest value
def test_add_changes_highest_value_to_first():
    hv = HighValue(5, 8)
    assert hv.get_highest() == "Second value is higher"
    hv.add(5, "first")
    assert hv.get_highest() == "First value is higher"

#Test add function where adding changes highest value
def test_add_changes_highest_value_to_second():
    hv = HighValue(8, 5)
    assert hv.get_highest() == "First value is higher"
    hv.add(5, "second")
    assert hv.get_highest() == "Second value is higher"

#Test add function where adding changes highest value to become equal
def test_add_changes_highest_value_to_equals():
    hv = HighValue(8, 5)
    assert hv.get_highest() == "First value is higher"
    hv.add(3, "second")
    assert hv.get_highest() == "Values are equal"
