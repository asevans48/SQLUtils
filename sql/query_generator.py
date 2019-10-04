"""
A query generator

@author Andrew Evans
"""


def generate_query(table_object):
    """
    Query generator

    :param table_object:    The table object
    :return:    Query or none if impossible to generate
    """
    query = None
    if table_object:
        schema = table_object.schema
        table = table_object.table
        fields = table_object.fields
        if fields:
            if schema:
                query = "CREATE TABLE {}.{} {}".format(schema, table, str(fields))
            else:
                query = "CREATE TABLE {} {}".format(table, str(fields))

    return query