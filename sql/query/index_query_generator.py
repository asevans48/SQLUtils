"""
Query generator for indices

@author Andrew Evans
"""

def generate_index_query(index):
    """
    Generate a query from a given index

    :param index:   The index object
    :return:    A relevant query
    """
    q = "CREATE"
    if index.unique:
        q = "{} UNIQUE".format(q)
    q = "{} INDEX".format(q)
    if index.concurrent:
        q = "{} CONCURRENTLY".format(q)
    q = "{} {} ON {}".format(q, index.name, index.table)
    if index.using:
        q = "{} USING {}".format(q, index.using)
    fields = ','.format(index.columns)
    q = "{}({})".format(q, fields)
    if index.use_with:
        with_list = ','.join(index.use_with)
        q = "{} WITH ({})".format(q, with_list)
    if index.tablespace:
        q = "{} TABLESPACE {}".format(q, index.tablespace)
    if index.condition:
        q = "{} WHERE {}".format(q, index.condition)
    return q