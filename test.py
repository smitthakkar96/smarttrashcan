from app import *
import unittest
import json

class tests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client(self)
        self.invalidData = {"id":"56fe4b3368fa1b0edd4b44a13","per":"10"}
        self.validData = {"id":"56fe4b3368fa1b0edd4b44a1","per":"10"}

    def test_invalid_update(self):
        response=self.app.post('/api/dustbin',data=self.invalidData)
        self.assertEqual(response.status_code,400)

    def test_valid_update(self):
        response=self.app.post('/api/dustbin',query_string=self.validData)
        self.assertEqual(response.status_code,200)
if __name__ == '__main__':
    unittest.main()
