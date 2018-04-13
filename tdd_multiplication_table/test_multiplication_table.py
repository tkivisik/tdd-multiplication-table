#!/usr/bin/env python3

import multiplication_table as mt
from multiplication_table import NotPositiveDimensionsException, TooBigDimensionsException
import pytest

@pytest.fixture
def table_5x5():
    '''Returns an empty MultiplicationTable'''
    return mt.MultiplicationTable(5,5,20)

def test_negative_dimensions():
    with pytest.raises(NotPositiveDimensionsException):
        mt.MultiplicationTable(-1,3)

def test_zero_zero_dimensions():
    with pytest.raises(NotPositiveDimensionsException):
        mt.MultiplicationTable(0,0)

def test_too_big_dimensions():
    dimension_max = 2
    ok_dimension = dimension_max
    too_big_dimension = dimension_max + 1
    with pytest.raises(TooBigDimensionsException):
        mt.MultiplicationTable(too_big_dimension, too_big_dimension, DIMENSION_MAX=dimension_max)
        mt.MultiplicationTable(too_big_dimension, ok_dimension, DIMENSION_MAX=dimension_max)
        mt.MultiplicationTable(ok_dimension, too_big_dimension, DIMENSION_MAX=dimension_max)

def test_correct_number_of_rows(table_5x5):
    rows = table_5x5.show_table_string().strip("\n").split("\n")
    assert len(rows) == 5

def test_correct_number_of_columns(table_5x5):
    rows = table_5x5.show_table_string().strip("\n").split("\n")
    for row in rows:
        columns = row.strip().split()
        assert len(columns) == 5

def test_first_element_not_zero(table_5x5):
    first_row = table_5x5.show_table_string().split("\n")[0]
    first_element = first_row.split()[0]
    assert int(first_element) != 0


@pytest.mark.parametrize("height,width,added_height,added_width,expected_height,expected_width", [
    (1, 1, 1, 0, 2, 1),
    (1, 1, 0, 1, 1, 2)
])
def test_adding_to_dimensions(height,width,added_height,added_width,expected_height,expected_width):
    table = mt.MultiplicationTable(height, width)
    
    if (table.DIMENSION_MAX-(height+added_height)) >= 0 and (table.DIMENSION_MAX-(width+added_width)) >= 0:
        table.update_height(added_height)
        table.update_width(added_width)
        assert table.height == expected_height
        assert table.width == expected_width
    else:
        with pytest.raises(TooBigDimensionsException):
            table.update_height(added_height)
            table.update_width(added_width)

@pytest.mark.parametrize("height,width,added_height,added_width,expected_height,expected_width", [
    (1, 1, "1", 0, 2, 1),
    (1, 1, "0", 1, 1, 2),
])
def test_adding_valid_int_strings_to_dimensions(height,width,added_height,added_width,expected_height,expected_width):
    table = mt.MultiplicationTable(height, width, 20)
    table.update_height(added_height)
    table.update_width(added_width)
    assert table.height == expected_height
    assert table.width == expected_width

@pytest.mark.parametrize("height,width,added_height,added_width,expected_height,expected_width", [
    (1, 1, 0, "1.0", 1, 2),
    (1, 1, "1.0", 0, 2, 1),
])
def test_adding_valid_float_strings_to_dimensions(height,width,added_height,added_width,expected_height,expected_width):
    table = mt.MultiplicationTable(height, width, 20)
    table.update_height(added_height)
    table.update_width(added_width)
    assert table.height == expected_height
    assert table.width == expected_width

@pytest.mark.parametrize("height,width,amount", [
    (1, 1, "1.1"),
    (1, 1, "1.5"),
    (1, 1, "1.9"),
    (1, 1, "0.1"),
    (1, 1, "0.9"),
    (10, 10, "-1.1"),
    (10, 10, "-1.5"),
    (10, 10, "-1.9"),
    (10, 10, "-0.1"),
    (10, 10, "-0.9"),
])
def test_adding_invalid_float_strings_to_height(height,width,amount):
    table = mt.MultiplicationTable(height, width, 20)
    with pytest.raises(TypeError):
        table.update_height(amount)

@pytest.mark.parametrize("height,width,amount", [
    (1, 1, "1.1"),
    (1, 1, "1.5"),
    (1, 1, "1.9"),
    (1, 1, "0.1"),
    (1, 1, "0.9"),
    (10, 10, "-1.1"),
    (10, 10, "-1.5"),
    (10, 10, "-1.9"),
    (10, 10, "-0.1"),
    (10, 10, "-0.9"),
])
def test_adding_invalid_float_strings_to_width(height,width,amount):
    table = mt.MultiplicationTable(height, width, 20)
    with pytest.raises(TypeError):
        table.update_width(amount)

@pytest.mark.parametrize("height,width,added_height,added_width,expected_height,expected_width", [
    (20, 20, -1, 0, 19, 20),
    (20, 20, 0, -1, 20, 19),
    (1, 1, -1, 0, 'error', 1),
    (1, 1, 0, -1, 1, 'error'),
])
def test_subtracting_from_dimensions(height,width,added_height,added_width,expected_height,expected_width):
    table = mt.MultiplicationTable(height, width, DIMENSION_MAX=20)
    
    if height+added_height >= 1 and width+added_width >= 1:
        table.update_height(added_height)
        table.update_width(added_width)
        assert table.height == expected_height
        assert table.width == expected_width
    else:
        with pytest.raises(NotPositiveDimensionsException):
            table.update_height(added_height)
            table.update_width(added_width)
