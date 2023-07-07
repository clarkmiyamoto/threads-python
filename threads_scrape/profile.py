from threads_scrape import Dict

import requests
import re

class Profile:
    """
    A class representing a user profile on the Threads platform.

    Attributes:
        username (str): The username of the profile.
        url (str): The URL of the profile on the Threads platform.
        user_id (int): The unique identifier of the user.
        RawUserData (Dict): A dictionary containing the raw user data fetched from the Threads platform.
        is_private (bool): Indicates whether the profile is private or not.
        is_verified (bool): Indicates whether the profile is verified or not.
        biography (str): The biography of the user.
        follower_count (int): The number of followers the user has.
        bio_links (list): A list of links in the user's bio.
        full_name (str): The full name of the user.
    """

    def __init__(self, 
                 username: str,
                 fetch_profile_data: bool = True,
                 fetch_post_data: bool = True):
        """
        Initializes a new instance of the Profile class.

        Args:
            username (str): The username of the profile.
            fetch_profile_data (bool, optional): Determines whether profile data should be fetched. Defaults to True.
            fetch_post_data (bool, optional): Determines whether post data should be fetched. Defaults to True.
        """
        self.username = username
        self.url = "https://www.threads.net/@" + username
        self.user_id = self._fetch_user_id()
        self.RawUserData = Dict()

        if fetch_profile_data:
            profile_data = self._fetch_profile_data()
            self.RawUserData.profile_data = profile_data

            self._populate_profile_data(profile_data=profile_data)
        if fetch_post_data:
            """TODO: Next thing to do"""
            pass

    def __str__(self):
        return f"<Profile [{self.username}, {self.user_id}]>"


    def _fetch_user_id(self) -> int:
        """
        Get ID associated w/ username from webscrape.
        
        Returns:
            user_id (int)"""
        user_id_pattern = r'"props":{"user_id":"(\d+)'

        response = requests.get(self.url)

        match = re.search(user_id_pattern, response.text)
        user_id = int(match.group(1))

        return user_id

    def _populate_profile_data(self, profile_data: dict):
        """
        Args:
            profile_data (dict): Value from self._fetch_profile_data(...)
        """
        user_data = profile_data['data']['userData']['user']

        self.is_private  = bool(user_data['is_private'])
        self.is_verified = bool(ser_data['is_verified'])
        self.biography = str(user_data['biography'])
        self.follower_count = int(user_data['follower_count'])
        self.bio_links = user_data['bio_links']
        self.full_name = str(user_data['full_name'])

    def _fetch_profile_data(self) -> dict:
        """
        Fetches associated profile data. JSON data structure.
        
        LIMITATIONS: ONLY supports public profiles. To fix this,
                     We'll need to analyze the `payload`, 
                     `headers['x-fb-lsd']`, or `headers['x-ig-app-id'].
                     I'm currently unsure how to analyze this...
        
        Returns
            profile_data (dict): Raw JSON data associated w/ user profile.
        """
        user_id = self.user_id

        url = "https://www.threads.net/api/graphql"

        payload = f'av=0&__user=0&__a=1&__req=1&__hs=19545.HYP%3Abarcelona_web_pkg.2.1..0.0&dpr=1&__ccg=UNKNOWN&__rev=1007803646&__s=cqfjsw%3Aa9nm1l%3A3td08l&__hsi=7253027684343748032&__dyn=7xeUmwlEnwn8K2WnFw9-2i5U4e0yoW3q32360CEbo1nEhw2nVE4W0om78b87C0yE465o-cw5Mx62G3i0Bo7O2l0Fwqo31wnEfovwRwlE-U2zxe2Gew9O22362W2K0zK5o4q0GpovU1aUbodEGdwtU2ewbS1LwTwNwLw8O1pwr82gxC&__csr=gB-FDy4Bg01lA8lU4u7orx-17z8d329ox0jm8waG22j41K444S7EiwjU8o622Mv60h81045k310VyTo6WA3Mf3Aho0Fc10zIqEu1QgE21zUWzw&__comet_req=29&lsd=W5pozrGtZMsjEHZTFEcE6K&jazoest=21925&__spin_r=1007803646&__spin_b=trunk&__spin_t=1688727104&__jssesw=2&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=BarcelonaProfileRootQuery&variables=%7B%22userID%22%3A%22{user_id}%22%7D&server_timestamps=true&doc_id=23996318473300828'
        headers = {
            'authority': 'www.threads.net',
            'origin': 'https://www.threads.net',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-fb-lsd': 'W5pozrGtZMsjEHZTFEcE6K',
            'x-ig-app-id': '1412234116260832',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        profile_data = response.json()

        return profile_data
    
    







    