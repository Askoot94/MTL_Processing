import pytest
import os
from .. import tools

@pytest.fixture(autouse=True)
def directory():
    return os.path.dirname(os.path.abspath(__file__)) + "\\glossary_testfiles\\"


# Test that given a proper formatted 1 equal sign per line
def test_goodcase(directory):
    # Arrange
    expected_result = [{"find":"クロウ", "replace":"Kuro"},{"find":"シロウ", "replace":"Shiro"}]
    
    # Act
    actual = tools.glossary.createGlossary(os.path.join(directory, "goodcase.txt"))

    # Assert
    assert expected_result == actual

# Tests that the function throws an error message saying terms are not seperated by newlines
def test_multiterm_case(directory):
    with pytest.raises(Exception):
        tools.glossary.createGlossary(os.path.join(directory, "multiterm.txt"))

# Tests that it will not break if given an empty file
def test_empty_case(directory):
    # Arrange
    expected_result = list(dict())

    # Act
    try:
        actual = tools.glossary.createGlossary(os.path.join(directory, "empty.txt"))

    except:
        assert False

    # Assert
    assert expected_result == actual