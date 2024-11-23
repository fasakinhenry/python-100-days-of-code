# Create a class
class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0

# create an object from the User class
user_1 = User()
