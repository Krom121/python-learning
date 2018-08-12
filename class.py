class User:
    pass
user1 = User()
user1.first_name = "stephen"
user1.last_name = "joker"

print(user1.first_name)
print(user1.last_name)

first_name = "Arthur"
last_name = "batman"

print(first_name, last_name)
print(user1.first_name, user1.last_name)

class User: 

    """ for now i am storing their name and birthday 
    soon will store more info about user."""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd

user = User("Stephen Macgregor", 19820305) 
print(user.name)
print(user.birthday)

#help(User)

class Employee:
    pass

