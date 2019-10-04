"""
Query generator to create a schema

@author Andrew Evans
"""


def generate_query(schema):
    """
    Generate a create schema query

    :param schema:  The schema object
    :return:    The create schema string
    """
    q = None
    if schema:
        q = "CREATE SCHEMA"
        if schema.if_not_exists:
            q = "{} IF NOT EXISTS".format(q)
        if schema.name:
            q = "{} {}".format(q, schema.name)
        if schema.authorization:
            q = "{} AUTHORIZATION {}".format(q, schema.authorization)
    return q
