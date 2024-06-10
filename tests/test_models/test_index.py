#!/usr/bin/python3
"""
Test module for index
"""
import unittest
import inspect
import pep8
from api.v1.app import app


class TestIndexDocs(unittest.TestCase):
    """Tests to check the documentation and style of index module"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.index_f = inspect.getmembers(app, inspect.isfunction)

    def test_pep8_conformance_index(self):
        """Test that api/v1/views/index.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/index.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestIndex(unittest.TestCase):
    """ Test case for index """

    def setUp(self):
        """ Set up test client """
        self.app = app.test_client()

    def test_status(self):
        """ Test /status route """
        response = self.app.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "OK"})


if __name__ == '__main__':
    unittest.main()
