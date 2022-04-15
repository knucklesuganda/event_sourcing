from models import User


class UserRepository:
    users = {}

    def save(self, user: User):
        if user.id is not None:
            self.users[user.id] = list(user.events)
        else:
            raise ValueError("Id is None!")

    def get(self, id: int):
        user = User(id)
        events = self.users.get(user.id)

        if events is None:
            raise ValueError("User was not found!")

        for event in events:
            user.apply(event)

        return user

    def get_user_id(self):
        return len(self.users)
