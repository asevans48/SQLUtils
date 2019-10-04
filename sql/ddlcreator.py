"""
Database layout generator

Usage:

Options:

"""

import json


def execute_queries(objects):
    """
    Execute queries for each object

    :param objects: The objects from sql objects
    """
    pass


def get_indices(layout_dict):
    """
    Get the layout dictionary

    :param layout_dict: The layout dictionary
    :return:    Index objects
    """
    pass


def get_tables(layout_dict):
    """
    Get the table objects

    :param layout_dict: The layout dictionary
    :return:    Table objects
    """
    pass


def get_schemas(layout_dict):
    """
    Get the schema objects
    :param layout_dict: The layout dictionary
    :return:    Schema objects
    """
    pass


def parse_layout(layout_dict):
    """
    Parse the layout and create schema, table, and index objects to be run as queries

    :param layout_dict: The layout dictionary from the json
    :return:    Layout objects in a dictionary
    """
    pass


def create_layout(self, fpath, conn):
    """
    Create the database layout from provided DDL

    :param fpath:   The fpath
    :param conn:    The connection to use
    """
    with open(fpath, 'r') as fp:
        layout = json.load(fp)
    if layout and type(layout) is dict:
        pass
    else:
        raise ValueError("Layout not Found in File")


if __name__ == "__main__":
    pass