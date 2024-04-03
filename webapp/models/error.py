from typing import TypedDict


class DB_Error(TypedDict):
    db_error: str


class API_Error(TypedDict):
    api_error: str


class LOGIN_Error(TypedDict):
    login_error: str
