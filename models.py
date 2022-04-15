from events import UserCreated, UserBalanceChanged, Event


class User:
    def __init__(self, id: int = None):
        self.events = []
        self.id = id
        self.username = None
        self.balance = None

    def apply(self, event: Event):
        if isinstance(event, UserCreated):
            self.id = event.id
            self.username = event.username
            self.balance = event.balance

        elif isinstance(event, UserBalanceChanged):
            self.balance += event.change

            if self.balance < 0:
                raise ValueError("Balance is negative!")

        self.events.append(event)

    def create_user(self, id: int, username: str, balance: int):
        self.apply(UserCreated(id=id, username=username, balance=balance))

    def change_balance(self, change: int):
        self.apply(UserBalanceChanged(id=self.id, change=change))
