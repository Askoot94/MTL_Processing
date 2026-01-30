import pytest
import os
from ..tools.glossary import createGlossary as SUT
# SUT = System Under Test

@pytest.fixture(autouse=True)
def directory():
    return os.path.dirname(os.path.abspath(__file__)) + "\\glossary_testfiles\\"


# Test that given a proper formatted 1 equal sign per line
def test_good_file(directory):
    # Arrange
    expected_result = [
        {"find":"Qrow", "replace":"Kuro"},
        {"find":"Natto", "replace":"Nats"}
        ]
    
    # Act
    actual = SUT(os.path.join(directory, "goodcase.txt"))

    # Assert
    assert expected_result == actual

def test_japanese_file(directory):
     # Arrange
    expected_result = [
        {"find":"クロウ", "replace":"Kuro"},
        {"find":"シロウ", "replace":"Shiro"}
        ]
    
    # Act
    actual = SUT(os.path.join(directory, "japanese.txt"))

    # Assert
    assert expected_result == actual

def test_chinese_file(directory):
     # Arrange
    expected_result = [
        {"find":"乔修", "replace":"Joshua"},
        {"find":"泽那斯", "replace":"Zenarth"},
        {"find":"罪业恶魔", "replace":"Sin Demon"}
        ]
    
    # Act
    actual = SUT(os.path.join(directory, "chinese.txt"))

    # Assert
    assert expected_result == actual

# Tests that it will not break if given an empty file
def test_empty_file(directory):
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
    actual = SUT(os.path.join(directory, "noFile.txt"))

    assert actual == []

def test_missing_equal_file(directory):
    expected = [
        {"find":"hello world", "replace":"oh no"},
        {"find":"", "replace":"boo"}]
    actual = SUT(os.path.join(directory, "missingEqual.txt"))

    assert actual == expected

def test_traling_newline_file(directory):
    expected = [
        {"find":"this", "replace":"test"}
    ]

    actual = SUT(os.path.join(directory, "trailingNewline.txt"))

    assert actual == expected

def test_good_text(directory):
    given = "crow=Kuro\nShirou=Shiro\nRamia=Lamia"

    expected = [
        {'find': "crow", 'replace': "Kuro"},
        {'find': "Shirou", 'replace': "Shiro"},
        {'find': "Ramia", 'replace': "Lamia"},
        ]

    actual = SUT(given)

    assert actual == expected

def test_empty_text(directory):
    given = ""

    expected = []

    actual = SUT(given)

    assert actual == expected

def test_missing_equal_text(directory):
    given = "This line does not have an equal sign\nBut it does=in the second line"

    expected = [{'find': "But it does", 'replace': "in the second line"}]

    actual = SUT(given)

    assert actual == expected

def test_chinese_text(directory):
    given = "万智牌=Magic: The Gathering\n炉石=Hearthstone\n"

    expected = [
        {'find': "万智牌", 'replace': "Magic: The Gathering"},
        {'find': "炉石", 'replace': "Hearthstone"}
        ]

    actual = SUT(given)

    assert actual == expected

def test_japanese_text(directory):
    given = "イチロウ=Ichirou\nササリス=Sasaris"

    expected = [
        {'find': "イチロウ", 'replace': "Ichirou"},
        {'find': "ササリス", 'replace': "Sasaris"}
        ]

    actual = SUT(given)

    assert actual == expected

def test_blank_oneside_text(directory):
    given = "=BLANK\nNOTHING="

    expected = [
        {'find': "", 'replace': "BLANK"},
        {'find': "NOTHING", 'replace': ""}
        ]

    actual = SUT(given)

    assert actual == expected

def test_blank_text(directory):
    given = "="

    expected = [
        {'find': "", 'replace': ""}
        ]

    actual = SUT(given)

    assert actual == expected