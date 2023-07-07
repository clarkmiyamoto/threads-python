from threads_scrape import Dict

import requests
import re

class Profile:

    def __init__(self, username):
        self.username = username
        self.url = "https://www.threads.net/@" + username
        self._user_id = None

    @property
    def user_id(self) -> int:
        """
        ID associated w/ self.username.
        
        Returns
            self._user_id (int)
        """
        # Prevents from querying multiple times. 
        if self._user_id is None:
            self._user_id = self._fetch_user_id() 

        return self._user_id

    def _fetch_user_id(self) -> int:
        """
        Get ID associated w/ username, method connects to Internet.
        
        Returns:
            user_id (int)"""
        user_id_pattern = r'"props":{"user_id":"(\d+)'

        response = requests.get(self.url)

        match = re.search(user_id_pattern, response.text)
        user_id = int(match.group(1))

        return user_id