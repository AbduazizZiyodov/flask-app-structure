from os import urandom


config = {
    "DEBUG": True,
    "DATABASE": "db.sqlite",
    "SECRET_KEY": urandom(32)
}