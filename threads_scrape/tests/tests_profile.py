import unittest

from threads_scrape import Profile


class ProfileTestCase(unittest.TestCase):
    """Unit test for Profile class"""

    _profile = Profile(username="clarkmiyamoto")

    def test_user_id(self):
        self.assertEqual(self._profile.user_id, 
                         1035181405, 
                         "User ID does not match expected value")
