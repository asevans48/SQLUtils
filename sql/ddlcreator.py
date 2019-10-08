"""
DDL Creator From JSON file or object.

Usage:
  ddlcreator.py (-f | --file) <layout> <connstring>...
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  -f --file     Use argument as file

"""

import json

import psycopg2
from docopt import docopt

from sql.objects.fields import TableField
from sql.objects.fkey import FKIndex
from sql.objects.index import Index
from sql.objects.schema import Schema
from sql.objects.tables import Table


def execute_queries(objects, conn):
    """
    Execute queries for each object

    :param objects: The objects from sql objects
    :param conn: The connection to use
    """
    for obj in objects:
        q = str(obj)
        with conn.cursor() as cursor:
            cursor.execute(str(q))


def get_indices(layout_dict):
    """
    Get the layout dictionary

    :param layout_dict: The layout dictionary
    :return:    Index objects
    """
    rindices = []
    if layout_dict.get("indices", None):
        for idx in layout_dict["indices"]:
            name = idx.get("name", None)
            table = idx.get("table", None)
            columns = idx.get("columns", None)
            if name is not None and table is not None and columns is not None:
                idx_object = Index(name, table, columns)
                if idx.get("if_not_exists", False):
                    idx_object.if_not_exists = True
                if idx.get("schema", None):
                    idx_object.schema = idx["schema"]
                if idx.get("using", None):
                    idx_object.using = idx["using"]
                if idx.get("unique", False):
                    idx_object.unique = True
                if idx.get("concurrent", False):
                    idx_object.concurrent = True
                if idx.get("use_with", None):
                    idx_object.use_with = idx["use_with"]
                if idx.get("tablespace", None):
                    idx_object.tablespace = idx["tablespace"]
                if idx.get("condition", None):
                    idx_object.condition = idx["condition"]
                rindices.append(idx_object)
            else:
                msg = "Name, table, and columns must be present for index"
                raise ValueError(msg)
    return rindices


def get_fkey(fkey_dict):
    """
    Get the foreign key dict

    :param fkey_dict:   The foreign key dictionary
    :return:    Foreign key object
    """

    if fkey_dict.get("foreign_table_field", None):
        foreign_table_field = fkey_dict["foreign_table_field"]
        if fkey_dict.get("ref_table", None):
            ref_table = fkey_dict.get("ref_table")
            fkidx = FKIndex(ref_table, foreign_table_field)
        else:
            raise ValueError("Ref Table of Foreign Key Cannot be NoneType")
    else:
        raise ValueError("Foreign Table of Foreign Key Cannot be NoneType")
    return fkidx


def get_field(field_dict):
    """
    Create a field from a field dictionary

    :param field_dict:  The field dictionary
    :return:    The field object
    """
    if field_dict:
        name = field_dict.get("name", None)
        if name:
            ftype = field_dict.get("type", None)
            if ftype:
                field = TableField(name, ftype)
                primary_key = field_dict.get("primary_key", None)
                not_null = field_dict.get("not_null", True)
                foreign_key = field_dict.get("foreign_key", None)
                default_val = field_dict.get("default_val", None)
                if foreign_key:
                    foreign_key = get_fkey(foreign_key)
                    field.foreign_key = foreign_key
                if primary_key:
                    field.primary_key = True
                if not_null:
                    field.primary_key = True
                if default_val:
                    field.default_val = default_val
            else:
                raise ValueError("Type Cannot Be Null for Table Field")
        else:
            raise ValueError("Field in Table cannot be NoneType")
    else:
        raise ValueError("Field Dictionary was null")
    return field


def get_tables(layout_dict):
    """
    Get the table objects

    :param layout_dict: The layout dictionary
    :return:    Table objects
    """
    rtables = []
    if layout_dict.get("tables", None):
        for table in layout_dict.get("tables"):
            to = Table()
            if table.get("schema", None):
                to.schema = table["schema"]
            if table.get("table", None):
                to.table = table["table"]
            if table.get("if_not_exists", False):
                to.if_not_exists = True
            if table.get("fields", None):
                fields = [get_field(x) for x in table["fields"]]
                to.fields = fields
            rtables.append(to)
    return rtables


def get_schemas(layout_dict):
    """
    Get the schema objects
    :param layout_dict: The layout dictionary
    :return:    Schema objects
    """
    rschemas = []
    if layout_dict.get("schemas", None):
        for schema in layout_dict.get("schemas"):
            schema_obj = Schema(schema["name"])
            if schema.get("authorization", None):
                schema_obj.authorization = schema["authorization"]
            if schema.get("if_not_exists", False):
                schema_obj.if_not_exists = True
            rschemas.append(schema_obj)
    return rschemas


def create_layout(layout, conn):
    """
    Create the database layout from provided DDL

    Layout should be a dict of the following form (options mirroring those in the functions)
    {
        schemas: [
            {
                name: required,
                authorization: optional user,
                if_not_exists: optional
            },....
        ],
        tables: [{
            schema: optional,
            table: required,
            fields: [{name: required, type: pgtype, notnull: optional, primary_key: optional,...},...],
            if_not_exists: optional
        }],
        indices[{
            name: required,
            unique: optional,
            if_not_exists: optional
        }]
    }

    :param layout:   The json layout
    :param conn:    The connection to use
    """
    if layout and type(layout) is dict:
        schemas = get_schemas(layout)
        tables = get_tables(layout)
        indices = get_indices(layout)
        if schemas and len(schemas) > 0:
            execute_queries(schemas, conn)
        if tables and len(tables) > 0:
            execute_queries(tables, conn)
        if indices and len(indices) > 0:
            execute_queries(indices, conn)
    else:
        raise ValueError("Layout not Found in File")


if __name__ == "__main__":
    arguments = docopt(__doc__, version="DDL Creator 0.1a")
    layout = arguments.get("layout", None)
    conn_string = arguments.get("connstring", None)
    if layout:
        if conn_string:
            if arguments.get("-f", None):
                with open(layout, 'r') as fp:
                    layout = json.load(fp)
            else:
                layout = json.loads(layout)
            with psycopg2.connect(conn_string) as conn:
                create_layout(layout, conn)
        else:
            raise ValueError("Connection String Cannot Be Null")
    else:
        raise ValueError("Missing JSON or File for DDL Creator")
