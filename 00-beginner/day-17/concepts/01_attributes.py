# Create a class
class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0

# create an object from the User class
user_1 = User("001", "Henry")

# Accessing the number of followers which is default
print(user_1.followers)
print(user_1.username)
