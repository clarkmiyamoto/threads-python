# threads-python
(Unofficial) Reverse-engineered Python client for [Meta's Threads](https://www.threads.net/). 


# Installation

## Installation for Developers
To install:
```
git clone https://github.com/clarkmiyamoto/threads-python
cd threads-python
pip install .
```

To make updates:
```
cd .../threads-python
git pull
pip install . --upgrade
```


# 🚗 Current Functionality / Roadmap

- **`Client` class: Allows log into specific `User`**
    - [ ] Logged-in Browsing (Read private data)
    - [ ] Wrapper on `User` class
        - [ ] Init `User` from user_id
        - [ ] Init `User` from user_url
    - [ ] Wrapper on `Post` class
        - [ ] Init `Post` from post_id
        - [ ] Init `Post` from user_url
    - [ ] Interface to see explore page/trends (whenever this is eventually added)
    - [ ] Interactions 
        - [ ] Uploads: a text/photo/multi-photo/audio post
        - [ ] Interactions w/ `Post`: like / comment / repost another `Post`
        - [ ] Interactions w/ `User`: (un)follow / remove follower / block

- **`User` class: view attributes, posts, and interactions of a user**
    - [x] Basic attributes (number of followers, is_private, etc.)
    - [ ] List usernames from followers/following
        - [ ] Ability to turn all those usernames into `User` objects
    - [ ] List all posts/replies from select user
        - [ ] `limit=` parameter, select num of a recent post
        - [ ] `daterange=` parameter, select all posts between dates

- **`Post` class: view attributes, reposts, replies associated w/ post**
    - [ ] Basic attributes (num of hearts/comments/views(?)/reposts/etc.)
    - [ ] List reposts/replies from post
