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
            fstr = ','.join([str(x) for x in fields])
            pkeys = [x for x in fields if x.primary_key is True]
            if pkeys and len(pkeys) > 0:
                pstr = ','.join([x.name for x in pkeys])
                pstr = '({})'.format(pstr)
                fstr = "{}, PRIMARY KEY {}".format(fstr, pstr)
            fstr = "({})".format(fstr)
            if table_object.if_not_exists:
                query = "{} IF NOT EXISTS".format(query)
            if schema:
                query = "{} {}.{} {}".format(query, schema, table, fstr)
            else:
                query = "{} {} {}".format(query, table, fstr)
    return query
