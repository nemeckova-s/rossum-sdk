from dataclasses import dataclass


@dataclass
class UserRole:
    id: int
    name: str
    url: str