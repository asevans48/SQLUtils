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
            query = "CREATE TABLE"
            if table_object.if_not_exists:
                query = "{} IF NOT EXISTS".format(query)
            if schema:
                query = "{} {}.{} {}".format(query, schema, table, str(fields))
            else:
                query = "{} {} {}".format(query, table, str(fields))
    return query
