import pytest
import os
from ..tools.glossary import createGlossary as SUT
# SUT = System Under Test

@pytest.fixture(autouse=True)
def directory():
    return os.path.dirname(os.path.abspath(__file__)) + "\\glossary_testfiles\\"


# Test that given a proper formatted 1 equal sign per line
def test_goodcase(directory):
    # Arrange
    expected_result = [{"find":"クロウ", "replace":"Kuro"},{"find":"シロウ", "replace":"Shiro"}]
    
    # Act
    actual = SUT(os.path.join(directory, "goodcase.txt"))

    # Assert
    assert expected_result == actual

# Tests that it will not break if given an empty file
def test_empty_case(directory):
    # Arrange
    expected_result = list(dict())

    # Act
    try:
        actual = SUT(os.path.join(directory, "empty.txt"))

    except:
        assert False

    # Assert
    assert expected_result == actual

# Test that the glossary will return an empty list of dictionaries if a given file is not found
def test_file_not_found(directory):
    actual = SUT(os.path.join(directory, "nofile.txt"))

    assert actual == []

