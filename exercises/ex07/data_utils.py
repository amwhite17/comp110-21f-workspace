from csv import DictReader

"""Utility functions."""

__author__ = "123456789"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Csv rows into table."""
    result: list[dict[str, str]] = []

    # Data file handle
    file_handle = open(filename, "r", encoding="utf8")

    # Data file as csv
    csv_reader = DictReader(file_handle)

    # Read the rows
    for row in csv_reader:
        result.append(row)

    # Close file
    file_handle.close()

    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """List for values in column."""
    result: list[str] = []
    for row in table:
        value: str = row[column]
        result.append(value)
    return result 

    
def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Row oriented to column oriented."""
    result: dict[str, list[str]] = {}
    first: dict[str, str] = row_table[0]
    for column in first:
        result[column] = column_values(row_table, column)
    return result 


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """New column table."""
    returned_dict: dict[str, list[str]] = {}
    i = 0
    for column in column_table:
        returned_dict[column] = []
        if rows >= len(column_table[column]):
            return column_table 
        while i < rows:
            returned_dict[column].append(column_table[column][i])
            i += 1
        i = 0
    return(returned_dict)


def select(column_based: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """New column table with certain columns."""
    new: dict[str, list[str]] = {}
    for column in column_based:
        for name in names:
            if name == column:
                new[column] = column_based[column]
    return new


def concat(first_dict: dict[str, list[str]], second_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Column table of two different column tables."""
    third_dict: dict[str, list[str]] = {}
    for column in first_dict:
        third_dict[column] = first_dict[column]
    for column in second_dict:
        if column in third_dict.keys():
            i = 0
            while i < len(second_dict[column]):
                third_dict[column].append(second_dict[column][i])
                i += 1
        else:
            third_dict[column] = second_dict[column]
    return third_dict


def count(values: list[str]) -> dict[str, int]:
    """Column table of frequencies."""
    empty: dict[str, int] = {}
    for a in values:
        if a not in empty:
            empty[a] = 1
        else:
            empty[a] += 1
    return empty