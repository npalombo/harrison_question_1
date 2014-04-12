__author__ = 'nick'

import unittest
import types

from geodata import fetch


class TestFetch(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_state(self):
        '''
        Get the data for state IL. A list of dictionary objects should be returned.
        '''
        geodata = fetch.get_data_for_state('IL')
        self.assertIsNotNone(geodata)
        self.assertTrue(isinstance(geodata, list))
        self.assertTrue(len(geodata) > 0)
        self.assertTrue(isinstance(geodata[0], dict))

    def _test_bad_state_exception(self):
        return fetch.get_data_for_state('FOOBAR')

    def test_bad_state_exception(self):
        '''
        Attempt to get data for a nonexistant state. An exception should be raised.
        '''
        with self.assertRaises(Exception):
            self._test_bad_state_exception()

    def test_get_all_states(self):
        '''
        Get the generator to iterate over all state data
        '''
        all_state_info = fetch.get_data_for_all_states()
        self.assertIsNotNone(all_state_info)
        self.assertTrue(isinstance(all_state_info, types.GeneratorType))
        # Test one element to see if it downloads
        state_info = all_state_info.next()
        self.assertTrue(isinstance(state_info, dict))
        self.assertIn('state', state_info.keys())
        self.assertIn('geodata', state_info.keys())

if __name__ == "__main__":
    unittest.main()
