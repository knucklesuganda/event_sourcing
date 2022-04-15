from dataclasses import dataclass


class Event:
    pass


@dataclass()
class UserCreated(Event):
    id: int
    username: str
    balance: int


@dataclass()
class UserBalanceChanged(Event):
    id: int
    change: int
