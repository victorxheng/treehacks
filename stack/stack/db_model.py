from sqlmodel import Field

import reflex as rx


class Follows(rx.Model, table=True):
    followed_username: str = Field(primary_key=True)
    follower_username: str = Field(primary_key=True)


class User(rx.Model, table=True):
    """A table of Users."""

    username: str
    password: str


class Tweet(rx.Model, table=True):
    """A table of Tweets."""

    content: str
    created_at: str

    author: str