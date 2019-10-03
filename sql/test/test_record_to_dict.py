"""
Convert a record tuple to a dictionary

@author Andrew Evans
"""

import unittest
from ..record_to_dict import RecordToDict


class TestRecordToDict(unittest.TestCase):
    """
    Functions for testing record conversion
    """

    def test_convert_record_to_dict(self):
        """
        Test the record conversion
        """
        rdict = RecordToDict(["v1", "v2"])
        vals = ["a", "b"]
        rdict = rdict.convert_record(vals)
        v1 = rdict.get("v1", None)
        v2  = rdict.get("v2", None)
        assert(v1 is not None and v1 == "a")
        assert(v2 is not None and v2 == "b")
