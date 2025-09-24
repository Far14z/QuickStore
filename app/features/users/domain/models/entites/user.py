from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    def __init__(self, id: int, name: str, email: str, password_hash: str):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash