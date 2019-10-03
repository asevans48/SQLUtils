"""
Test a postgresql record iterator

@author Andrew Evans
"""

from ..pgrecord_iterator import PGRecordIterator
import psycopg2
import unittest


class TestPGRecordIterator(unittest.TestCase):
    """
    Test cases for Postgres Record Iteration
    """

    def get_conn(self):
        conn = psycopg2.connect(dbname="selective", user="postgres", password="rtp*4500")
        return conn

    def test_iterator_should_execute_query(self):
        """
        The iterator should initialize
        """
        conn = self.get_conn()
        pgr = PGRecordIterator(conn, "SELECT * FROM vault.sat_agent", "test")
        pgit = iter(pgr)
        rval = next(pgit)
        assert(type(rval) is dict)
        assert(rval is not None)
        pgr.close_cursor()
        conn.close()


    def test_iterator_should_obtain_multiple_records(self):
        """
        The iterator should obtain multiple records
        """
        conn = self.get_conn()
        pgr = PGRecordIterator(conn, "SELECT * FROM vault.sat_agent")
        pgit = iter(pgr)
        ival = 0
        for rval in pgit:
            ival += 1
            assert (rval is not None)
        assert(ival > 0)
        pgr.close_cursor()
        conn.close()

    def test_iterator_should_not_create_error_on_empty_result(self):
        """
        Iterator should not fail if no results are found
        """
        conn = self.get_conn()
        pgr = PGRecordIterator(conn, "SELECT NULL where false")
        pgit = iter(pgr)
        rval = next(pgit, None)
        assert(rval is None)
        pgr.close_cursor()
        conn.close()
