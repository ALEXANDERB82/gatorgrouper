import gatorgrouper
import string
import random


def test_create_escaped_string_from_list():
    """Testing the create_escaped_string_from_list() function
        with a list of normal input size"""
    list = ["Dan", "Nick", "Jeff", "Nikki", "Angie", "Austin"]
    desired_output_string = "Dan\nNick\nJeff\nNikki\nAngie\nAustin\n"
    actual_output_string = gatorgrouper.create_escaped_string_from_list(list)
    assert len(list) == 6
    assert ("Dan" in actual_output_string) is True
    assert ("Austin" in actual_output_string) is True
    assert (desired_output_string == actual_output_string) is True


def test_create_escaped_string_from_list_with_empty_list():
    """Testing the create_escaped_string_from_list() function
        with an empty list as input"""
    list = []
    desired_output_string = ""
    actual_output_string = gatorgrouper.create_escaped_string_from_list(list)
    assert len(list) == 0
    assert (desired_output_string == actual_output_string) is True


def test_create_escaped_string_from_list_with_large_list():
    """Testing the create_escaped_string_from_list() function
        with a list of large input size"""
    list = []
    extra_list = []
    desired_output_string = ""
    chars = string.ascii_uppercase + string.ascii_lowercase

    # populate the list with 250 random strings
    for i in range(0, 250):
        random_string = ''.join(random.choice(chars) for _ in range(5))
        list.append(random_string)
        extra_list.append(random_string + '\n')

    # add the new line character at the end of each string in the list
    desired_output_string = ''.join(extra_list)
    # running the function with our large input list
    actual_output_string = gatorgrouper.create_escaped_string_from_list(list)

    assert len(list) == 250
    assert len(extra_list) == 250
    assert (desired_output_string == actual_output_string) is True
