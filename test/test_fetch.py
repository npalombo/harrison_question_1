__author__ = 'nick'

import unittest

from geodata import fetch


class TestFetch(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_state(self):
        '''
        Get the data for state IL. A list of dictionary objects should be returned.
        '''
        state_info = fetch.get_data_for_state('IL')
        self.assertIsNotNone(state_info)
        self.assertTrue(isinstance(state_info, list))
        self.assertTrue(len(state_info) > 0)
        self.assertTrue(isinstance(state_info[0], dict))

    def _test_bad_state_exception(self):
        return fetch.get_data_for_state('FOOBAR')

    def test_bad_state_exception(self):
        '''
        Attempt to get data for a nonexistant state. An exception should be raised.
        '''
        with self.assertRaises(Exception):
            self._test_bad_state_exception()


if __name__ == "__main__":
    unittest.main()
