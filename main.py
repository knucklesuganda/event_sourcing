from repository import UserRepository
from models import User


def main():
    user = User()
    repository = UserRepository()

    user_id = repository.get_user_id()
    user.create_user(
        id=user_id,
        username="Andrey",
        balance=0,
    )

    user.change_balance(10)
    user.change_balance(20)
    user.change_balance(100)
    user.change_balance(-25)

    repository.save(user)

    user2 = repository.get(user_id)
    user2.change_balance(10)
    print(user2.username, user2.balance, user2.events)

    repository.save(user2)
    print(repository.get(user2.id).events)


if __name__ == '__main__':
    main()
