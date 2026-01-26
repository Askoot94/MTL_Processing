import pytest
from .. import tools

# change this to a fixture
test_dir = "./glossary_testfiles/"

# Test that given a proper formatted 1 equal sign per line
def test_goodcase():
    # Arrange
    expected_result = [{"find":"クロウ", "replace":"Kuro"},{"find":"クロウ", "replace":"Kuro"}]
    
    # Act
    actual = tools.glossary.createGlossary(test_dir + "goodcase.txt")

    # Assert
    assert expected_result == actual

# Tests that the function throws an error message saying terms are not seperated by newlines
def test_multiterm_case():
    with pytest.raises(Exception):
        tools.glossary.createGlossary(test_dir + "multiterm.txt")

# Tests that it will not break if given a empty file
def test_empty_case():
    # Arrange
    expected_result = list(dict())

    # Act
    try:
        actual = tools.glossary.createGlossary(test_dir + "empty.txt")

    except:
        assert False

    # Assert
    assert expected_result == actual